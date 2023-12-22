import streamlit as st
import plotly.express as px
#importar df do dataset.py, que é esse df o meu DataFrame já com a formatação da data, campos, coluna chamada "Datas" já formatada.
from dataset import df
#Possibilita adicionar um ícone personalizado no título do dashboard.
import requests
import locale

#Caminho da imagem personalizada
icon_url = "/home/jadenilsonsilva/Documents/python/pictures/Background_PGN.png"

#Deixa a tela um pouco mais larga, interessante para colocar gráficos lado a lado. Deve ser colocado antes do título.
st.set_page_config(layout="wide")

#Cria um dashboard com o título.
st.title("Dashboard da Posição Diária :shopping_trolley:")

#criar 4 habas. Chamo o streamlit tabs e passo uma lista, em formato de lista.
aba1, aba2, aba3, aba4, aba5, aba6 = st.tabs(["Geral","Datas","Coop. Ativos","Emprestimo","Depositos(Total)","Média Cooperados e Media de Emprestimos"])

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
        total_registros = st.metric("Quantidade de dias contabilizados", df.shape[0])

    #Cálculo da média de cooperados ativos em um período de 19 dias, ou seja, a soma total dividida por 19.
    with coluna2:
        metrica = st.metric("Media de Coop. Ativos", (df["Coop. Ativos"].sum())/df.shape[0])

    #Cálculo da média de empréstimos concedidos em um período de 19 dias, ou seja, a soma total dividida por 19.
    with coluna3:
        st.metric("Media de Emprestimo", (df["Emprestimo"].sum())/df.shape[0])