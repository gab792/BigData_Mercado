## 📌 Visão Geral

Este projeto foi desenvolvido para solucionar problemas de gerenciamento de dados enfrentados por um supermercado, que utilizava diversas planilhas e sistemas desconectados para armazenar informações de vendas, produtos, categorias e estoques.

A solução proposta consiste em um *pipeline completo de ingestão, processamento, armazenamento e análise*, permitindo gerar insights valiosos como:

* Produtos mais lucrativos
* Análises de sazonalidade
* Previsões e tendências de vendas
* Desempenho por categoria e produto
* Horários e dias de maior movimentação

---

## 🎯 Objetivos do Projeto

### *Objetivo Geral*

Construir um pipeline robusto para gestão e tratamento dos dados de vendas do supermercado.

### *Objetivos Específicos*

* Consolidar dados brutos em um *Data Lake estruturado*.
* Automatizar o processo de ingestão (batch ou streaming).
* Processar e limpar dados para análises confiáveis.
* Criar camadas de dados: *Raw, Bronze, Silver e Gold*.
* Gerar dashboards e KPIs acionáveis.
* Documentar arquitetura e decisões técnicas.

### *Justificativa Técnica*

A arquitetura adota boas práticas de engenharia de dados, garantindo:

* Escalabilidade do armazenamento
* Processamento eficiente (Spark ou Pandas)
* Visualização de alto nível com dashboards
* Pipeline organizado por camadas
* Possibilidade de integração futura com outros sistemas

---

## 🧩 Escopo da Solução

### ✔️ *Incluído*

* Ingestão de dados (CSV/JSON)
* Pipeline de processamento
* Data Lake em MinIO/S3
* Camadas: Raw, Bronze, Silver, Gold
* Dashboard com KPIs de vendas
* Organização do repositório
* Documentação completa

### ❌ *Não incluído*

* Modelos avançados de previsão
* APIs externas
* Interface web
* Integração com ERP real 