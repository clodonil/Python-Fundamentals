Laboratório Práticas
--------------------

(https://pt.wikipedia.org/wiki/C%C3%A2mara_Municipal_de_S%C3%A3o_Paulo)[https://pt.wikipedia.org/wiki/C%C3%A2mara_Municipal_de_S%C3%A3o_Paulo)

![lista_vereadores_wikipedia](https://github.com/clodonil/curso_python/blob/master/Imagens/m1_lab1_f1.PNG)

Para obter os valores da lista dinamicamente, será utilizado a biblioteca Scrapy_table. Se uma página tiver mais de uma tabela, informe qual delas deseja obter. Por exemplo, no código abaixo queremos pegar a tabela de número 5  `tables = site_connect.get_tables(5)`.

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

Com essa informação, vamos responder as perguntas abaixo.desenvolvendo os códigos em Python.

Vamos utilizar os seguintes recursos da linguagem:
* Variável;
* String;
* List
* Set
* Tupla
* for
* if
* Operadores
* Dicionário

------

1. **Listar os 8 caracteres do nome do vereador para fazer o login de acesso aos sistemas:**

```Exemplo de resposta:
       Eduardo
       Milton L
       Reginald
       Conte Lo
       Mario Co
       Eduardo
        ...
```
> Codificação: [m1_lab1.py](code/m1_lab1.py)
	 
2. **Listar os partidos que tiveram candidatos eleitos:**
   
```Exemplo de Resposta:
         PDT
	 PSDB
	 ....
```
> Codificação: [m1_lab2.py](code/m1_lab2.py)

3. **Mostrar o somatória de todos os votos em vereadores:**
    
```Exemplo de Resposta: 2364.913'```
> Codificação: [m1_lab3.py](code/m1_lab3.py)

4. **Pesquisar se tem algum vereador vereador com os seguintes nomes (João, Eduardo, josé):**
```Exemplo de Resposta:
	    Eduardo Suplicy
		Eduardo Tuma
		João Jorge
		José Police Neto
```
> Codificação: [m1_lab4.py](code/m1_lab4.py)
	
5. **O partido que tive mais vereadores eleitos:**
   
```Resposta: 
        PSDB com 10 vereadores
```
> Codificação: [m1_lab5.py](code/m1_lab5.py)
6. **Numero total de votos por partidos:**
   Resposta: 
   
> Codificação: [m1_lab6.py](code/m1_lab6.py)

7. **Pesquisar se tem algum vereador está na lista de investigados na Lava Jato:**
 
> Codificação: [m1_lab7.py](code/m1_lab7.py)
