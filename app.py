import streamlit as st
import plotly.express as px
#importar df do dataset.py, que é esse df o meu DataFrame já com a formatação da data, campos, coluna chamada "Datas" já formatada.
from dataset import df
#Possibilita adicionar um ícone personalizado no título do dashboard.
import requests

#Caminho da imagem personalizada
icon_url = "/home/jadenilsonsilva/Documents/python/pictures/Background_PGN.png"

#Deixa a tela um pouco mais larga, interessante para colocar gráficos lado a lado. Deve ser colocado antes do título.
st.set_page_config(layout="wide")

#Cria um dashboard com o título.
st.title("Dashboard da Posição Diária :shopping_trolley:")