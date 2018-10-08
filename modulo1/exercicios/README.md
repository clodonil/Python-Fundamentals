Módulo 1 - Lista de Exercício
=========

Para realização desse exercício vamos utilizar a lista de municípios do Brasil, juntamente com a taxa de homicídio e a taxa de fecundidade. Vamos realizar o cruzamento dessas informações para obter respostas interessantes:

![lista_exercicio](https://github.com/clodonil/curso_python/blob/master/Imagens/m1_exercicio.JPG)

* https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Brasil_por_popula%C3%A7%C3%A3o
* https://pt.wikipedia.org/wiki/Lista_de_cidades_por_taxa_de_homic%C3%ADdios
* https://pt.wikipedia.org/wiki/Lista_de_unidades_federativas_do_Brasil_por_taxa_de_fecundidade

Para obter os valores da lista dinamicamente, será utilizado a biblioteca Scrapy_table. Se uma página tiver mais de uma tabela, informe qual delas deseja obter. Para obter as tabelas acima utilize o seguinte código:

```python
# importa a lib para obter as tabelas da Wikipedia
from  lib.scrapy_table import Scrapy_Table
# Variavel com o link da tabela
url="https://pt.wikipedia.org/wiki/C%C3%A2mara_Municipal_de_S%C3%A3o_Paulo"
# Inicia a class para obter a tabela
site_connect = Scrapy_Table(url)
# Pegando a tabela 5 (Vereadores em exercicio)
tables = site_connect.get_tables(5)
```

Um demo pode ser consultado [AQUI](https://github.com/clodonil/Python-Fundamentals/blob/master/modulo1/exercicios/code/m1_exercicio_demo.py).

Com essa informação, vamos responder as perguntas abaixo.desenvolvendo os códigos em Python.

> Questão de 1-5 serão consideradas para nota

1. **Listar o nome de todos os municípios do Brasil com o código do IBGE:**
__Exemplo de Resposta:__
```sh
  N IBGE  Municipio
--------------------
3550308	São Paulo
3304557	Rio de Janeiro	
5300108	Brasília	
2927408	Salvador
 ...      ....
 ```

2. **Listar os municípios com menos de 70.000 habitantes:**
   
3. **Mostrar o estado que tem o maior número de cidades acima 100.000 habitantes:**

4. **Qual município tem o menor número de habitantes. Mostre também em qual estado está esse município:**
	
5. **Mostre a taxa de fecundidade para os estados:**
     - **que tem a cidade com maior número de habitantes**
     - **que tem a cidade com menor número de habitantes**

> Questão 6 e 8 são para aprofundamento do conhecimento

```
6. Mostrar o total da população brasileira:

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
