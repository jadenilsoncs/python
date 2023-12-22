import json
from time import sleep
import pandas as pd

# Importar os dados da planilha Excel
df = pd.read_excel("/home/jadenilsonsilva/Documents/python/UAD_Posicao_Diaria.xlsx")

# Salvar os dados em formato JSON(transformar em json)
df.to_json("/home/jadenilsonsilva/Documents/python/UAD_Posicao_Diaria.json")

#Caminho onde estão os dados, agora em formato json. Pode ser um banco de dados também. Estou abrindo o arquivo.
file = open("/home/jadenilsonsilva/Documents/python/UAD_Posicao_Diaria.json")

#Carregamento do arquivo json
data = json.load(file)

#Estrutura python que arremete muito ao json é a estrutura de diciónario. Estou criando um DataFrame baseado em dicionário e passo os dados (data)
# df é referência a DataFrame
df = pd.DataFrame.from_dict(data)

#imprime os dados carregados para ter certeza de que os estou acessando. E imprime agora já em formato tabular.
#Formatando a data no formato dia/mês/ano.
df["Datas"] = pd.to_datetime(df["Datas"], format="%d/%m/%Y")

#Fecha o arquivo, o acesso ao arquivo carregado.
file.close()