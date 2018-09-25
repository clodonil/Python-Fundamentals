'''
classe: m2p1_lab1.py
descricao: Listar os dados dos deputados (id, Nome, DNasc, email, estado, partido) 
autor: Clodonil Honorio Trigo
email: clodonil@nisled.org
data: 18 de setembro de 2018
'''

from  lib.scrapy_dadosAbertos import DadosAbertos

list_dep = DadosAbertos()

print(list_dep.help())