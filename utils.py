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
    
##################################################################################
