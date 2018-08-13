'''
classe: m1_lab4py
descricao: Pesquisar se tem algum vereador vereador com os seguintes nomes (José, Eduardo, João
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
  
#Variavél para somatória de votos
total = 0 

for linha in tables[1:]:

    # Obtendo o numo de votos do cantidato
    nome = linha[0]

    # Separando o nome e sobrenome e tornando uma lista
    # [ 'Eduardo', 'Suplicy' ]
    l_nome  = nome.split(" ")
          
    # Compara se jose é igual ao primeiro nome da lista. Lower muda a string para minuscula
    if 'josé' == l_nome[0].lower():
        print(nome)
          
    if 'eduardo' == l_nome[0].lower():
        print(nome)

    if 'joão' == l_nome[0].lower():
        print(nome)


    # Podems escrever essa parte do código dessa forma:
    # if 'josé' == l_nome[0].lower() or  'eduardo' == l_nome[0].lower() or  'joão' == l_nome[0].lower():
    #   print(nome)


    # Também podems escrever essa parte do código dessa forma:
    # if l_nome[0].lower() in [ 'josé', 'eduardo','joão']:
    #     print(nome)
          
