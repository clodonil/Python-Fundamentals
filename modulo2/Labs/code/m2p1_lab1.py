'''
classe: m2p1_lab1.py
descricao: Imprima a quantidade de deputadores retornados na consulta
autor: Clodonil Honorio Trigo
email: clodonil@nisled.org
data: 18 de setembro de 2018
'''

from  lib.scrapy_dadosAbertos import DadosAbertos

list_dep = DadosAbertos()

print("Numero de deputados:",len(list_dep.deputados()))