#Importando os dados do meu dataframe.
import datetime
from heapq import nsmallest as ns
import numpy as np
from pandas import Series
from dataset import df

#Função para formatar números
def format_number(value, prefix = ""):
    #Vai varrer os dados de vazio até mil e verificar o value
    for unit in ["", "1000"]:
        if value < 1000:
            #Retorna uma f string. value formatado em 2 casas decimais.
            return f"{prefix} {value:.2f} {unit}"
        
        elif value < 1000000:
            #Retorna uma f string. value formatado em 2 casas decimais.
            return f"{prefix} {value:.2f} {unit} mil"
        
        value /= 1000
        #Retorna uma f string. value formatado em 2 casas decimais.
        return f"{prefix} {value:.2f} milhões"
#####################################################################################################################
#Agrupando pela data.
df_tabela_soma_cooperados = df.groupby("Datas")[["Coop. Ativos"]].sum()
df_tabela_soma_cooperados = df.drop_duplicates(subset="Datas")[["Datas","Coop. Ativos"]].merge(df_tabela_soma_cooperados, left_on="Datas", right_index=True).sort_values("Datas", ascending=True)



#Agrupando pela data.
df_tabela_soma_emprestimos = df.groupby("Datas")[["Emprestimo"]].sum()
df_tabela_soma_emprestimos = df.drop_duplicates(subset="Datas")[["Datas","Emprestimo"]].merge(df_tabela_soma_emprestimos, left_on="Datas", right_index=True).sort_values("Datas", ascending=True)

print(f"",df_tabela_soma_cooperados,"\n")

print(df_tabela_soma_emprestimos)
