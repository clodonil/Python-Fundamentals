'''
classe: m1_lab1.py
descricao: Listar os 8 caracteres do nome do vereador para fazer o login de acesso aos sistemas
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
  
# Listando o conteudo da tabela
for linha in tables[1:]:

     # Obtendo o nome. Esta na primeira posicao da lista
     nome = linha[0]

     # Imprimindo os caracteres da posicao 0 ate 8 
     print(nome[0:8])


     #Outras formas de fazer a mesma coisa
     #print(nome[:8])
 
     #Para retirar os espacos em branco de uma string
     #print(nome[:8].replace(' ',''))
