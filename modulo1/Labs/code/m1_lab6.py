'''
classe: m1_lab6.py
descricao: Numero total de votos por partido
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
  
# Dicionario para armazenar partido e votos
# key = partidos
# values = votos
partidos =  {}

# Listando o conteudo da tabela
for linha in tables[1:]:

    # Obtendo o partido
    partido = linha[1]

    # Obtendo o voto do partido
    n_voto = float(linha[2].split(" ")[0])

    # se o partido esta no dicionario
    if partido in partidos:
       # Se tiver soma os votos
       partidos[partido] = partidos[partido] + n_voto
    else:
       # Se nao tiver inicializa o dicionario com o partido e o numero de votos
       partidos[partido] = n_voto
    
# Imprime os partidos e os votos
for partido in partidos:
    print(partido, 'teve',partidos[partido], 'votos.') 
