import plotly.express as px
from utils import df_rec_estado, df_rec_mensal, df_rec_categoria, \
    df_vendedores
#######################################################################
#Gráfico de mapa mostrando receita por estado.
grafico_map_estado = px.scatter_geo(
    df_rec_estado,
    lat = 'lat',
    lon = 'lon',
    scope = 'south america',
    size = 'Preço',
    template = 'seaborn',
    hover_name = 'Local da compra',
    hover_data = {'lat': False, 'lon': False},
    title = 'Receita por Estado'
)
#######################################################################
#Gráfico de linha mostrando a receita mensal.
#Nesse tipo de gráfico preciso de uma informação categórica('Mes')
    #que será o eixo X e uma informação numérica('Preço'), o eixo Y.
grafico_rec_mensal = px.line(
    df_rec_mensal,
    #Eixo X.
    x = 'Mes',
    #Eixo Y.
    y = 'Preço',
    #Inserindo marcadores
    markers = True,
    #Range no eixo Y de 0 até o máximo de meses, máximo de dados.
    range_y = (0, df_rec_mensal.max()),
    #O ano vem como a cor, como se fosse a legenda do gráfico.
    color = 'Ano',
    line_dash = 'Ano',
    #Título do Gráfico
    title = 'Receita Mensal'   
)
#Alterando, dando um nome, tirando do padrão, o nome do eixo Y.
grafico_rec_mensal.update_layout(yaxis_title = 'Receita')
#########################################################
#Gráfico em barras mostrando a receita por estado( os TOP 7).
grafico_rec_estado = px.bar(
    #head pega os primeiros registros e tail os últimos.
    df_rec_estado.head(7),
    #X é o local da compra, no caso, o estado.
    x = 'Local da compra',
    y = 'Preço',
    text_auto = True,
    #Título do Gráfico
    title = 'Top 7 Receita por Estados'
)
#######################################################################
grafico_rec_categoria = px.bar(
    df_rec_categoria.head(7),
    text_auto = True,
    title = 'Top 7 Categorias com Maior Receita'
)
#######################################################################
#Vendas Totais por vendedor
grafico_rec_vendedores = px.bar(
    #Selecionando os 7 primeiros vendedores.
    df_vendedores[['sum']].sort_values('sum', ascending=False).head(7),
    x = 'sum',
    y = df_vendedores[['sum']].sort_values('sum', ascending=False)\
        .head(7).index,
    text_auto = True,
    title = 'Top 7 Vendedores por Receita'
)
#######################################################################
grafico_vendas_vendedores = px.bar(
    df_vendedores[['count']].sort_values('count',ascending=False).\
        head(7),
    x = 'count',
    #Contagem de vendar por vendedor (top 7 vendedores).
    y = df_vendedores[['count']].sort_values('count',ascending=False).\
        head(7).index,
    text_auto = True,
    title = 'Top 7 Vendedores por Venda'
)
#######################################################################
