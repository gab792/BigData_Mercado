import pandas as pd
from sqlalchemy import create_engine
import config
import os

storage_options = {
    "key": config.MINIO_ACCESS_KEY,
    "secret": config.MINIO_SECRET_KEY,
    "client_kwargs": {"endpoint_url": config.MINIO_ENDPOINT}
}

def processar_silver():
    print("--- Iniciando Camada Silver (Limpeza e Parquet) ---")

    caminho_raw = f"s3://{config.BUCKET_NAME}/raw/supermarket_sales.csv"
    try:
        df = pd.read_csv(caminho_raw, storage_options=storage_options)
        print(f"Lido {len(df)} linhas da camada Raw.")
    except Exception as e:
        print(f"Erro ao ler Raw: {e}")
        return None

    df.columns = [c.lower().replace(" ", "_") for c in df.columns]
    rename_map = {
        'invoice_id': 'id_fatura',
        'branch': 'filial',
        'city': 'cidade',
        'customer_type': 'tipo_cliente',
        'gender': 'genero',
        'product_line': 'linha_produto',
        'unit_price': 'preco_unitario',
        'quantity': 'quantidade',
        'tax_5%': 'imposto',
        'total': 'total_venda',
        'date': 'data_venda',
        'time': 'hora_venda',
        'payment': 'pagamento',
        'cogs': 'custo_venda',
        'gross_income': 'lucro_bruto',
        'rating': 'avaliacao'
    }
    df = df.rename(columns=rename_map)
    
    df['data_venda'] = pd.to_datetime(df['data_venda'])
    
    caminho_silver = f"s3://{config.BUCKET_NAME}/silver/vendas_tratadas.parquet"
    df.to_parquet(caminho_silver, storage_options=storage_options)
    print(f"Sucesso: Dados limpos salvos em '{caminho_silver}'")
    
    return df

def processar_gold(df_silver):
    print("--- Iniciando Camada Gold (Agregação e Banco) ---")
    
    if df_silver is None:
        print("Erro: Dataframe Silver vazio.")
        return

    df_gold = df_silver.groupby(['cidade', 'linha_produto', 'genero'])[['total_venda', 'quantidade', 'lucro_bruto']].sum().reset_index()
    
    df_gold['data_processamento'] = pd.Timestamp.now()

    print(f"Gerada tabela Gold com {len(df_gold)} linhas agregadas.")

    engine = create_engine(config.DB_CONNECTION_URI)
    
    try:
        df_gold.to_sql('kpi_vendas_cidade', engine, if_exists='replace', index=False)
        print("Sucesso: Tabela 'kpi_vendas_cidade' salva no PostgreSQL.")
    except Exception as e:
        print(f"Erro ao salvar no Banco: {e}")

if __name__ == "__main__":
    df = processar_silver()
    processar_gold(df)