# 🩺 Unimed-BH Analytics & Data Engineering Pipeline

Pipeline de Engenharia de Dados de ponta a ponta desenvolvida para extrair, carregar, modelar e validar dados públicos do portal da Unimed-BH, transformando informações brutas em assets analíticos estruturados utilizando Python, Snowflake e dbt.

---

## 🏗️ Arquitetura da Solução

1. **Extração (Ingestão Raw):** Script em Python utilizando `pandas` e `snowflake-connector-python` para ler fontes de dados estruturadas a partir de varreduras do portal.
2. **Armazenamento:** Camada de Staging (`staging`) hospedada no **Snowflake** (`UNIMED_DB`), garantindo isolamento de ambientes e governança.
3. **Transformação e Qualidade (dbt):** Modelagem de dados declarativa (`stg_unimed_locais`), com testes automatizados de integridade integrados.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.10+**: Automação de ingestão e manipulação de dados (`pandas`).
* **Snowflake**: Data Warehouse em nuvem para processamento e armazenamento escalável.
* **dbt (data build tool)**: Transformação de dados, documentação e testes de qualidade.
* **Git & GitHub**: Versionamento de código e portfólio.

---

## 🧪 Qualidade e Testes de Dados (dbt Tests)
O projeto conta com testes automatizados na camada de staging para garantir a confiabilidade dos dados:
* `not_null`: Assegura que colunas críticas (como `texto_link`, `url_destino` e `origem`) não contenham valores nulos.
* `accepted_values`: Valida a integridade dos tipos de URLs e rotas mapeadas.

---

## 🚀 Como Executar o Projeto

1. Clone o repositório:
   `git clone [https://github.com/PaullaAllbuquerque/unimed_analytics_project.git](https://github.com/PaullaAllbuquerque/unimed_analytics_project.git)`
   `cd unimed_analytics_project`

2. Configure o seu ambiente virtual e instale as dependências:
   `python3 -m venv .venv`
   `source .venv/bin/activate`
   `pip install -r requirements.txt`

3. Configure o seu arquivo `~/.dbt/profiles.yml` com as credenciais do Snowflake.

4. Execute os modelos e testes do dbt:
   `dbt run`
   `dbt test`

---
Feito com 💜 por **Paula Pires e Albuquerque de Mello**.