Módulo 1 - Lista de Exercício
=========

Para realização desse exercício vamos utilizar os dados do site 'dados abertos' da câmera de deputados federal (https://dadosabertos.camara.leg.br/) temos todas as informações de ações e gastos dos deputados federais. Vamos realizar o cruzamento dessas informações para obter respostas interessantes:


![dadosabertos](https://github.com/clodonil/Python-Fundamentals/blob/master/Imagens/dados_abertos1.png)

Para obter os valores dinâmicamente, utilizaremos a biblioteca `Scrapy_DadosAbertos`. Mais a frente vamos entender como foi desenvolvida essa biblioteca, mais agora o importante é saber utiliza-lá.

A biblioteca retorna os dados da API do site dados abertos. 

```python
# importa a lib para conexão com o site Dados Abertos
from  lib.scrapy_dadosAbertos import DadosAbertos
# Inicia a class para obter os dados
site_connect = DadosAberto()
# obtendo ajuda com os métodos disponíveis.
print(site_connect.help())
#Obtendo a lista de Deputados
list_dep = site_connect.deputados()
#Imprimindo a lista de deputados
print(list_dep)

```

Com essa informação, vamos responder as perguntas abaixo.desenvolvendo os códigos em Python.

> Questão de 1-5 serão consideradas para nota

1. **Listar os nomes em maúsculo dos deputados que tenham mais de 50 anos de idade:**

2. **Listar as deputadas:**
   
3. **Mostre a soma dos gastos de um deputados especificos:**

4. **Mostre o nome dos 3 deputados com maiores gastos:**
	
5. **Mostre as informações da comissão sobre 'PEC57402':**

> Questão 6 e 8 são para aprofundamento do conhecimento

```
6. Mostre os gastos mais comum dos deputados:

7. Quantos estados brasileiros estão abaixo da taxa de reposição populacional (2.10 filhos):

8. Quantos habitantes moram no sudeste (São Paulo, Minas Gerais, Rio de Janeiro, Espírito Santo):
```

> Questão 9 e 10 são desafios; só para os valentes, corajosos e fortes. Esqueça você não vai conseguir.

```
9. Mostrar o nome, número de habitantes e taxa de fecundidade para as cidades brasileiras que estão 
com taxa de homicídio acima de 60 por 100 Mil:

10. Quantos habitantes brasileiros estão morando nas 50 cidades mais violentas do mundo:
```
***
> By:
```python
Autor   = ['Clodonil Honorio Trigo','clodonil@nisled.org']
linkdin = 'https://www.linkedin.com/in/clodonil-trigo-4155722a'
Blog    = 'http://www.devops-sys.com.br'
```
