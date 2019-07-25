'''
classe: m2p1_lab5.py
descricao: Lista os titulos em maiúsculo dos orgãos do Congresso.:
autor: Clodonil Honorio Trigo
email: clodonil@nisled.org
data: 18 de setembro de 2018
'''
# Importa a class DadosAbertos do arquivo scrapy_dadosAbertos.py
from  scrapy_dadosAbertos import DadosAbertos

# Inicializa a classe DadosAbertos
dep = DadosAbertos()

# dep.orgaos() retorna a lista com as comissoes
comissao = dep.orgaos()

# for para interar comissao por comissao
for org in comissao:
    id   = org['id']
    nome = org['nome']
    # imprime o id e o nome em maiusculo
    print(id,nome.upper())