import pandas as pd

# Especificar o nome do arquivo CSV
arquivo_csv = "saude_do_sono_estilo_vida.csv"

# Carregar o arquivo CSV em um DataFrame
df = pd.read_csv(arquivo_csv)

# Substituir "Peso Normal" por "Normal" na coluna "Categoria BMI"
df["Categoria BMI"] = df["Categoria BMI"].replace("Peso normal", "Normal")

# Renomear as colunas "ID" para "Identificador" e "Ocupação" para "Profissão"
df = df.rename(columns={"ID": "Identificador", "Ocupação": "Profissão"})

# Salvar o arquivo CSV modificado
df.to_csv("saude_do_sono_estilo_vida_modificado.csv", index=False)

print("Substituições concluídas e arquivo salvo como 'arquivo_modificado.csv'.")
