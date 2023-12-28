#Biblioteca de plotagem
import plotly.express as px
#Importa as fórmulas das tabelas para alimentar o gráfico.
from utils import df_tabela_soma_cooperados
from utils import df_tabela_soma_emprestimos

#Gráfico da soma dos cooperados
grafico_map_soma_cooperados = px.scatter_geo(
    df_tabela_soma_cooperados,
    custom_data = df_tabela_soma_cooperados,
    coop_ativos = "Coop. Ativos",
    scope = "south america",
    size = "Coop. Ativos",
    template = "seaborn",
    #Quando passar o mouse
    hover_name = "Coop. Ativos",
    hover_data = {"Datas": False, "Coop. Ativos": False},
    title = "Gráfico da Soma dos Cooperados"
)

#Gráfico da soma dos empréstimos
grafico_map_soma_emprestimos = px.scatter_geo(
    df_tabela_soma_emprestimos,
    custom_data = df_tabela_soma_emprestimos,
    coop_ativos = "Emprestimo",
    scope = "south america",
    size = "Emprestimo",
    template = "seaborn",
    #Quando passar o mouse
    hover_name = "Emprestimo",
    hover_data = {"Datas": False, "Emprestimo": False},
    title = "Gráfico da Soma dos Empréstimos"
)
