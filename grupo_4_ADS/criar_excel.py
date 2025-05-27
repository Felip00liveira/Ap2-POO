import pandas as pd

empregado_data = [
    {
        "nss": 111111111,
        "pnome": "joão",
        "mnome": "carlos",
        "snome": "silva",
        "sexo": "M",
        "datanasc": "1985-10-10",
        "endereco": "rua a, 100",
        "salario": 60000.0,
        "numero_dep": 1,
        "nss_supervisor": None,
    },
    {
        "nss": 222222222,
        "pnome": "maria",
        "mnome": "eduarda",
        "snome": "souza",
        "sexo": "F",
        "datanasc": "1979-03-21",
        "endereco": "av. b, 200",
        "salario": 90000.0,
        "numero_dep": 2,
        "nss_supervisor": None,
    },
    {
        "nss": 333333333,
        "pnome": "pedro",
        "mnome": "henrique",
        "snome": "oliveira",
        "sexo": "M",
        "datanasc": "1990-07-15",
        "endereco": "rua c, 300",
        "salario": 50000.0,
        "numero_dep": 1,
        "nss_supervisor": 222222222,
    },
]

departamento_data = [
    {"numero": 1, "nome": "pesquisa", "nss_emp": 222222222, "datainicio": "2021-01-01", "nro_emp": 2},
    {"numero": 2, "nome": "administração", "nss_emp": 111111111, "datainicio": "2020-06-15", "nro_emp": 1},
    {"numero": 3, "nome": "ti", "nss_emp": 333333333, "datainicio": "2022-09-10", "nro_emp": 3},
]

localizacao_data = [
    {"numero_dep": 1, "localizacao": "rio de janeiro"},
    {"numero_dep": 1, "localizacao": "são paulo"},
    {"numero_dep": 2, "localizacao": "belo horizonte"},
    {"numero_dep": 3, "localizacao": "curitiba"},
]

projeto_data = [
    {"numero": 1, "nome": "produtox", "localizacao": "rio de janeiro", "numero_dep": 1},
    {"numero": 2, "nome": "reestruturação", "localizacao": "são paulo", "numero_dep": 2},
    {"numero": 3, "nome": "website", "localizacao": "curitiba", "numero_dep": 3},
]

trabalha_em_data = [
    {"nss_emp": 111111111, "numero_proj": 1, "horas": 20.0},
    {"nss_emp": 111111111, "numero_proj": 2, "horas": 10.0},
    {"nss_emp": 222222222, "numero_proj": 2, "horas": 30.0},
    {"nss_emp": 333333333, "numero_proj": 1, "horas": 15.0},
    {"nss_emp": 333333333, "numero_proj": 3, "horas": 25.0},
]

dependente_data = [
    {"nss_emp": 111111111, "nome": "lucas", "sexo": "M", "datanasc": "2010-11-05", "tiporel": "filho"},
    {"nss_emp": 111111111, "nome": "laura", "sexo": "F", "datanasc": "2012-02-18", "tiporel": "filha"},
    {"nss_emp": 222222222, "nome": "carlos", "sexo": "M", "datanasc": "2015-08-22", "tiporel": "filho"},
]

df_empregado = pd.DataFrame(empregado_data).astype({
    'nss': 'int64',
    'pnome': 'string',
    'mnome': 'string',
    'snome': 'string',
    'sexo': 'string',
    'datanasc': 'string',
    'endereco': 'string',
    'salario': 'float64',
    'numero_dep': 'int64',
    'nss_supervisor': 'Int64'
})

df_departamento = pd.DataFrame(departamento_data).astype({
    'numero': 'int64',
    'nome': 'string',
    'nss_emp': 'Int64',
    'datainicio': 'string',
    'nro_emp': 'int64'
})

df_localizacao = pd.DataFrame(localizacao_data).astype({
    'numero_dep': 'int64',
    'localizacao': 'string'
})

df_projeto = pd.DataFrame(projeto_data).astype({
    'numero': 'int64',
    'nome': 'string',
    'localizacao': 'string',
    'numero_dep': 'Int64'
})

df_trabalha_em = pd.DataFrame(trabalha_em_data).astype({
    'nss_emp': 'int64',
    'numero_proj': 'int64',
    'horas': 'float64'
})

df_dependente = pd.DataFrame(dependente_data).astype({
    'nss_emp': 'int64',
    'nome': 'string',
    'sexo': 'string',
    'datanasc': 'string',
})

df_empregado = pd.DataFrame(empregado_data)
df_departamento = pd.DataFrame(departamento_data)
df_localizacao = pd.DataFrame(localizacao_data)
df_projeto = pd.DataFrame(projeto_data)
df_trabalha_em = pd.DataFrame(trabalha_em_data)
df_dependente = pd.DataFrame(dependente_data)

with pd.ExcelWriter("exemplo_dados.xlsx") as writer:
    df_empregado.to_excel(writer, sheet_name="empregado", index=False)
    df_departamento.to_excel(writer, sheet_name="departamento", index=False)
    df_localizacao.to_excel(writer, sheet_name="localizacao", index=False)
    df_projeto.to_excel(writer, sheet_name="projeto", index=False)
    df_trabalha_em.to_excel(writer, sheet_name="trabalha_em", index=False)
    df_dependente.to_excel(writer, sheet_name="dependente", index=False)