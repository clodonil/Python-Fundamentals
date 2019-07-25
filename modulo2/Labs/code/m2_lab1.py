'''
classe: m2p1_lab1.py
descricao: Imprima a quantidade de deputadores retornados na consulta
autor: Clodonil Honorio Trigo
email: clodonil@nisled.org
data: 18 de setembro de 2018
'''

# Importa a class DadosAbertos do arquivo scrapy_dadosAbertos.py
from  scrapy_dadosAbertos import DadosAbertos

# Inicializa a classe DadosAbertos
dep = DadosAbertos()

# dep.deputados() retorna a lista com informacoes gerais do deputados
lista_deputados = dep.deputados()

# For pega cada elemento da lista_deputados e passa para variavel deputado.
# A variavel deputado e um dicionario retornado pela API
for deputado in lista_deputados:    
    # Acesso a key nome do dicionario deputado
    print('Nome:', deputado['nome'])

# A funcao len() retorna o total de registro na lista_deputados 
print("Numero total de deputados:",len(lista_deputados))