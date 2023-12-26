#FrameWork
import streamlit as st
#Biblioteca de plotagem
import plotly.express as px
#importar df do dataset.py, que é esse df o meu DataFrame já com a formatação da data, campos, coluna chamada "Datas" já formatada.
from dataset import df
#Possibilita adicionar um ícone personalizado no título do dashboard.
import requests
#importa do arquivo utils a função format_number
from utils import format_number

#Caminho da imagem personalizada
icon_url = "/home/jadenilsonsilva/Documents/python/pictures/Background_PGN.png"

#Deixa a tela um pouco mais larga, interessante para colocar gráficos lado a lado. Deve ser colocado antes do título.
st.set_page_config(layout="wide")

#Cria um dashboard com o título.
st.title("Dashboard da Posição Diária :shopping_trolley:")

#criar 4 habas. Chamo o streamlit tabs e passo uma lista, em formato de lista.
aba1, aba2, aba3, aba4, aba5, aba6, aba7 = st.tabs(["Geral","Datas","Coop. Ativos","Emprestimo","Depositos(Total)","Média Cooperados e Media de Emprestimos", 
    "Tabela da Média dos Cooperados e Media dos Emprestimos"])

#Aqui já mostra uma coluna da planilha por aba (aba1: "Geral(essa motra tudo)", aba2: "Datas", aba3: "Coop. Ativos", aba4: "Emprestimo", aba5: "Depositos(Total)", 
    #"Média Cooperados e Media de Emprestimos").
with aba1:
    st.dataframe(df)

with aba2:
    st.dataframe(df["Datas"])

with aba3:
    st.dataframe(df["Coop. Ativos"])

with aba4:
    st.dataframe(df["Emprestimo"])

with aba5:
    st.dataframe(df["Depositos (Total)"])

with aba6:
    #Crio um dashboard com 2 colunas
    coluna1, coluna2, coluna3 = st.columns(3)

    #Cálculo da quantidade registros existentes.
    with coluna1:
        total_registros = st.metric("Quantidade de dias contabilizados", df.shape[0], "dias")

    #Cálculo da média de cooperados ativos em um período de 19 dias, ou seja, a soma total dividida por 19.
    with coluna2:
        st.metric("Media de Coop. Ativos", format_number( ( df["Coop. Ativos"].sum() ) / df.shape[0] ), "R$" )

    #Cálculo da média de empréstimos concedidos em um período de 19 dias, ou seja, a soma total dividida por 19.
    with coluna3:
        st.metric("Media de Emprestimo", format_number( ( df["Emprestimo"].sum() ) / df.shape[0] ), "R$" )

with aba7:
    #Crio um dashboard com 3 colunas
    coluna1, coluna2, coluna3 = st.columns(3)

    #Cálculo da quantidade registros existentes coma função df.shape[0].
    with coluna1:
        total_registros = st.metric("Quantidade de dias contabilizados", df.shape[0], "dias")

    #Tabela com a média de cooperados ativos em um período de 19 dias, ou seja, a soma total de cooperados dividida por 19 dias.
    with coluna2:
        st.metric("Media de Coop. Ativos", format_number( ( df["Coop. Ativos"].sum() ) / df.shape[0] ), "R$" )

    #Tabela da média dos empréstimos concedidos em um período de 19 dias, ou seja, a soma total de todos os empréstimos dividida por 19 dias.
    with coluna3:
        st.metric("Media de Emprestimo", format_number( ( df["Emprestimo"].sum() ) / df.shape[0] ), "R$" )
