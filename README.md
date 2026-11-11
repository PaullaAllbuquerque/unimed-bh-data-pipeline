# 🚀 Unimed-BH Data Engineering Pipeline (Case de Estudo)

> ⚠️ **Status do Projeto:** 🛠️ *Em construção.*  
> A primeira fase (Ingestão com Python, qualidade com Pytest e Staging no dbt) já está implementada. A integração e carga no Data Warehouse (Snowflake) está atualmente em desenvolvimento.

Este repositório consiste em um **projeto de demonstração técnica (Case Prático)** desenvolvido com o objetivo de consolidar e apresentar conhecimentos práticos na área de **Engenharia de Dados**. O projeto simula a extração automatizada, estruturação e transformação de dados institucionais públicos do portal Unimed-BH, aplicando arquitetura moderna e boas práticas corporativas.

## 🎯 Objetivo do Projeto
Demonstrar na prática o domínio do ciclo completo de um pipeline de dados (End-to-End): da ingestão automatizada de dados brutos à garantia de qualidade, documentação e transformação orientada a Data Warehouse.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.10+
* **Ingestão & Extração:** `requests`, `BeautifulSoup4`, `pandas`
* **Transformação & Governança:** `dbt` (data build tool)
* **Qualidade de Dados:** `pytest`, testes nativos do `dbt`
* **Data Warehouse (Módulo 2 - Em andamento):** Snowflake

## 🏗️ Arquitetura do Projeto
1. **Ingestão (Python):** Extração de dados públicos do portal Unimed-BH.
2. **Camada Raw (Bronze):** Armazenamento imutável dos dados brutos em formato `.csv`.
3. **Garantia de Qualidade (Pytest):** Validação unitária de existência, esquema e integridade dos arquivos gerados.
4. **Camada Staging (Silver / dbt):** Padronização, limpeza (CTEs, `TRIM`, `UPPER`) e aplicação de contratos de dados via `schema.yml`.
5. **Data Warehouse (Módulo 2):** Carga e modelagem analítica avançada no Snowflake.

## 🚀 Como Executar
```bash
# Executar a ingestão de dados
python ingestao/extrair_unimed.py

# Executar a suíte de testes unitários
pytest

# Executar a modelagem e testes no dbt
dbt run
dbt test
