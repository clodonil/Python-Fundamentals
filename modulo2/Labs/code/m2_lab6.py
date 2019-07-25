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

# dep.orgaos_membros(id) retorna a lista de deputados de uma comissao
membros = dep.orgaos_membros('5973')


for comissao in membros:
    # Imprime o nome do deputado que participa da comissao
    print(comissao['nome'])
    