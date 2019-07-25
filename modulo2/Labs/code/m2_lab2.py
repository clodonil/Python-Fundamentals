'''
classe: m2_lab2.py
descricao: Listar os dados dos deputados (id, Nome, DNasc, email, estado, partido) 
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
    # atribui as variavel id e nome do deputado
    id   = deputado['id']
    nome = deputado['nome']

    # dep.deputado_id(id) retorna informacao detalhada do deputado e atribui na variavel infodep 
    infodep = dep.deputado_id(id)
    
    # cria uma mascara de string. No local {0},{1},{2}.. vai ser substituido na utilizacaoo do format
    mascara = "Id: {0}\n Nome: {1}\n Data de Nascimento: {2}\n Estado de Nascimento: {3}\n Email: {4}\n Sigla do Partido: {5}\n #-------------------------------------------------"

    # O format substitui o {0} pelo id, {2} pelo nome, e assim por diante
    print(mascara.format( 
                         id,
                         nome,
                         infodep['dataNascimento'],
                         infodep['ufNascimento'],
                         infodep['ultimoStatus']['gabinete']['email'],
                         infodep['ultimoStatus']['siglaPartido']
                         ))