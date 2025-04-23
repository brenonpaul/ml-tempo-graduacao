import pandas as pd
import glob
import os

caminho_diretorio = r"Microdados_Enade_2023\DADOS"

# Buscar todos os arquivos .csv com padrão especificado
arquivos = glob.glob(os.path.join(caminho_diretorio, "microdados2023_arq*.csv"))

dfs = []
colunas_existentes = set()

for arquivo in arquivos:
    df = pd.read_csv(arquivo, delimiter=";", encoding="latin1")
    
    # Filtra apenas colunas ainda não adicionadas
    colunas_novas = [col for col in df.columns if col not in colunas_existentes]
    
    if colunas_novas:
        dfs.append(df[colunas_novas])
        colunas_existentes.update(colunas_novas)

# Concatena os dados horizontalmente (colunas diferentes, mesmas linhas)
df_final = pd.concat(dfs, axis=1)

# Filtrar por curso e região
df_final = df_final[
    (df_final["CO_GRUPO"] == 6411) & 
    (df_final["CO_REGIAO_CURSO"] == 4)
]

# Exibe amostra
print(df_final.head())

# Salva resultado
df_final.to_csv(os.path.join(caminho_diretorio, "base_final.csv"), index=False, sep=";")
