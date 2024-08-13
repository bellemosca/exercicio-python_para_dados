import pandas as pd

df = pd.read_csv("saude_do_sono_estilo_vida_modificado.csv")

profissoes = df.groupby("Profissão")

# Calcular a média, mediana e moda
mediana = profissoes["Duração do sono"].median()
media = profissoes["Duração do sono"].mean()
moda = profissoes["Duração do sono"].apply(lambda x: x.value_counts().idxmax())

resultado = pd.DataFrame({"Mediana": mediana, "Media": media, "Moda": moda})

print(resultado)
