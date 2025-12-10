# 🛒 Análise de Vendas de um Supermercado

Pipeline de Dados • Data Lake • Dashboards • ETL

## 📌 Visão Geral

Este projeto foi desenvolvido para solucionar problemas de gerenciamento de dados enfrentados por um supermercado, que utilizava diversas planilhas e sistemas desconectados para armazenar informações de vendas, produtos, categorias e estoques.

A solução proposta consiste em um **pipeline completo de ingestão, processamento, armazenamento e análise**, permitindo gerar insights valiosos como:

* Produtos mais lucrativos
* Análises de sazonalidade
* Previsões e tendências de vendas
* Desempenho por categoria e produto
* Horários e dias de maior movimentação

---

## 🎯 Objetivos do Projeto

### **Objetivo Geral**

Construir um pipeline robusto para gestão e tratamento dos dados de vendas do supermercado.

### **Objetivos Específicos**

* Consolidar dados brutos em um **Data Lake estruturado**.
* Automatizar o processo de ingestão (batch ou streaming).
* Processar e limpar dados para análises confiáveis.
* Criar camadas de dados: **Raw, Bronze, Silver e Gold**.
* Gerar dashboards e KPIs acionáveis.
* Documentar arquitetura e decisões técnicas.

### **Justificativa Técnica**

A arquitetura adota boas práticas de engenharia de dados, garantindo:

* Escalabilidade do armazenamento
* Processamento eficiente (Spark ou Pandas)
* Visualização de alto nível com dashboards
* Pipeline organizado por camadas
* Possibilidade de integração futura com outros sistemas

---

## 🧩 Escopo da Solução

### ✔️ **Incluído**

* Ingestão de dados (CSV/JSON)
* Pipeline de processamento
* Data Lake em MinIO/S3
* Camadas: Raw, Bronze, Silver, Gold
* Dashboard com KPIs de vendas
* Organização do repositório
* Documentação completa

### ❌ **Não incluído**

* Modelos avançados de previsão
* APIs externas
* Interface web
* Integração com ERP real

---

## 🏗️ Arquitetura do Pipeline

O pipeline foi dividido em **4 etapas principais**:

### **1. Ingestão**

* Leitura de arquivos CSV/JSON
* Upload automático para a camada **Raw**

### **2. Processamento**

* Normalização de colunas
* Conversão de tipos
* Tratamento de valores ausentes
* Agregações (por produto, categoria, data, loja etc.)

### **3. Armazenamento**

* **Raw** → dados brutos
* **Bronze** → dados padronizados
* **Silver** → dados limpos
* **Gold** → dados analíticos prontos para dashboards

### **4. Análise**

* Construção de dashboards com:

  * Metabase
  * Superset
  * Power BI

---

## 🛠️ Ferramentas e Tecnologias

* **Python (Pandas / PySpark)** – processamento
* **MinIO / AWS S3** – Data Lake
* **Docker Compose** – infraestrutura
* **Jupyter Notebooks** – exploração
* **Superset / Metabase / Power BI** – visualização
* **GitHub / Bitbucket** – versionamento
* **Confluence** – documentação

---

## ⚙️ Decisões Técnicas

### **Data Lake → MinIO**

* Escolhido por simular S3 localmente
* Alternativa descartada: armazenamento local

### **Formato de Arquivos → Parquet**

* Mais rápido, compacto e eficiente
* CSV descartado por ser lento e ocupar mais espaço

### **Processamento → Spark ou Pandas**

* Spark: ideal para grandes volumes
* Pandas: suficiente para datasets médios

### **Dashboard → Superset ou Power BI**

* Superset: ideal para ambiente técnico
* Power BI: melhor para apresentação comercial

---

## 🚀 Guia de Execução

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/seu-repo/projeto-supermercado.git
```

### 2️⃣ Subir os containers

```bash
docker-compose up -d
```

### 3️⃣ Inserir arquivos brutos

Adicionar os arquivos na pasta:

```
/datasets/raw
```

### 4️⃣ Executar o pipeline

```bash
python src/pipeline.py
```

### 5️⃣ Visualizar dashboards

* Abrir Metabase ou Superset
* Conectar-se à camada **Gold**
* Explorar KPIs e filtros

---

## 📦 Dependências

* Python ≥ 3.10
* Pandas ≥ 2.0
* PySpark (opcional)
* Docker ≥ 20.10
* docker-compose ≥ 1.29
* MinIO configurado
* Superset / Metabase

---

## 📊 Descrição dos Dados

### **Origem:**

Simulação de vendas reais de supermercado.

### **Formato:**

Arquivos CSV ou JSON contendo vendas diárias.

### 📁 **Esquema Exemplo – vendas**

| Campo        | Tipo     | Descrição                             |
| ------------ | -------- | ------------------------------------- |
| sale_id      | int      | ID da venda                           |
| date         | datetime | Data da venda                         |
| product_id   | int      | ID do produto                         |
| product_name | string   | Nome do produto                       |
| category     | string   | Categoria (frutas, bebidas, limpeza…) |
| unit_price   | float    | Preço unitário                        |
| quantity     | int      | Quantidade vendida                    |
| total        | float    | Valor total da venda                  |
| store        | string   | Unidade/loja                          |

---

## ⚠️ Limitações Conhecidas

* Dados podem conter inconsistências
* Arquivos muito grandes exigem Spark
* Dashboards dependem do Data Lake
* Crescimento do volume pode exigir Airflow
* Não há streaming real (Kafka)

---

## 👩‍💻 Trabalho Individual

### **Antuane Felipe**

### **Gabrielle Palma**

* Estruturação da documentação no Confluence
* Construção da camada Silver
* Implementação da limpeza dos dados
* Criação parcial do dashboard no Superset

### **Karolina Mendes**

### **Victória Nascimento**