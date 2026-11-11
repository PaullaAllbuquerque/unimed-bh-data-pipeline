-- Configura a materialização como view no dbt
{{ config(materialization='view') }}

WITH dados_brutos AS (
    -- Seleciona os dados vindos da camada raw
    SELECT 
        texto_link,
        url_destino,
        origem
    FROM {{ ref('tb_portal_unimed_bruto') }}
),

dados_padronizados AS (
    SELECT
        -- Padroniza o texto do link removendo espaços extras
        TRIM(texto_link) AS nome_menu,
        
        -- Garante a estrutura correta da URL
        TRIM(url_destino) AS link_acesso,
        
        -- Converte a origem para caixa alta
        UPPER(origem) AS fonte_dados
    FROM dados_brutos
    WHERE texto_link IS NOT NULL AND texto_link != ''
)

SELECT * FROM dados_padronizados;