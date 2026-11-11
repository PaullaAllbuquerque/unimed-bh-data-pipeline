import pandas as pd
import requests
from bs4 import BeautifulSoup

# URL real e oficial da Unimed-BH
url = "https://www.unimedbh.com.br"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

print("🔄 Acessando o portal oficial da Unimed-BH...")

try:
    response = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    # Extraindo links institucionais e de atendimento reais da página principal
    dados_coletados = []
    for link in soup.find_all("a", href=True):
        texto = link.get_text(strip=True)
        url_destino = link["href"]
        if len(texto) > 3:  # Filtra textos válidos
            dados_coletados.append({
                "texto_link": texto,
                "url_destino": url_destino,
                "origem": "Web Scraping Portal Unimed-BH"
            })

    # Criando o DataFrame com os dados raspados da página real
    df = pd.DataFrame(dados_coletados)
    
    # Removendo duplicadas caso existam
    df = df.drop_duplicates(subset=["texto_link"])

    # Salvando o resultado bruto dentro da pasta raw
    df.to_csv("raw/tb_portal_unimed_bruto.csv", index=False)
    print("✅ Web scraping concluído! Arquivo 'tb_portal_unimed_bruto.csv' salvo na pasta raw.")

except Exception as e:
    print(f"❌ Erro ao realizar o scraping na página real: {e}")