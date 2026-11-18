with source as (
    select * from {{ source('unimed_raw', 'stg_unimed_locais_raw') }}
),

renamed as (
    select
        trim(texto_link) as texto_link,
        trim(url_destino) as url_destino,
        trim(origem) as origem,
        case
            when url_destino like 'http%' then 'Link Externo'
            when url_destino like '#%' then 'Âncora Interna'
            else 'Rota Interna Portal'
        end as tipo_url
    from source
    where texto_link is not null
      and trim(texto_link) != ''
)

select * from renamed
