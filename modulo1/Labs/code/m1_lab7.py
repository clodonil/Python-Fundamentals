'''
classe: m1_lab7.py
descricao: Pesquisar se tem algum vereador está na lista de investigados na Lava Jato 
autor: Clodonil Honorio Trigo
email: clodonil@nisled.org
data: 04 de julho de 2018
'''

# importa a lib para obter as tabelas da Wikipedia
from  lib.scrapy_table import Scrapy_Table


if __name__ == "__main__":
 
     # Variavel com o link da tabela
     url="https://pt.wikipedia.org/wiki/C%C3%A2mara_Municipal_de_S%C3%A3o_Paulo"
     url_jato="https://pt.wikipedia.org/wiki/Lista_de_pessoas_envolvidas_na_Opera%C3%A7%C3%A3o_Lava_Jato"

     # Inicia a class para obter a tabela
     site_vereadores = Scrapy_Table(url)
     site_jato       = Scrapy_Table(url_jato)

     # Pegando as tabelas
     vereadores      = tuple(site_vereadores.get_tables(5))
     lista_lava_jato = tuple(site_jato.get_tables(1))

     # Criar uma tuple com os nomes dos investigados
     lista_investigados = ()
     for investigados in  lista_lava_jato[1:]:
         lista_investigados = lista_investigados + (investigados[0],)

     # pesquisar nome por nome de vereador na lista de investigado
     for vereador in vereadores[1:]:
         # Verifica se o nome do vereador esta na lista de investigados
         if vereador[0] in lista_investigados:
            print(vereador)


     # Validacao 
     #vereador = "Aécio Neves"
     #if vereador in lista_investigados:
     #    print(vereador)

