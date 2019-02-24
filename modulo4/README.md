   
### Módulo 4


 __Python Fundamentals__ - Módulo 4
 ====================== 
 
## Objetivo
Neste módulo vamos desenvolver habilidade de persistir os dados tanto por aquivos como banco de dados.

## Conteúdo:
> 1. [Date e Time](#1-date-e-time)
> 2. [Trabalhando com Arquivos](#2-trabalhando-com-Arquivos)
> 3. [JSON ](#3-JSON)
> 4. [CSV](#4-CSV)
> 5. [Packages](#5-Package)
> 6. [Banco de Dados](#4-Banco-de-Dados)
> 7. [Laboratório](#10-laboratório)
> 8. [Lista de Exercício](#11-lista-de-exercício)

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

| mode | descrição |
|------|-----------|
| 'r' | Abre o arquivo apenas para leitura; |
| 'w' | Cria o arquivo para escrita, se o arquivo existir um arquivo com o mesmo nome, será deletado.| 
| 'a' | Abre o arquivo para escrita e adiciona o conteúdo no final do arquivo. |
| 'r+' | Modo especial de leitura e gravação, usado para lidar com as duas ações ao trabalhar com um arquivo.|

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

## 3 JSON

O Python manipula dados em JSON (JavaScript Object Notation) através da biblioteca interna `json`. Com ela podemos realizar as principais tarefas.

Nesse  primeiro exemplo, vamos transformar um json que está na string `json_string` para dicionário e assim acessar os dados. O método `loads` transforma o json em dicionário de dados.

```python
import json
json_string = '{"first_name": "Guido", "last_name":"Rossum"}'

parsed_json = json.loads(json_string)

print(parsed_json['first_name'])
```

No próximo exemplo vamos utilizar a função `dumps` para transformar um dicionário em json.

```python
import json
dados = {
          "nome" : "Jose",
		  "end"  : "rua de  baixo",
		  "idade": "40"
        }
json_dados = dados.dumps(dados)
print(json_dados)
```
Principais funções da classe json são:

* loads: Transforma um json em dicionário
* dumps: Transforma um dicionário no formato JSON

Uma combinação bastante utilizada e interessante é obter dados de API em JSON e manipular esse dados. No exemplo a seguir, utilizando a biblioteca `requests` para acessar os dados da API e assim transformar os dados em dicionários.

```python
import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

print(todos)
```

Também é possível escrever o JSON em um arquivo e também ler o JSON de um arquivo. O processo é semelhante a ler um arquivo texto comum.

Um exemplo para escrever o arquivo JSON em um arquivo.

```python
import json

dados = { 'nome': 'jose',
          'cidade': 'SP',
		  'partido': 'NOVO'
		  }

j_file = open('filename.json','w')
j_file.write(json.dumps(dados))
j_file.close()
```
Agora será utilizado o mesmo arquivo JSON para ler o conteúdoe realizar a transformação para dicionário.

```python
import json

j_file = open('filename.json','r')
raw = j_file.read()
j_file.close()

dados =  json.loads(raw)

print(dados['nome'])
print(dados)
```
## 4 CSV
Outra forma bastante comum para armazenar os dados os dados de forma estruturada é utilizando arquivos CSV (Comma Separated Values). 

A utilização do CSV é interessante porque programas exportão dados nessa estrutura e os dados também podem ser gerados pelas planilhas eletrônicas.

Como exemplo, vamos criar um arquivo CSV manualmente. Salve com o nome arquivo.csv. 

```csv
id;nome;idade;partido
1;jose;90;PT
2;maria;18;PSDB
3;carlos;20;NOVO
```
Perceba que o arquivo CSV utiliza um delimitador para separar os dados, no exemplo o delimitador utilizado é o ";".

Para manipulação de dados em CSV, vamos utilizar a biblioteca  `csv`. Primeiramente vamos lêr os dados do arquivo e transformar em uma lista.

O método `csv.reader` faz todo o trabalho que é ler o arquivo e transformar em uma lista que python facilmente consegue tratar.

```python
import csv
csvfile = open('arquivo.csv')
spamreader = csv.reader(csvfile, delimiter=';')

for item in spamreader:
  print(item)
```
Também podemos salvar os dados em um arquivo CSV. Nesse próximo exemplo tem uma lista chamado `dados` que contém as linhas com os valores que serão gravados no arquivo.

O método `csv.write` abre o arquivo para escrita e define o delimitador. Já o `writerow` salva os dados de uma linha.

```python
import csv
csvfile = open('eggs.csv', 'w') 
writer = csv.writer(csvfile, delimiter=';')

dados = [
           ['nome','idade','UF'],
           ['Maria','19','SP'],
           ['Jose','40','RJ'],
           ['Pedro','21','MG'],
        ]
for linha in dados:    
    writer.writerow(linha)

csvfile.close()
```

## 5 Packages

Até esse momento temos utilizado as bibliotecas internas do Python, mas existe um infinidades de outras bibliotecas que pode ser utilizado para auxiliar no desenvolvimento.

As bibliotecas externas podem ser instaladas facilmente utilizando o aplicativo `pip`.

As principais funções do `pip` são:

|  Commando   | descrição |
|-------------|-----------|
|  install    |  Instalação de pacotes. |
|  download   |  Download de pacotes. |
|  uninstall  |  Desinstalação de pacotes. |
|  freeze     |  Gera um arquivo `requirements` com os pacotes instalados. |
|  list       |  Lista todos os pacotes instalados. |
|  show       |  Mostra informação sobre um pacote instalado. |
|  check      |  Verify installed packages have compatible dependencies. |
|  search     |  Procura no PyPI por um pacote. |
|  help       |  Mostra ajuda. |

O `pip`utiliza o site `https://pypi.org/` como repositório para instalação dos pacotes.

Um exemplo da utilização 


Algumas bibliotecas interessantes:

| Nome | Descrição|
|------|----------|
| scikit-learn | Biblioteca adiciona um conjunto de algoritmos apropriados para executar tarefas de aprendizado de máquina, como agrupamento de dados, regressão e classificação.|
| Theano | Com os modelos da biblioteca Theano, é possível processar grandes volumes de dados — em teras ou petabytes — em alta velocidade, usando a chamada data-intensive computing. |
| TensorFlow | Desenvolvida pelo Google, TensorFlow é uma sucessora do DistBelief e usada para treinar redes neurais. Com sistemas de nós, a TensorFlow permite que se configure rapidamente várias camadas de dados, visando o treinamento e a implantação de redes neurais artificiais.Com essa biblioteca, o Google consegue identificar detalhes em fotos e entender palavras específicas em áudios nos aplicativos de reconhecimento de voz. |
| Scrapy | A Scrapy é usada na criação de bots que fazem o rastreamento sistemático da web e a extração de dados estruturados. São capazes também de colher dados também de APIs.As aplicações da Scrapy são variadas e vão de testes automatizados e monitoramento até mineração de dados e aprendizado de máquina. |
| NLTK | A NLTK um conjunto de bibliotecas projetado para processamento de linguagem natural. Entre suas funções básicas estão a marcação de textos, a identificação de entidades e a exibição de árvores de análise sintática. É útil para demandas de análise de sentimento do público-alvo e para resumos esquemáticos e mapas mentais.|
| NetworkX | Permite a criação e a análise de gráficos e dados em rede, contemplando formatos de dados padronizados e não estruturados. Isso torna a biblioteca NetworkX eficiente e escalável, especialmente quando a demanda está relacionada à análise de volumes de dados grandes e complexos, como os oriundos de redes sociais.|
| Selenium | Embora bastante conhecido para testes automatizados no navegador, o Selenium também pode ser usado como uma ferramenta de raspagem. Eu prometo a você, ele é muito bom. Com métodos para encontrar elementos via ids, nome, classe etc., o Selenium permitirá que você obtenha qualquer coisa do site.
| BeautifulSoup | é outro belo módulo Python que ajuda na raspagem dos dados necessários a partir de html/xmls via tags. Com ele, você pode raspar quase tudo, porque ele oferece métodos diferentes, como pesquisa de tags, encontrar todos os links etc.|
| Mechanize | Biblioteca que permite a criação de uma instância do navegador. Ele também mantém sessões que auxiliam como um toolkit para obter tarefas como login, automação de inscrição etc.|
| PyGames | Bibliotecas para desenvolvimento de jogos |
| Plotly | Biblioteca para gerar gráficos |

## 6 Banco de Dados

Para finalizar esse módulo será apresentado a biblioteca `sqlalchemy`. Essa biblioteca é muito interessante porque transforma a estrutura de banco de dados em código.

`SQLAlchemy` é um SQL toolkit ORM (Object Relational Mapper), ela abstrae as funções que são executadas em um banco de dados.

Muitos banco de dados são suportados, alguns deles são:
  * SQLite
  * Postgresql
  * MySQL
  * Oracle
  * MS-SQL
  * Firebird
  * Sybase
  * Muitos outros.

Para utilizar o `SQLAlchemy` precisamos instalar a biblioteca:

```bash
pip install SQLAlchemy
```

Com a biblioteca instalado, vamos criar um banco de dados e realizar as operações básicas utilizado CRUD.

```python
import os
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
  
Base = declarative_base()
 
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    nome   = Column(String(250), nullable=False)
    idade  = Column(String(250), nullable=False)
    cidade = Column(String(250), nullable=False)

banco = "banco_de_dado.db"
engine = create_engine("sqlite:///{0}".format(banco)) 

if not os.path.exists(banco):   
   Base.metadata.create_all(engine)

#Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
 
# Adicionando um novo registro
new_person = User(nome='clodonil',idade='10',cidade='SP')
session.add(new_person)
session.commit()
 
# Lista todos
def lista_todos(): 
    for user in session.query(User).all():
        print(user.name, user.idade, user.cidade)

# Pesquisar por um elemento espeficio
user1 = session.query(User).filter(User.name == 'clodonil').first()

lista_todos()
#Alterar um Registro
user1.name = "jose"
user1.idade = "20"
session.commit()
lista_todos()

# Delete 
user1 = session.query(User).filter(User.name == 'clodonil').first()
session.delete(user1)
session.commit()
```

## 7 Laboratório
No link abaixo temos o laboratório dirigido, faça o laboratório para praticar os conhecimentos apreendidos
> [Laboratório](Labs/README.md)

## 8 Lista de Exercício
Após realizar o laboratório e brincar com os códigos, teste o seu conhecimento com a lista de exercícios:
> [Lista de Exercícios](exercicios/README.md)

***
> By:
```python
Autor   = ['Clodonil Honorio Trigo','clodonil@nisled.org']
linkdin = 'https://www.linkedin.com/in/clodonil-trigo-4155722a'
Blog    = 'http://www.devops-sys.com.br'
```
