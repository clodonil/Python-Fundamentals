Laboratório do Módulo 3 
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
* Salvar dados em JSON;
* Salvar dados em arquivos texto;
* Salvar dados em CSV;
* Manipulando datas;
* Criando banco de dados;

------

1. **Salve em um arquivo texto os nomes dos deputados**

> Codificação: [m3_lab1.py](code/m3_lab1.py)
	 
2. **Exporte para CSV os dados de gastos de pelo menos 5 deputados. Faça um arquivo para cada deputado):**
   
> Codificação: [m3_lab2.py](code/m3_lab2.py)

3. **Exporte no formato json os dados cadastraes dos deputados:**
    
> Codificação: [m3lab3.py](code/m3_lab3.py)

4. **Lista as descrição e o valor das despesas de um deputado (pode ser qualquer um):**

> Codificação: [m3_lab4.py](code/m3_lab4.py)
	
5. **Lista os titulos em maiúsculo dos orgãos (comissão) do Congresso.:**
   
> Codificação: [m3_lab5.py](code/m2p1_lab5.py)
6. **Lista os deputados que participam da comissão que tem o ID 5973:**
   
> Codificação: [m3_lab6.py](code/m2p1_lab6.py)


***
> By:
```python
Autor   = ['Clodonil Honorio Trigo','clodonil@nisled.org']
linkdin = 'https://www.linkedin.com/in/clodonil-trigo-4155722a'
Blog    = 'http://www.devops-sys.com.br'
```
