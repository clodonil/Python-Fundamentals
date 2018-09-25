'''
classe: m2p1_lab1.py
descricao: Listar os dados dos deputados (id, Nome, DNasc, email, estado, partido) 
autor: Clodonil Honorio Trigo
email: clodonil@nisled.org
data: 18 de setembro de 2018
'''

from  lib.scrapy_dadosAbertos import DadosAbertos

list_dep = DadosAbertos()

for dep in list_dep.deputados():    
    id   = dep['id']
    nome = dep['nome']

    infodep = list_dep.deputado_id(id)
    
    mascara = "Id: {0}\n Nome: {1}\n Data de Nascimento: {2}\n Estado de Nascimento: {3}\n Email: {4}\n Sigla do Partido: {5}\n #-------------------------------------------------"

    print(mascara.format( 
                         id,
                         nome,
                         infodep['dataNascimento'],
                         infodep['ufNascimento'],
                         infodep['ultimoStatus']['gabinete']['email'],
                         infodep['ultimoStatus']['siglaPartido']
                         ))