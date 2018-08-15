__Python Fundamentals__ - Módulo 2
 ====================== 
 
## Objetivo
Apresentar o Python e introduzir os primeiros conceitos e ao final o aluno deve ter a capacidade de desenvolver pequenos programas.

## Conteúdo:
> 1.  [Funções builtin](#p1)
> 2.  [Principais bibliotecas](#P1)</br>
> 2.1 [Strings](#p1)</br>
> 2.2 [Number](#p1)</br>
> 2.3 [Data](#p1)</br>
> 2.3 [boolean](#p1)</br>
> 2.4 [List](#p1)</br>
> 2.5 [Tuple](#p1)</br>
> 2.5 [Dicionário](#p1)</br>
> 2.6 [Set](#p1)</br>
> 4. [Pip](#p1)
> 5. [Classes](#p1)
> 6. [Herança](#p1)
> 7. [Polimorfismo](#p1)
> 8. [Métodos](#p1)
> 9. [Atributos](#p1)
> 10. [Encapsulamento](#p1)
> 11. [Laboratório](#10-laboratório)
> 12. [Lista de Exercício](#11-lista-de-exercício)


## 1. Funções builtin

Por padrão o Python trás 68 comandos internos. São eles:

|            |            | Funções Built-in 		|      |        |
|------------|------------|---------------------|------|--------|
|abs()	      |dict()	      |help()	       |min()      |	setattr()|
|all()	      |dir()	       |hex()	        |next()	    |slice()|
|any()	      |divmod()     |	id()	        |object()	  |sorted()|
|ascii()	    |enumerate()	 |input()	      |oct()	     |staticmethod()|
|bin()	      |eval()       |	int()	       |open()     |	str()|
|bool()	     |exec()       |	isinstance()	|ord()	     |sum()|
|bytearray()	|filter()	    |issubclass()	 |pow()	     |super()|
|bytes()	    |float()      |	iter()	      |print()    |	tuple()|
|callable() 	|format()	    |len()	        |property()	|type()|
|chr()	      |frozenset()	 |list()	       |range()   	|vars()|
|classmethod()	| getattr()	|locals()      |	repr()   	|zip()|
|compile()	    |globals()  |	map()	       |reversed()	|\__import__()|
|complex()	    |hasattr()  |	max()        | 	round() 	| |
|delattr()	    |hash()     |	memoryview() |	set()	    ||

A seguir a descrição de cada função e um exemplo para ajudar na compreensão.

-----------

* abs

**Descrição:** a função `abs()` retorna o valor absoluto de um número, isso é retorna o valor positivo.

**Exemplo:**
```pyton
print(abs(-100))   # retorna 100
print(abs(100))    # retorna 100
print(abs(-100.1)) # retorna 100.1
```

* dict

**Descrição:** A função `dict()` cria um novo dicionário de dados. É a mesma coisa que `{` e `}`.

**Exemplo:**
```pyton
a = dict()
a['jose'] = 10
print(a)
```
* help

**Descrição:** A função `help()` retorna uma ajuda para as funções internas do Python.

**Exemplo:**
```pyton
print(help(id))
```

* min

Descrição: `min()`

Exemplo:
```pyton
sdfsd
```

* setattr

Descrição: `setattr()`

Exemplo:
```pyton
sdfsd
```

* all

**Descrição:** A função `all()` retorna True se todos os elementos de uma interação é True (ou se a interação estiver vázio).

**Exemplo:**
```pyton
x = [1,True]
print(all(x))     # Retorna True
x = [0,True]
print(all(x))     # Retorna False
```

* dir

**Descrição:** A função `dir()` retorna todas as variável e  função do escopo local.  Se um parâmetro for passado, será retornado todos os metodos daquela função.

**Exemplo:**
```pyton
a="teste"
print(dir())
print(dir(a))
```

* hex

**Descrição:** A função `hex()`, converte um número em string hexadecimal.

**Exemplo:**
```pyton
print(hex(123))
```

* next

Descrição: `next()`

Exemplo:
```pyton
sdfsd
```

* slice()

Descrição: `slice()`

Exemplo:
```pyton
sdfsd
```

* any

**Descrição:** A função `any()`, retorna True se algum elemento da interação for verdade. Se a interação estiver vázia, retorna False.

**Exemplo:**
```pyton
x = [False,True]
print(any(x))     # Retorna True
x = []
print(any(x))     # Retorna False
```

* divmod
**Descrição:** A função `divmod()`,retorna o resultado da divisão de 2 números inteiros e também o resto.

**Exemplo:**
```pyton
print(devmod(10,2)
```

* id

**Descrição:** A função `id()`, retorno o identificador de um objeto.

**Exemplo:**
```pyton
a=10
print(id(a))
```

* object

Descrição: `object()`

Exemplo:
```pyton
sdfsd
```

* sorted

**Descrição:** A função `sorted()`, retorna uma lista ordenada.

**Exemplo:**
```pyton
a=[3,5,1,9,10,100,-1]
print(sorted(a))
```

* ascii

Descrição: A função `ascii()`, retorna uma string da representação ascii

Exemplo:
```pyton
a=10
print(ascii(a))
```

* enumerate

**Descrição:** A função `enumerate()`, retorna um objeto enumerado (indexado). É possível utilizar apenas com objetivos interados (lista) e o retorno é uma tuple.

**Exemplo:**
```pyton
a  = ['maria','jose','pedro']
print(list(enumerate(a)))
```

* input
**Descrição:** A função `input()`, recebe dados da entrada padrão (teclado.

Exemplo:
```pyton
texto = input("Digite um texto:")
idade   = int(input("Digite a sua idade:"))
```

* oct

**Descrição:** A função `oct()`, converte um inteiro para uma string octal com prefixo "0o".

**Exemplo:**
```pyton
print(oct(10))
```

* staticmethod

Descrição: `staticmethod()`

Exemplo:
```pyton
sdfsd
```

* bin()

**Descrição:** A função `bin`, converte um número inteiro em uma string binária.

**Exemplo:**
```pyton
print(bin(10))  # Retorna '0b1010'
```

* eval

**Descrição:** A função `eval()` avalia uma string como uma expressão python.

Exemplo:
```pyton
print(eval('1+1'))
a = 10
print(eval('a+1'))
```

* int

**Descrição:** A função `int()`, retorna um inteiro apartir de uma string.

**Exemplo:**
```pyton
a = int('10')
print(a)
```

* open

Descrição: `open()`

Exemplo:
```pyton
sdfsd
```

* str

Descrição: A função `str()`, retorna uma string

Exemplo:
```pyton
a=10
print(str(a))
```

* bool

**Descrição:** A função `bool()`, converte um valor, True, False, 0 e 1 para o  tipo booleano.

**Exemplo:**
```pyton
print(bool(True))  # retorna True
print(bool(0))     # retorna False
```

* exec

Descrição: `exec()`

Exemplo:
```pyton
sdfsd
```

* isinstance

**Descrição:** A função `isinstance()`, retorna True se a objeto é da mesma classe espeficicada.

**Exemplo:**
```pyton
print(isinstance(10,int))
```

* ord

**Descrição:** A função `ord()`, retorna um inteiro como representação da string Unicode.

**Exemplo:**
```pyton
print(ord('a'))
```

* sum()

**Descrição:** A função `sum`, retorna a soma de um objeto interavel, tais como lista.

**Exemplo:**
```pyton
a = [ 10,15,40,20 ]
print(sum(a))
```

* bytearray

Descrição: `bytearray()`

Exemplo:
```pyton
sdfsd
```

* filter

Descrição: `filter()`

Exemplo:
```pyton
sdfsd
```

* issubclass

**escrição:** A função `issubclass()`, retorna True em uma classe é subclasse da verificada.

**Exemplo:**
```pyton
class Person:
       nome = 'jose'
       idade = 30

class Politico(Person):
      salario=100000
.
print(issubclass(Politico,Person))
```

* pow

Descrição: A função `pow()`, retorna a potência de um número. 

Exemplo:
```pyton
#retornar a 2 potência  5
print(pow(2,5)
```

* super

**Descrição:** A função `super()` é utilizado para sobrescrever um metodo herdado de uma class.

**Exemplo:**
```pyton
Class Pai(object):
  def __init__(self):
    print('Construindo a classe Pai')

    
class Filha(Pai):
  def __init__(self):
    super().__init__()
```

* bytes

Descrição: `bytes()`

Exemplo:
```pyton
sdfsd
```

* float

**Descrição:** A função `float()`, retorna um número float. 

**Exemplo:**
```pyton
a = float('10.3')
print(a)
```

* iter

Descrição: `iter()`

Exemplo:
```pyton
sdfsd
```

* print

**Descrição:**  A função `print()`, imprime na saída padrão

**Exemplo:**
```pyton
print("Olá Python")
```

* tuple

Descrição: A função `tuple()`, retorna um tuple de elementos.

Exemplo:
```pyton
x= tuple(a)
print(x)
```

* callable

Descrição: `callable()`

Exemplo:
```pyton
sdfsd
```

* format

Descrição: A função `format()`, formata uma  string que contem campos entre chaves a serem substituídos pelos argumentos de format..

Exemplo:
```pyton
x= 10 
comando = "linha {0}".format(x)
```

* len

Descrição: A função `len()`, retorno o tamanho de um objeto. 

Exemplo:
```pyton
a="texto"
b=[1,2,3,4]
print(len(a))
print(len(b))
```

* property

Descrição: `property()`

Exemplo:
```pyton
sdfsd
```

* type

**Descrição:** A função `type()`, retorna o tipo do objeto.

**Exemplo:**
```pyton
print(type('a'))
```

* chr

**Descrição:** A função `chr()`, retorna a representação de uma string baseado code unicode da tabela ascii. A entrada sempre é um inteiro.


**Exemplo:**
```pyton
print(chr(97))   # Retorna 'a'
```

* frozenset

**Descrição:** A função `frozenset()`, retorna um novo conjunto fronzenset.

**Exemplo:**
```pyton
vowels = ('a', 'e', 'i', 'o', 'u')
fSet = frozenset(vowels)
print('O frozen set eh:', fSet)
```

* list

**Descrição:** A função `list()`, cria uma lista de elementos.

**Exemplo:**
```pyton
lista = [1,2,3,4]
print(lista)
```

* range

**Descrição:** A função `range()`, retorna um serie de números no intervalo informado.

**Exemplo:**
```pyton
for k in range(1,10):
    print(k)
```

* vars

Descrição: A função `vars()` retorna um dicionário com todas as variável daquele escopo.

Exemplo:
```pyton
print(vars())
```

* classmethod

Descrição: `classmethod()`

Exemplo:
```pyton
sdfsd
```

* getattr

Descrição: `getattr()`

Exemplo:
```pyton
sdfsd
```

* locals

Descrição:  `locals()`

Exemplo:
```pyton
sdfsd
```

* repr

**Descrição:** A função `repr()`, é utilizada para retornar uma string da representação do objetivo. Muito utilizado nos consoles.

**Exemplo:**
```pyton
>>> a = "banana"
>>> a
banana
```

* zip

**Descrição:** A função `zip()`, retorna uma tupla cotendo a junção de duas listas, elemento a elemento.

**Exemplo:**
```pyton
x=[100,200,300]
y=[1000,2000,3000]

for i in zip(x,y):
   print(i)
```

* compile

Descrição: `compile()`

Exemplo:
```pyton
sdfsd
```

* globals

**Descrição:** A função `globals()`, retorna um dicionário contendo a lista global de variável.

**Exemplo:**
```pyton
print(globals())
```

* map

Descrição: `map()`

Exemplo:
```pyton
sdfsd
```

* reversed

**Descrição:** A função `reversed()`, inverte uma lista.  Não é realizada a ordenação, apenas a inversção das posições.

**Exemplo:**
```pyton
a = [ 100,2,5,9,1]
print(list(reversed(a)))
```

* __import__

**Descrição:** A `__import__()`, é invocada pelo import. É utilizado para incoporar partes de outros programas

**Exemplo:**
```pyton
import spam
```

* complex

**Descrição:** A `complex()`, retorna um número complexo.

**Exemplo:**
```pyton
x = complex('1+2j')
print(x)
```

* hasattr

**Descrição:** A função `hasattr()`, retorna True se um metodo ou variável existir em um objeto (classe)

Exemplo:
```pyton
class Person:
     nome="jose"
     idade=30


print(hasattr(Person,'nome'))
print(hasattr(Person,'idade'))
print(hasattr(Person,'salario'))
```

* max

**Descrição:** A função `max()`, retorno a maior valor de uma lista.

**Exemplo:**
```pyton
a = [100,200, 500,1,2,3]
print(max(a))
```

* round	 

**Descrição:** A função `round()`, retorna o arendondamento de um númeto

**Exemplo:**
```pyton
x = round(10.9)
print(x)
```

* delattr

Descrição: `delattr()`

Exemplo:
```pyton
sdfsd
```

* hash

**Descrição:** A função `hash()` retorna um valor inteiro. utilizado para verificar integridade.

**Exemplo:**
```pyton
x = "texto 1"
print(hash(x))
```

* memoryview

Descrição: A função `memoryview()`, retorna um objetivo do tipo memoryview, de acesso rápido.

Exemplo:
```pyton
v = memoryview(b'abcefg')
print(v[1])
print(v[-1])
print(v[1:4])
print(v[1:4])
```

* set	 

**Descrição:** A função `set()`, retorna um novo objeto com a estrutura de dados.

**Exemplo:**
```pyton
conj = set([1,2])
print(conj)
```

## 2. Principais Métodos
###  2.1 Strings
###  2.2 Number
* Inteiro

```python
a=10
```

| Méthodo  | Descrição  | Exemplo| Resultado|
|----------|------------|--------|-----------|
|bit_length |           |        |          |
|conjugate|           |        |          |
|denominator|           |        |          |
|from_bytes|           |        |          |
|imag|           |        |          |
|numerator|           |        |          |
|real|           |        |          |
|to_bytes|           |        |          |


* Float

```python
a=10.1
```

| Méthodo  | Descrição  | Exemplo| Resultado|
|----------|------------|--------|-----------|
as_integer_ratio|           |        |          |
conjugate|           |        |          |
fromhex|           |        |          |
hex|           |        |          |
imag|           |        |          |
is_integer|           |        |          |
real|           |        |          |
###  2.3 Data
###  2.3 boolean
###  2.4 List
###  2.5 Tuple
###  2.5 Dicionário
###  2.6 Set
## 4.  Pip
## 5.  Classes
## 6.  Herança
## 7.  Polimorfismo
## 8.  Métodos
## 9.  Atributos
## 10. Encapsulamento
## 11 Laboratório
No link abaixo temos o laboratório dirigido, faça o laboratório para práticar os conhecimentos apreendidos
> [Laboratório](https://github.com/clodonil/curso_python/tree/master/modulo1/Labs)

## 11 Lista de Exercício
Após realizar o laboratório e brincar com os códigos, teste o seu conhecimento com a lista de exercicio:
> [Lista de Exercício](exercicios/README.md)

***
> By:
```python
Autor   = ['Clodonil Honorio Trigo','clodonil@nisled.org']
linkdin = 'https://www.linkedin.com/in/clodonil-trigo-4155722a'
Blog    = 'http://www.devops-sys.com.br'
```
