## 🏗️ Arquitetura do Pipeline

O pipeline foi dividido em *4 etapas principais*:

### *1. Ingestão*

* Leitura de arquivos CSV/JSON
* Upload automático para a camada *Raw*

### *2. Processamento*

* Normalização de colunas
* Conversão de tipos
* Tratamento de valores ausentes
* Agregações (por produto, categoria, data, loja etc.)

### *3. Armazenamento*

* *Raw* → dados brutos
* *Bronze* → dados padronizados
* *Silver* → dados limpos
* *Gold* → dados analíticos prontos para dashboards

### *4. Análise*

* Construção de dashboards com:

  * Metabase
  * Superset
  * Power BI

---

## 🛠️ Ferramentas e Tecnologias

* *Python (Pandas / PySpark)* – processamento
* *MinIO / AWS S3* – Data Lake
* *Docker Compose* – infraestrutura
* *Jupyter Notebooks* – exploração
* *Superset / Metabase / Power BI* – visualização
* *GitHub / Bitbucket* – versionamento
* *Confluence* – documentação