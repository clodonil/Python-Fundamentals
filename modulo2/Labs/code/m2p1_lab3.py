'''
classe: m2p1_lab3.py
descricao: Ordene a lista dos deputados por partido. Imprima o nome do deputado e o partido  em maiúscula
autor: Clodonil Honorio Trigo
email: clodonil@nisled.org
data: 18 de setembro de 2018
'''

from  lib.scrapy_dadosAbertos import DadosAbertos

listJson = DadosAbertos()

ldeputados = {}
for lista in listJson.deputados():
    nome    =  lista['nome']
    partido =  lista['siglaPartido']
    ldeputados[nome] = partido

for partido in sorted(ldeputados.values()):
    for nome in ldeputados:
        if partido == ldeputados[nome]:
            print("Nome: {0}, Partido: {1}".format(nome,partido))