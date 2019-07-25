'''
classe: m2_lab4.py
descricao: Lista as descrição e o valor das despesas de um deputado (pode ser qualquer um)
autor: Clodonil Honorio Trigo
email: clodonil@nisled.org
data: 18 de setembro de 2018
'''
# Importa a class DadosAbertos do arquivo scrapy_dadosAbertos.py
from  scrapy_dadosAbertos import DadosAbertos

# Inicializa a classe DadosAbertos
dep = DadosAbertos()

# dep.deputado_id() retorna a lista detalhada do deputado
deputado = dep.deputado_id('73437')

# recupera o nome do deputado
nome = deputado['nomeCivil']

# dep.deputado_despesas(id) retorna a lista com as despesas do deputado
despesas = dep.deputado_despesas('73437')

#Interecao para mostrar despesa a despesa
for despesa in despesas:
    # imprime os gastos
    print("Deputado: {0}, Gasto:{1}, Data:{2}/{3}, Valor: R$ {4}".format(nome,despesa['tipoDespesa'],despesa['mes'],despesa['ano'],despesa['valorDocumento']))
