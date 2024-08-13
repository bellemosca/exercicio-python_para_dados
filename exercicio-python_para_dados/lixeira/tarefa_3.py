import pandas as pd

df = pd.read_csv("saude_do_sono_estilo_vida_modificado.csv")

# Porcentagem obesos em Engenheiros
eng_software = df[df["Profissão"] == "Eng. de Software"]
total_eng = eng_software.shape[0]

obesos_eng = eng_software[eng_software["Categoria BMI"] == "Obesidade"]

quantidade_obesos = obesos_eng.shape[0]

porcentagem = (quantidade_obesos / total_eng) * 100

print(f"{porcentagem:.0f}%")
