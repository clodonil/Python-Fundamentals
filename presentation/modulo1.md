<!-- $theme: gaia -->

# Python Fundamentals

#### [Módulo 1](https://github.com/clodonil/Python-Fundamentals/tree/master/modulo1)

###### [Clodonil Trigo (@clodonil)](https://github.com/clodonil)



---
<!-- page_number: true -->

# Overview

**Gaia** is the beautiful presentation theme on Marp!

- ==**New features**==
	1. Title Slides
	2. Highlight
	3. Color scheme

---
<!-- page_number: true -->

# História da Python

#### From menu

Select menu: *View :arrow_right: Theme :arrow_right: Gaia*

#### Use directive

Set `gaia` theme by `$theme` Global Directive.

```
<!-- $theme: gaia -->
```

---
<!-- page_number: true -->
## Ambiente de Desenvolvimento

- **Python 3** 
	- VS Code (Microsoft)
	- TextEdit
	- Notepad++
	- Vim
	- PyCharm


---
<!-- page_number: true -->
### Segregação de Ambientes

> Nunca se deve confiar em bibliotecas pré-instaladas, sempre deve ser declarado  atráves de um manifesto todas as dependências envolvidas na aplicação, conforme descrito [12factor](https://12factor.net/pt_br/dependencies).

- VirtualEnv
- Máquinas Virtuais

---

# VirtualEnv
Criado um VirtualEnv

```bash
$ python -m venv workspace_projeto
```
Ativando o VirtualEnv

```bash
$ source workspace_projeto/bin/active
```

Desativando o VirtualEnv

```bash
$ source workspace_projeto/bin/deactive
```

---
<!-- *template: gaia -->

## Sintaxe do Python


---

# Variável

Os nomes das variáveis é conforme a vontade do programador, com nomes longos, contendo letras e números. 
No entanto, elas devem necessariamente começar com 'letras minúsculas'. 

```bash
and       def       exec      if        not       return
assert    del       finally   import    or        try
break     elif      for       in        pass      while
class     else      from      is        print     yield
continue  except    global    lambda    raise
```

---
---

# Variável (exemplos)


```python
dados=10
```
Atribuição também pode ser realizado em cadeia, conforme o exemplo:

```python
dados=x=filho=10
```
Outra forma de realizar atribuição em cadeia:

```python
nome,idade,tel = 'jose',10,'56945-2342'
```

---
# Estrutura de Dados

* String;
* Number (Integer e Float);
* List;
* Tuple;
* Dictionary;
* Boolean

---
# String
Exemplo:
 ```python
texto="As vezes você tem que se levantar sozinho e seguir em frente"
```
Para declarar múltiplas linhas utilize 3 aspas simples.
Exemplo:
   ```python
texto='''
     Tudo e possível. 
     O impossível apenas demora mais
     '''
   ```
---
# Manipulando String

Exemplo:
```python
texto="As vezes você tem que se levantar sozinho e seguir em frente" 
# Recuperar o caractere da posição 5
print(texto[6])   # Retorno "e"
   
# Recuperar do inicio da string ate posição 10
print(texto[0:10])  # Retorno "As vezes v"
  
# Recuperar da posição 10 até a posição 15
print(texto[10:15]) # retorno "ocê t"
```
---
# Numbers

```python
a = 5
print(a, "do tipo", type(a))

a = 2.0
print(a, "do tipo", type(a))

a = 1+2j
print(a, "número complexo?", isinstance(1+2j,complex))
```
>No exemplo utilizamos a função `type()` para mostrar o tipo da classe da variável. Também usamos a função `isinstance()` para comparar o tipo da váriavel.
---
# List
Lista é Python é uma sequência de item, equivale aos arrays de outras linguagens.

```python 
lista=[10,60,'jose','45234234',50.9]
# Mostrando a lista
print("Conteúdo da lista", lista)
```
Estrutura da Lista:

|0 |1 |2     | 3        | 4  |
|--|--|------|----------|----|
|10|60|'jose'|'45234234'|50.9|

---
# List

Acessando elementos da lista

|0 |1 |2 | 3| 4 |5|6 |7   |
|--|--|--|--|---|-|-|---|
|10|30|50|90|100|1|5|19 | 

```python
lista=[10,30,50,90,100,1,5,19]

# lista[2] = 50
print("lista[2] = ", lista[2])

# lista[0:3] = [10, 30, 50]
print("lista[0:3] = ", lista[0:3])

# lista[5:] = [1, 5, 19]
print("lista[5:] = ", lista[5:])
```
---
# List
Alterando elementos da lista

```python

a = [1,2,3]
a[2]=4

# [1, 2, 4]
print(a)
```
---
# Tuple

As tuplas são uma sequência de itens, semelhante a uma lista. A diferença que a tuples são imultavél.

```python
t = (10,40,'jose','maria',6.5)

print(t[1])
```

**Tuple é mais rápido que uma lista**

---
# Dictionary
Dicionário são estrutura de dados com um par conhecido como `chave/valor`. 

```python
login = {"user": "jose","password":"okri"}

print("usuario", login['user'])
```
Hash:

|user|password|
|---|---------|
|jose|okri|

---
# Set
Set é uma coleção não ordenada de itens exclusivos (não pode ter itens repetidos).

```python
posicao_chegada={3,4,1,7,8}
print(posicao_chegada)
```

---
# Frozenset
`Frozen set` são conjuntos similares ao set. A diferença que frozenset são imutáveis, portanto não podem ser modificados.


```python
lista = ('a', 'e', 'i', 'o', 'u')

fSet = frozenset(lista)
print('O frozen set é:', fSet)
```
---
# Um outro exemplo:

```python
# random dictionary
person = {"name": "John", "age": 23, "sex": "male"}

fSet = frozenset(person)
print('The frozen set is:', fSet)
```
---
# Boolean
O tipo de dados Boolean em Python são criados pela classe `bool` que logicamente aceita 2 valores constantes `True` e `False`.

```python
print(type(True))
```
Os booleanos também podem ser presentados por inteiros sendo 1 para `True`e 0 para `False`.

---
# Conversão entre tipos

| Descrição| Função | Exemplo |
|----------|-----------|-----|
| Converte para intero.|  int(x) | num=int(a)|
| Converte para float.|float(x) |num = float(a) |
| Converte para String |str(x) | letra = str(num)  |
| Converte para uma tuple|tuple(s) |t_lista = tuple(lista)|
| Converte para Lista.|list(s) |lista = list(a) |
| Converte para Set.|set(s) | l = set(lista) |
| Converte um set em frozenset.| frozenset(s) |frozenset(x) |
| Converte um número em um string da tabela ascii. | chr(x) | chr(95) |
| Converte uma string em um valor da tabela ascii.| ord(x) | ord('a') |

---
# Operadores
Igualmente as outras linguagens de programação, as operações básicas de matemáticas são realizadas pelos operadores `+`, `-`, `/` e `*`. 

| Descrição     | Operador |
|---------------|----------|
| adição	       | +        |
| subtração	    | -        |
| multiplicação	| /        |
| divisão	      | *        |

---
# Exemplo
A utilização é bem simples.

```python
soma = 10 + 5
```
Python também segue as precedências definidas pela Matemática, porém sempre recomendamos utilizar parentes `( )` para separar os operadores, para tornar mais legível.
Por exemplo:

```python 
result = 2+2*2   # Resultado 6
#dessa forma fica mais legível
result = (2+2)*2 # Resultado 8
```
---
# Operadores de Atribuição

Operadores que fazem operação e atribuição.

| Descrição | Operador    |
|-----------|------------|
| soma e atribui         | +=       |
| subtrai e atribui      | -=       |
| dividi e atribui       | \*=       |
| multiplica e atribui   | /=       | 

---

# Exemplo:
```python
a = 10
a = a + 10 
a += 10
```
Além dos operadores básicos, também temos os operadores para exponenciação, extração do módulo da divisão, parte inteira de uma divisão.

|Descrição	|Operador|
|--------|-------|
|exponenciação	|**|
|parte inteira	|//|
|módulo|	%|

---
# Exemplo
A sintaxe para utilização desses operadores.

```python
result = 2 ** 2  # resutado  4
result = 5 // 2  # resultado 2
result = 5 %  2  # resultado 1
```
Esses operadores que vimos também podem ser utilizados com outras estruturas de dados tais como string e list.
Um exemplo de utilização com string:

```python
result = "-"*50   
result = "Ola" + "Mundo"
```
---
#Operadores com Lista:
```python
 lista = [1,2,3] * 10
 todos_numeros = [2,4,6,8] + [1,3,5,7] 
```
Além dos operadores matemáticos, também temos os operadores lógicos que retornam `True` e `False`.

|Descrição	|Operador|
|----------|--------|
|Maior que	|>|
|Menor que	|<|
|Igual a	|==|
|Maior ou igual a	|>=|
|Menor ou igual a	|<=|
| Negação        | not |
---
# Operadores Lógicos
A utilização dos operadores lógicos também é bem simples. Eles não são muito utilizados para tomadas de decisão em `IF`.
```python
a=10 > 5
b=100 == 200
if 200 > 100:
   print("maior")   
if a or b:
   print("Tudo certo")
if a and b:
   print("Tudo errado")
x = not(a and b)
```
Também temos os operadores para verificar se um item está contido em um conjunto, para testar identidade e para criar pequenas funções.

|Descrição | Operador|
|----------|---------|
|Contido em |in         |
| Teste de identidade               | is |
|Criar funções | lambda     |

Utilizamos muito o operador `in` para verificar se um valor está incluso em uma lista.
```python
x = 10 in [3,4,5,10]   | Retorna True
```
Já operador `is` é para testar a identidade de um objetivo. Verificar se realmente é o mesmo objeto.
```python
a=10
b=a
k = a is b   
print(id(a))
print(id(b))
a=[10,2,3]
b=[10,2,3]
k a is b
```
O operador lambda é bastante útil, com ele podemos fazer pequenas funções. 
```python
produdo = lambda  x,y: x*y
print(produto(6,4))
```

---
<!-- template: gaia -->

# ==That's all!==

## Let's create beautiful slides<br />with ==Marp== + ==Gaia== theme!
---
<!-- *template: invert -->

> In Greek mythology, **Gaia** also spelled **Gaea**, was the personification of the Earth and one of the Greek primordial deities.
>
> <small>-- *[Gaia (mythology) - Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Gaia_%28mythology%29)*</small>

---

---

#### `<!-- $theme: gaia -->` of Marp

###### [![](../images/marp.png)](https://yhatt.github.io/marp)

#### https://yhatt.github.io/marp
