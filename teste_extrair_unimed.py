import os
import pandas as pd
import pytest

# Teste 1: Verifica se a pasta raw existe
def test_diretorio_raw_existe():
    assert os.path.exists("raw"), "A pasta 'raw' não foi encontrada no projeto."

# Teste 2: Verifica se o arquivo CSV bruto foi gerado pela ingestão
def test_arquivo_csv_gerado():
    caminho_csv = "raw/tb_portal_unimed_bruto.csv"
    assert os.path.exists(caminho_csv), f"O arquivo {caminho_csv} não existe. Rode a ingestão primeiro."

# Teste 3: Valida a estrutura e conteúdo dos dados raspados
def test_qualidade_dados_extraidos():
    caminho_csv = "raw/tb_portal_unimed_bruto.csv"
    df = pd.read_csv(caminho_csv)
    
    # Valida se a tabela não veio vazia
    assert not df.empty, "O arquivo CSV está completamente vazio."
    
    # Valida se as colunas esperadas do scraping estão presentes
    colunas_esperadas = {"texto_link", "url_destino", "origem"}
    assert colunas_esperadas.issubset(set(df.columns)), f"As colunas do CSV não batem. Esperado: {colunas_esperadas}"