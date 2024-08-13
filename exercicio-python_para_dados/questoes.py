import pandas as pd
import numpy as np

# Carregar o arquivo CSV em um DataFrame
df = pd.read_csv("saude_do_sono_estilo_vida.csv")

# Questão 1: Renomear colunas
df = df.rename(
    columns={
        "ID": "Identificador",
        "Pressão sanguíneaaaa": "Pressão sanguínea",
        "Ocupação": "Profissão",
        "Categoria BMI": "Categoria IMC",
    }
)

# Questão 2: Média, moda e mediana de horas de sono para cada profissão
resultado_sono = df.groupby("Profissão")["Duração do sono"].agg(
    ["mean", "median", lambda x: x.mode()[0]]
)
resultado_sono.columns = ["Media", "Mediana", "Moda"]
print(resultado_sono)

# Questão 3: Porcentagem de obesos em Eng. de Software
eng_software = df[df["Profissão"] == "Eng. de Software"]
porcentagem_obesos_eng = (
    eng_software[eng_software["Categoria IMC"] == "Obesidade"].shape[0]
    / eng_software.shape[0]
) * 100
print(
    f"Porcentagem de obesos entre Engenheiros de Software: {porcentagem_obesos_eng:.0f}%"
)

# Questão 4: Advogados e Representantes de Vendas dormem menos?
dormem_menos = df[df["Profissão"].isin(["Advogado(a)", "Representante de Vendas"])]
media_sono = dormem_menos["Duração do sono"].mean()
print(
    f"Média de horas de sono para Advogados e Representantes de Vendas: {media_sono:.2f} horas"
)

# Questão 5: Enfermagem vs Medicina, quem dorme menos?
enf_vs_med = df[df["Profissão"].isin(["Enfermeiro(a)", "Médico(a)"])]
media_sono_enf = enf_vs_med[enf_vs_med["Profissão"] == "Enfermeiro(a)"][
    "Duração do sono"
].mean()
media_sono_med = enf_vs_med[enf_vs_med["Profissão"] == "Médico(a)"][
    "Duração do sono"
].mean()

if media_sono_enf < media_sono_med:
    print(f"Enfermeiros(as) dormem menos: {media_sono_enf:.2f} horas em média")
else:
    print(f"Médicos(as) dormem menos: {media_sono_med:.2f} horas em média")

# Questão 6: Subconjunto com Identificador, Gênero, Idade, Pressão sanguínea e Frequência cardíaca
subconjunto = df[
    ["Identificador", "Gênero", "Idade", "Pressão sanguínea", "Frequência cardíaca"]
]
print(subconjunto.head())

# Questão 7: Profissão menos frequente
profissao_menos_frequente = df["Profissão"].value_counts().idxmin()
print(f"Profissão menos frequente: {profissao_menos_frequente}")

# Questão 8: Maior pressão sanguínea média por gênero
df[["Sistolica", "Diastolica"]] = (
    df["Pressão sanguínea"].str.split("/", expand=True).astype(int)
)

media_pressao_genero = (
    df.groupby("Gênero")[["Sistolica", "Diastolica"]].mean().mean(axis=1)
)
genero_maior_pressao = media_pressao_genero.idxmax()
print(f"Gênero com maior pressão sanguínea média: {genero_maior_pressao}")

# Questão 9: Predominância de 8 horas de sono por dia
moda_sono = df["Duração do sono"].mode()[0]
print(f"Moda das horas de sono: {moda_sono} horas")

# Questão 10: Frequência cardíaca e passos diários
media_passos_alta_fc = df[df["Frequência cardíaca"] > 70]["Passos diários"].mean()
media_passos_baixa_fc = df[df["Frequência cardíaca"] <= 70]["Passos diários"].mean()

if media_passos_alta_fc > media_passos_baixa_fc:
    print(
        f"Pessoas com frequência cardíaca acima de 70 dão mais passos: {media_passos_alta_fc:.0f} passos em média"
    )
else:
    print(
        f"Pessoas com frequência cardíaca abaixo ou igual a 70 dão mais passos: {media_passos_baixa_fc:.0f} passos em média"
    )

# Salvar o arquivo CSV modificado com codificação UTF-8 e BOM
df.to_csv("saude_do_sono_estilo_vida_modificado.csv", index=False, encoding="utf-8-sig")
