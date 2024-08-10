import pandas as pd

df = pd.read_csv("saude_do_sono_estilo_vida.csv")

# Agrupar por ...
profissoes = df.groupby("Ocupação")

# Calcular a media, mediana e moda
mediana = profissoes["Duração do sono"].median()
media = profissoes["Duração do sono"].mean()
moda = profissoes["Duração do sono"].apply(lambda x: x.value_counts().idxmax())

#Porcentagem obesos em Engenheiros
eng_software = df[df['Ocupação'] == 'Eng. de Software']
total_engenheiros = eng_software.shape[0]


# Exibir resultados
resultado = pd.DataFrame({"Mediana": mediana, "Media": media, "Moda": moda})

print(resultado)
