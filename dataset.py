import json
from time import sleep
import pandas as pd

# Importar os dados da planilha Excel
df = pd.read_excel("/home/jadenilsonsilva/Documents/python/UAD_Posicao_Diaria.xlsx")

# Salvar os dados em formato JSON(transformar em json)
df.to_json("/home/jadenilsonsilva/Documents/python/UAD_Posicao_Diaria.json")

#Caminho onde estão os dados. Pode ser um banco de dados também.
file = open("/home/jadenilsonsilva/Documents/python/UAD_Posicao_Diaria.json")

#Carregamento do arquivo
data = json.load(file)

#Estrutura python que arremete muito ao json é a estrutura de diciónario.
#Estou criando um DataFrame baseado em dicionário e passo os dados (data)
# df é referência a DataFrame
df = pd.DataFrame.from_dict(data)

#imprime os dados carregados para ter certeza de que os estou acessando em formato tabular.
print(df)

#Fecha o arquivo, o acesso ao arquivo carregado.
file.close()