from minio import Minio
import os
import config

def realizar_ingestao():
    print("--- Iniciando Ingestão (Bronze) ---")
    
    # 1. Conectar ao MinIO
    # Removemos o 'http://' para o cliente Minio oficial, pois ele espera apenas host:port
    endpoint_clean = config.MINIO_ENDPOINT.replace("http://", "")
    
    client = Minio(
        endpoint_clean,
        access_key=config.MINIO_ACCESS_KEY,
        secret_key=config.MINIO_SECRET_KEY,
        secure=False
    )

    # 2. Criar o Bucket se não existir
    if not client.bucket_exists(config.BUCKET_NAME):
        client.make_bucket(config.BUCKET_NAME)
        print(f"Bucket '{config.BUCKET_NAME}' criado.")
    else:
        print(f"Bucket '{config.BUCKET_NAME}' já existe.")

    # 3. Upload do arquivo (Dataset Local -> Raw)
    # Caminho do arquivo dentro do container Jupyter
    arquivo_origem = "datasets/supermarket_sales.csv" 
    caminho_destino = "raw/supermarket_sales.csv"

    if os.path.exists(arquivo_origem):
        client.fput_object(
            config.BUCKET_NAME, 
            caminho_destino, 
            arquivo_origem
        )
        print(f"Sucesso: Arquivo salvo em 's3://{config.BUCKET_NAME}/{caminho_destino}'")
    else:
        print(f"ERRO: Arquivo {arquivo_origem} não encontrado. Verifique a pasta datasets.")

if __name__ == "__main__":
    realizar_ingestao()