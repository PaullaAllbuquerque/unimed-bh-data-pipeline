with source as (
    select * from {{ source('unimed_raw', 'stg_unimed_locais_raw') }}
),

renamed as (
    select
        trim(nome_local) as nome_local,
        trim(endereco) as endereco,
        trim(bairro) as bairro,
        trim(cidade) as cidade,
        trim(telefone) as telefone,
        trim(tipo_atendimento) as tipo_atendimento
    from source
)

select * from renamed