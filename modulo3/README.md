   
### Módulo 3


 __Python Fundamentals__ - Módulo 3
 ====================== 
 
## Objetivo
Neste módulo vamos desenvolver habilidade de persistir os dados tanto por aquivos como banco de dados.

## Conteúdo:
> 1. [Date e Time](#1-date-e-time)
> 2. [Trabalhando com Arquivos](#2-trabalhando-com-Arquivos)
> 3. [JSON e CSV](#3-JSON-CSV)
> 4. [Banco de Dados](#4-Banco-de-Dados)
> 5. [Modulos e Package](#6-Modulos-e-Package)
> 6. [Laboratório](#10-laboratório)
> 7. [Lista de Exercício](#11-lista-de-exercício)

## 1 Date e Time
Um dos recursos frequentemente utilizado no dia-a-dia e também no desenvolvimento de software, é a manipulação de datas.

Para manipulação de data e hora, vamos um módulo interno do Python `datetime`. Com esse módulo podemos de forma simples manipular dados relacionando a data e hora.

O exemplo abaixo, retorno a data atual do sistema.

```python
import datetime
now = datetime.datetime.now()
print(now)  #2018-11-20 01:27:10.903625
```
Para formatar a impressão da data com as informações necessárias, podemos utilizar o método `strftime`.

```python
import datetime

now = datetime.datetime.now())
print(now.strftime("%d/%m/%y")) # (07/11/18)

```
Com o método strtime, podemos formatar uma data com as informações que precisamos. 																													
Os parâmetros que podemos utilizar no strftime são:

|Parâmetros |	Descriçao	|Exemplo|
|---------|---------|--------|
| %a	  |Apreviação do dia da semana. | Sun, Mon, …, Sat |
| %A	  |Nome completo do dia da semana. | Sunday, Monday, …, Saturday |
| %w	|Dia da semana em numeral, sendo 0 para domingo e 6 para sábado.|	0, 1, …, 6	| 
| %d	|Dia do mês em numeral.|	01, 02, …, 31|	 
| %b	|Nome do mês abreviado.|Jan, Feb, …, Dec |
|%B	|Nome do mês completo.|January, February, …, December|
|%m	|Mês em númeral.|	01, 02, …, 12|	 
|%y	|Ano com 2 casas decimal.|	00, 01, …, 99|	 
|%Y	|Ano com 4 casas decimal.|	1970, 1988, 2001, 2013	 |
|%H	|Hora (24-hora ).|	00, 01, …, 23|	 
|%I	|Hora (12-hora ).|	01, 02, …, 12|	 
|%p	|AM ou PM.|AM, PM |
|%M	|Minuto.|	00, 01, …, 59|	 
|%S	|Segundos.|	00, 01, …, 59|
|%f	|Microsegundos.|	000000, 000001, …, 999999	|
|%%	|Escape do %.|	%	| 

O comando `import datetime` importa o módulo inteiro de date e hora, entretando muitas vezes é necessário apenas a trabalhar com `date`, não sendo necessário importar a classe `time`.

```python

from datetime import date

agora = date.today()

print(agora.day)
print(agora.month)
print(agora.year)
```

Também podemos converter uma string em `datetime`.

```python

from datetime import datetime

data_e_hora_em_texto = '01/03/2018 12:30'
data_e_hora = datetime.strptime(data_em_texto, ‘%d/%m/%Y %H:%M’)

```

Além da formatação de datas, podemos realizar as operações básicas tais como "maior (>)", "menor (<)","igual (=)". Também somar, subtrair. 

Um exemplo dessas operações:

```python
import datetime
#data atual
now = datetime.datetime.now()
# data nascimento
nasc = datetime.datetime.strptime('01/03/2018 12:30', '%d/%m/%Y %H:%M')
print ( now - nasc)  # 263 days, 13:30:19.341628 
print ( now > nasc)  # True
```
### Timedelta

A classe timedelta também é bastante útil na manipulação das datas. Com ela podemos movimentar as datas em semanas (`weeks`), dias (`days`), horas (`hours`), minutos (`minutes`) ou segundos (`seconds`).

**Exemplo1:**

Vamos somar duas semanas em um data especifica.

```python
import datetime
data = datetime.datetime.strptime('01/03/2018 12:30', '%d/%m/%Y %H:%M')
print(data)
data += datetime.timedelta(weeks=2)
print(data)
```

**Exemplo2:**

Vamos subtrair 100 dias de um data especifica.

```python
import datetime
data = datetime.datetime.strptime('01/03/2018 12:30', '%d/%m/%Y %H:%M')
print(data)
data -= datetime.timedelta(days=2)
print(data)
```


## 2 Trabalhando com Arquivos
Podemos tornar os nossos programas muito mais interessante quando podemos gravar e ler conteúdo de arquivos.
No Python podemos utilizar a função `open()` para ler o conteúdo de um arquivo e também para escrever nesse arquivo.

Para o código abaixo, crie um arquivo chamado `file.txt` e escreva um conteúdo. O programa vai ler o conteudo do arquivo e imprimir na tela.

```python
#abrir o arquivo
farq = open('file.txt')
#Lendo todo o conteúdo do arquivo
conteudo = farq.readlines()
#Fechando o arquivo
farq.close()
#Imprimindo o conteúdo do arquivo
print(conteudo)

```
Nesse caso o arquivo `file.txt` está no mesmo diretório do código em python, caso esteja em outro diretório é necessário colocar o diretório completo.

A função `open()` tem a seguinte sintaxe:

* open("filename", "mode"): O filename é o nome do arquivo que será tratado e o mode, é a forma que vamos trabalhar com o arquivo. 

** 'r' - Abre o arquivo apenas para leitura; 
** 'w' - Cria o arquivo para escrita, se o arquivo existir um arquivo com o mesmo nome, será deletado. 
** 'a' - Abre o arquivo para escrita e adiciona o conteúdo no final do arquivo. 
** 'r+' - Modo especial de leitura e gravação, usado para lidar com as duas ações ao trabalhar com um arquivo.

Se nenhuma opção for declarado no mode, por padrão vai ser `r`.

* readlines() : A função readlines retorna todas as linhas em forma de lista, sendo uma linha em casa posição.
* read() : Retorna todo o conteúdo de um texto;
* write() : Escreve uma stringo no arquivo.

Para finalizar, vamos escrever um arquivo.

```python
#linha
linha = "Primeira linha do arquivo"
fconf = open('file2.txt','w')
fconf.write(linha)
fconf.close()
```

## 3 JSON e CSV

## 4 Banco de Dados

```python
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import mapper, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///data.db')
Base = declarative_base(engine)
metadata = Base.metadata
Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
	__tablename__ = "users"
	id = Column(Integer, primary_key=True)
	nome = Column(String(255), nullable=False)
	idade = Column(Integer, nullable=False)
Base.metadata.create_all(bind=engine)
session.commit()
p = session.query(PollList).filter(PollList.id == None)
print(type(p)) 
```

## 5 Modulos e Package

## 6 Laboratório
No link abaixo temos o laboratório dirigido, faça o laboratório para praticar os conhecimentos apreendidos
> [Laboratório](https://github.com/clodonil/curso_python/tree/master/modulo1/Labs)

## 7 Lista de Exercício
Após realizar o laboratório e brincar com os códigos, teste o seu conhecimento com a lista de exercícios:
> [Lista de Exercícios](exercicios/README.md)

***
> By:
```python
Autor   = ['Clodonil Honorio Trigo','clodonil@nisled.org']
linkdin = 'https://www.linkedin.com/in/clodonil-trigo-4155722a'
Blog    = 'http://www.devops-sys.com.br'
```
