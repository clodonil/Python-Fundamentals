# importa a lib para conexão com o site Dados Abertos
from scrapy_dadosAbertos import DadosAbertos
# Inicia a class para obter os dados
site_connect = DadosAbertos()
# obtendo ajuda com os métodos disponíveis.
print(site_connect.help())
#Obtendo a lista de Deputados
list_dep = site_connect.deputados()
#Imprimindo a lista de deputados
print(list_dep)
