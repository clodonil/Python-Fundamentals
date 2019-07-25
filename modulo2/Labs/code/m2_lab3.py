'''
classe: m2_lab3.py
descricao: Lista dos deputados por partido. Imprima o nome do deputado e o partido 
autor: Clodonil Honorio Trigo
email: clodonil@nisled.org
data: 18 de setembro de 2018
'''
# Importa a class DadosAbertos do arquivo scrapy_dadosAbertos.py
from  scrapy_dadosAbertos import DadosAbertos

# Inicializa a classe DadosAbertos
dep = DadosAbertos()

# Cria um dicionario para ter o nome do deputado e o partido. ex: {'jose':'pt'}
ldeputados = {}

# dep.deputados() retorna a lista com informacoes gerais do deputados
lista_deputados = dep.deputados()

# For pega cada elemento da lista_deputados e passa para variavel deputado.
# A variavel deputado e um dicionario retornado pela API
for lista in lista_deputados:
    nome    =  lista['nome']
    partido =  lista['siglaPartido']

    # Imprimi o nome do deputado e e o partido
    print("Nome: {0}, Partido: {1}".format(nome,partido))