# Python para Dados - Desafio Final

Considerando a base de dados de saude_do_sono_estilo_vida.csv responda
as questões abaixo.
Você é uma pesquisadora que está tentando entender melhor qual o impacto
do estilo de vida de uma pessoa na sua qualidade de sono, por isso fez a
coleta dos dados de sobre 373 pessoas, onde foram recolhidas 12
características para cada uma delas. Por competência a sua pesquisa foi bem
controlada e você não tem dados faltosos na sua base. Chegou o momento
de você fazer sua análise e responder algumas perguntas.


### 1. 
Ao visualizar a base você percebeu que seria melhor alterar o nome de
algumas colunas. Mude o ‘ID’ para ‘Identificador’, corrija o nome da
coluna que indica a pressão sanguínea, mude a coluna ‘Ocupação’ para
‘Profissão’, a coluna ‘Categoria BMI’ está em parte em inglês, substitua
para ‘Categoria IMC’.
### 2. 
Qual é a média, a moda e a mediana de horas de sono para cada uma
das profissões? [‘mean’, np.median, pd.Series.mod]
### 3. 
Das pessoas que atuam com engenharia de software qual a
porcentagem de obesos?
### 4. 
De acordo com os dados, advogar ou ser representante de vendas faz
você dormir menos? (Use o método ‘isin’, considere a média)
### 5. 
Entre quem fez enfermagem e quem fez medicina, quem tem menos
horas de sono? (Use o método ‘isin’, considere a média)
### 6. 
Faça um subconjunto com as colunas Identificador, Gênero, Idade,
Pressão sanguínea e Frequência cardíaca.
### 7. 
Descubra qual a profissão menos frequente no conjunto. (Use
value_counts)
### 8. 
Quem tem maior pressão sanguínea média, homens ou mulheres?
(Considere a média)
### 9. 
É predominante entre os participantes dormir 8 horas por dia
(considere usar Moda como medida)?
### 10. 
Pessoas com frequências cardíacas acima de 70 dão mais passos que
pessoas com frequência cardíaca menor ou igual a 70? (Use a média)
