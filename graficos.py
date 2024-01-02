#Biblioteca de plotagem
import pandas as pd
import plotly.express as px
#Importa as fórmulas das tabelas para alimentar o gráfico.
from utils import df_tabela_soma_cooperados
from utils import df_tabela_soma_emprestimos
from dataset import df

#Gráfico da soma dos cooperados
grafico_map_soma_cooperados = px.scatter_matrix(
    df_tabela_soma_cooperados,
    #lat = "Coop. Ativos",
    #lon= "Coop. Ativos",
    #scope = "south america",
    size = "Coop. Ativos",
    template = "seaborn",
    #Quando passar o mouse
    hover_name ="Coop. Ativos",
    hover_data = {"Coop. Ativos": False},
    title = "Gráfico da Soma dos Cooperados"
)

#Gráfico da soma dos empréstimos
grafico_map_soma_emprestimos = px.scatter_matrix(
    df_tabela_soma_emprestimos,
    #lat = "Emprestimo",
    #lon= "Emprestimo",
    #scope = "south america",
    size = "Emprestimo",
    template = "seaborn",
    #Quando passar o mouse
    hover_name = "Emprestimo",
    hover_data = {"Emprestimo": False},
    title = "Gráfico da Soma dos Empréstimos"
)
