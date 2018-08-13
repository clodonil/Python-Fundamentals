'''
classe: m1_lab5.py
descricao: Partido com mais vereadores eleitos 
autor: Clodonil Honorio Trigo
email: clodonil@nisled.org
data: 04 de julho de 2018
'''

# importa a lib para obter as tabelas da Wikipedia
from  lib.scrapy_table import Scrapy_Table

# Variavel com o link da tabela
url="https://pt.wikipedia.org/wiki/C%C3%A2mara_Municipal_de_S%C3%A3o_Paulo"

# Inicia a class para obter a tabela
site_connect = Scrapy_Table(url)

# Pegando a tabela 5 (Vereadores em exercicio)
tables = site_connect.get_tables(5)
  
# Dicionario para guardar o partido e numero de vereadores eleitos
# key   = nome do Partido
# Valor = Numero de vereadores eleitos
partidos = { }
     
# Listando o conteudo da tabela
for linha in tables[1:]:

    # Obtendo o partido
    partido = linha[1]

    # Verifica se o partido ja esta no dicionario
    if partido in partidos:
       # Se tiver, soma +1 no valor daquele partido
       partidos[partido] += 1
    else:
       # Se não tiver, inicializa o partido com 1
       partidos[partido] = 1

#Agora temos o dicionario com a seguinte estrutura:
# {'PT': 9, 'DEM': 5, 'PV': 2, 'PP': 1, 'PSDB': 10, 'PTB': 2, 'PRB': 4, 'PMDB': 2, 'PR': 4, 'PSD': 4, 'PSB': 3, 'PPS': 2, 'PSC': 1, 'PROS': 1, 'PODE': 1, 'NOVO': 1, 'PSOL': 2, 'PHS': 1}

# Precisamos pegar o maior

# Variabel para controlar o numero de vereadores e o nome do partido 
num_vereadores = 0
nome_partido   = 0

# Varre toda o dicionário
for part in partidos:
    # Verica se o numero de vereadores é maior que num_vereadores 
    if partidos[part] > num_vereadores:
        # Se for maior, armazenar o numero de vereadores e o nome do partido
        nome_partido   = part
        num_vereadores =  partidos[part] 
            
print(nome_partido,'com',num_vereadores,'vereadores') 
