Laboratório do Módulo 3
======

# Como trabalhar
Vamos colocar em prática o que aprendemos sobre a linguagem Python e seus paradigmas. 

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
> Antes de executar o exercício, instale as dependências do arquivo [requirements.txt](code/requirements.txt)
Com essa informação, vamos responder as perguntas abaixo.desenvolvendo os códigos em Python.

```python
$ pip install -r requirements.txt
```

Vamos utilizar os seguintes recursos da linguagem:
* Variável (String/Float);
* List
* Set
* Tuple
* for
* if
* Operadores
* Dicionário
* Funções
* Classes

------

1. **Crie uma função para retornar a quantidade de letras do nome do deputado**

> Codificação: [m3_lab1.py](code/m3_lab1.py)

**Sugestão de alteração:**
- Crie uma função para retornar o nome do deputador formatado; 
- Crie uma função para retornar o sobrenome do deputado;
- Crie uma função para retornar True se o deputado for do partido PSDB, todos os outros retorna False;


2. **Crie uma função para retornar uma lista com  os dados do deputados (id, Nome, DNasc, email, estado, partido):**
   
> Codificação: [m2_lab2.py](code/m3_lab2.py)

**Sugestão de alteração:**
- Adicione o campo escolaridade do deputado;
- Liste os deputados que tem ensino superior;
- Liste a escolaridade e o número de deputado que tem essa escolaridade ex: Superior 10, Mestrado 20; 

3. **Crie uma função, que dado o partido, retorna a lista de deputados:**
    
> Codificação: [m2_lab3.py](code/m3_lab3.py)

**Sugestão de alteração:**
- Imprima a lista ordenado por partido;
- Imprima apenas os deputados do PT e PSDB;
- Imprima a quantidade de deputados do PSL; 

4. **Crie uma função que retorna os gastos que são recorrentes a cada mês de cada deputado:**

> Codificação: [m2_lab4.py](code/m3_lab4.py)

**Sugestão de alteração:**
- Imprima a soma dos gastos do deputado;
- Formate o texto do gasto do deputado com o método title;
- Imprima também o nome do fornecedor; 

5. **Crie uma função que retorna o deputado que tem os gastos acima de um valor definido:**
   
> Codificação: [m2_lab5.py](code/m3_lab5.py)

**Sugestão de alteração:**
- Formate a saida do print, para uma melhor representação;
- Formate o titulo da comissão, imprimindo no máximo 30 caracteres;
- Imprima o total de comissão; 


6. **Lista os deputados que participam da comissão que tem o ID 5973:**
   
> Codificação: [m2_lab6.py](code/m3_lab6.py)

**Sugestão de alteração:**
- Imprima o partido que tem mais representante na comissão;
- Imprima o nome do deputado em maisculo;
- Imprima a quantidade de deputados que estão na comissão; 


***
> By:
```python
Autor   = ['Clodonil Honorio Trigo','clodonil@nisled.org']
linkdin = 'https://www.linkedin.com/in/clodonil-trigo-4155722a'
Blog    = 'http://www.devops-sys.com.br'
```
