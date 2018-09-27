Laboratório do Módulo 2 (Parte1) 
======

# Como trabalhar
Vamos colocar em prática o que aprendemos sobre a linguagem Python. 

Esse laboratório propoe um problema e suas soluções. O aluno deve trabalhar como `code review`, isso é entender o código e fazer modificações construindo assim o seu conhecimento. 

> Ao final do laboratório proponha perguntas para você mesmo e tente responde-lás desenvolvendo o código em Python.


# Problema

No site 'dados abertos' da câmera de deputados federal (https://dadosabertos.camara.leg.br/) temos todas as informações de ações e gastos dos deputados federais.


![dadosabertos](https://github.com/clodonil/Python-Fundamentals/blob/master/Imagens/dados_abertos1.png)

Para obter os valores dinâmicamente, utilizaremos a biblioteca `Scrapy_DadosAbertos`. Mais a frente vamos entender como foi desenvolvida essa biblioteca, mais agora o importante é saber utiliza-lá.

A biblioteca retorna os dados da API do site dados abertos. 

```python
# importa a lib para conexão com o site Dados Abertos
from  lib.scrapy_dadosAbertos import DadosAbertos
# Inicia a class para obter os dados
site_connect = DadosAbertos()
# obtendo ajuda com os métodos disponíveis.
print(site_connect.help())
#Obtendo a lista de Deputados
list_dep = site_connect.deputados()
#Imprimindo a lista de deputados
print(list_dep)

```

Com essa informação, vamos responder as perguntas abaixo.desenvolvendo os códigos em Python.

Vamos utilizar os seguintes recursos da linguagem:
* Variável (String/Float);
* List
* Set
* Tuple
* for
* if
* Operadores
* Dicionário

------

1. **Imprima a quantidade de deputadores retornados na consulta**

> Codificação: [m2p1_lab1.py](code/m2p1_lab1.py)
	 
2. **Listar os dados dos deputados (id, Nome, DNasc, email, estado, partido):**
   
> Codificação: [m2p1_lab2.py](code/m2p1_lab2.py)

3. **Ordene a lista dos deputados por partido. Imprima o nome do deputado e o partido:**
    
> Codificação: [m2p1_lab3.py](code/m2p1_lab3.py)

4. **Lista as descrição e o valor das despesas de um deputado (pode ser qualquer um):**

> Codificação: [m2p1_lab4.py](code/m2p1_lab4.py)
	
5. **Lista os titulos em maiúsculo dos orgãos (comissão) do Congresso.:**
   
> Codificação: [m2p1_lab5.py](code/m2p1_lab5.py)
6. **Lista os deputados que participam da comissão que tem o ID 5973:**
   
> Codificação: [m2p1_lab6.py](code/m2p1_lab6.py)


***
> By:
```python
Autor   = ['Clodonil Honorio Trigo','clodonil@nisled.org']
linkdin = 'https://www.linkedin.com/in/clodonil-trigo-4155722a'
Blog    = 'http://www.devops-sys.com.br'
```
