import pandas as pd
import glob
import os


caminho_diretorio = r"Microdados_Enade_2023\DADOS"

# Listar todos os arquivos que começam com "microdados2022_arq" e terminam em ".txt"
arquivos = glob.glob(os.path.join(caminho_diretorio, "microdados2023_arq*.txt"))

# Criar uma lista para armazenar os DataFrames
dfs = []

# Ler cada arquivo e adicioná-lo à lista
for arquivo in arquivos:
    df = pd.read_csv(arquivo, delimiter=";", encoding="latin1")  # Ajuste o delimitador se necessário
    dfs.append(df)

# Concatenar todos os DataFrames
df_final = pd.concat(dfs, ignore_index=True)

# Gerar a base de dados final filtrando por curso (CO_GRUPO) e região do Brasil (CO_REGIAO_CURSO)
# 6411 e 4 são "Engenharia de Computacão I" e "Sul", respectivamente.
df_final = df_final[
    (df_final["CO_GRUPO"] == 6411) & 
    (df_final["CO_REGIAO_CURSO"] == 4)]

# Exibir a quantidade de linhas e colunas. São 887 linhas e 125 colunas.
print(df_final.head())

# Gerar a base de dados final em CSV
df_final.to_csv(os.path.join(caminho_diretorio, "base_final.csv"), index=False, sep=";")


