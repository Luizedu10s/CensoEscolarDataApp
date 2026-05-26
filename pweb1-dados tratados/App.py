import pandas as pd
import json

# Leitura dos dados do csv e geração de uma dataframe do pandas
df_escolas = pd.read_csv(
    "Tabela_Escola_2025.csv",
    sep=";",
    encoding="latin1",
    low_memory=False
)

# leitura dos arquvios csc e geração de uma dataframe do pandas
df_matriculas = pd.read_csv(
    "Tabela_Matricula_2025.csv",
    sep=";",
    encoding="latin1",
    low_memory=False
)

# colunas desejadas de cada arquivo csv
colunas_escolas = [
    "NO_ENTIDADE", "CO_ENTIDADE", "NO_UF", "SG_UF", 
    "CO_UF", "NO_MUNICIPIO", "CO_MUNICIPIO", "NO_MESORREGIAO",
    "CO_MESORREGIAO", "NO_MICRORREGIAO", "CO_MICRORREGIAO",
    "NU_ANO_CENSO", "NO_REGIAO", "CO_REGIAO"
]

# Colunas da tabela de matriculas
colunas_matriculas = [
    "CO_ENTIDADE", "QT_MAT_BAS",
    "QT_MAT_INF", "QT_MAT_FUND",
    "QT_MAT_MED", "QT_MAT_PROF",
    "QT_MAT_EJA", "QT_MAT_ESP"
]

# Colunas selecionadas
data_escolas = df_escolas[colunas_escolas]
data_matriculas = df_matriculas[colunas_matriculas]

# junção dos dados das escolas e matriculas através do relacionamento com a coluna co_entidade.
df = pd.merge(
    data_escolas,
    data_matriculas,
    on="CO_ENTIDADE",
    how="inner"
)

# instituições da paraíba
df_pb = df[df["SG_UF"] == "PB"]

# Ordenação das 30 primeiras instituições com mais matriculas
df_top30 = df_pb.sort_values(
    by="QT_MAT_BAS",
    ascending=False
).head(30)

# geração do arquivo json
resultado = df_top30.to_dict(
    orient="records"
)

# exportar o json com as 30 instituições da paraiba
with open("top30_paraiba.json", "w", encoding="utf-8") as f:
    json.dump(
        resultado,
        f,
        ensure_ascii=False,
        indent=4
    )