#Importando os dados do meu dataframe.
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
#Agrupando pela data e fazendo um somatório dos cooperados ativos.
df_tabela_media_cooperados = df.groupby("Datas")[["Coop. Ativos"]].sum()
#Eliminando registros duplicados e aplicando formatações.
df['Datas'] = df['Datas'].astype('int64') # Convertendo coluna datas para inteiro.
df['Coop. Ativos'] = df['Coop. Ativos'].astype('int64') # Convertendo coluna Coop. Ativos para inteiro.
df_tabela_media_cooperados = df.drop_duplicates(subset="Datas")[["Datas", "Coop. Ativos"]].merge(df_tabela_media_cooperados, left_on="Datas",right_on="Coop. Ativos").sort_values("Datas", ascending= True)


df_tabela_media_emprestimos = df.groupby("Datas")[["Emprestimo"]].sum()
#Eliminando registros duplicados e aplicando formatações.
df['Datas'] = df['Datas'].astype('int64') # Convertendo coluna datas para inteiro.
df['Emprestimo'] = df['Emprestimo'].astype('int64') # Convertendo coluna Emprestimo para inteiro.
df_tabela_media_emprestimos = df.drop_duplicates(subset="Datas")[["Datas", "Emprestimo"]].merge(df_tabela_media_emprestimos, left_on="Datas",right_on="Emprestimo").sort_values("Datas", ascending= True)

print(df_tabela_media_cooperados)
print(df_tabela_media_emprestimos)
