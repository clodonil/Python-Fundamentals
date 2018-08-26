__Python Fundamentals__ - Módulo 2
 ====================== 
 
## Objetivo
Apresentar o Python e introduzir os primeiros conceitos e ao final o aluno deve ter a capacidade de desenvolver pequenos programas.

## Conteúdo:
> 1.  [Funções builtin](#p1)
> 2.  [Principais bibliotecas](#P1)</br>
> 2.1 [Strings](#p1)</br>
> 2.2 [Number](#p1)</br>
> 2.4 [List](#p1)</br>
> 2.5 [Tuple](#p1)</br>
> 2.5 [Dicionário](#p1)</br>
> 2.6 [Set](#p1)</br>
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
|all()	      |dir()	       |hex()	        |next()	    |zip()|
|any()	      |divmod()     |	id()	        |object()	  |sorted()|
|ascii()	    |enumerate()	 |input()	      |oct()	     |type()|
|bin()	      |eval()       |	int()	       |open()     |	str()|
|bool()	     |exec()       |	isinstance()	|ord()	     |sum()|
|bytearray()	|filter()	    |issubclass()	 |pow()	     |super()|
| vars()  |float()      |	iter()	      |print()    |	tuple()|
|callable() 	|format()	    |len()	        |property()	|\__import__()|
|chr()	      |frozenset()	 |list()	       |range()   	||
|classmethod()	| getattr()	|locals()      |	repr()   	||
|compile()	    |globals()  |	map()	       |reversed()	||
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

Descrição: A `min()` retorna o menor valor de uma lista.

Exemplo:
```pyton
lista=[100,8,9,19,1,80]
print(min(lista))
```

* setattr

Descrição: A função `setattr()` atribui um valor para um atributo.

Exemplo:
```pyton
class Pessoa:
   nome="ze"
funcionario = Pessoa()
setattr(funcionario,'nome','pedro')
print("O nome do funcionario: {0}".format(funcionario.name))
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

**Descrição:** A função `dir()` retorna todas as variável e função do escopo local.  Se um parâmetro for passado, será retornado todos os metodos daquela função.

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

Descrição: A função `next()`, retorno o próximo objeto de uma interação.


Exemplo:
```pyton
nomes = ['jose','pedro','maria']
obj = iter(nomes)
print(next(obj))
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


* filter

Descrição: A função `filter()`, filtra os elementos de uma sequência. O processo de filtragem é definido a partir de uma função que o programador passa como primeiro argumento da função.

Exemplo:
```pyton
print(list(filter(lambda n: n % 2, range(6))))
```

* issubclass

**Descrição:** A função `issubclass()`, retorna True em uma classe é subclasse da verificada.

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

* float

**Descrição:** A função `float()`, retorna um número float. 

**Exemplo:**
```pyton
a = float('10.3')
print(a)
```

* iter

Descrição: A função `iter()` retorna um objeto que pode ser interado.

Exemplo:
```pyton
nomes = ['jose','maria','pedro']
lista = iter(nomes)
print(next(lista))  # jose
print(next(lista))  # maria
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

Descrição: A função `callable()`, retorna true se um objeto é acc

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

Descrição: A função `getattr()`, retorna o valor de um objeto.

Exemplo:
```pyton
class Pessoa:
     nome = "jose"

diretoria = Pessoa()
print(getattr(diretoria,'nome'))
```

* locals

Descrição:  A função `locals()` retorna as varíáveis que estão declaradas no escopo local

Exemplo:
```pyton
print(locals())
```

* repr

**Descrição:** A função `repr()`, é utilizada para retornar uma representaçao do objeto em string. Utilizado em console. No exemplo, quando digitamos a no console, a função repr é invocado para ser apresentada o valor no console.
**Exemplo:**
```pyton
a = "banana"
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

Descrição: A função `compile()` retorna um objeto de código Python apatir de uma string.

Exemplo:
```pyton
code = 'a=10\nb=20\nprint("soma:{0}".format(a+b))'
codeObj = compile(code, 'soma', 'exec')
exec(codeObj)
```

* globals

**Descrição:** A função `globals()`, retorna um dicionário contendo a lista global de variável.

**Exemplo:**
```pyton
print(globals())
```

* map

Descrição: A função `map()`, serve para aplicarmos uma função a cada elemento de uma lista.

Exemplo:
```pyton
alunos = ['jose','mario','clodonil','carlos']
print(list(map(len,lista)))
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

Descrição: A função `delattr()`, desaloca um objeto.  

Exemplo:
```pyton
class Coordinate:
  x = 10
  y = -5
  z = 0

point1 = Coordinate() 

print('x = ',point1.x)
print('y = ',point1.y)
print('z = ',point1.z)

delattr(Coordinate, 'z')

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
Uma variável do tipo string possue uma série de métodos que auxiliam no desenvolvimento.
```python
s = "se nada mudar, invente."
```
|Método |	Descrição | 
|-------|-------------|
|s.capitalize()	|Retorna uma nova string com a primeira letra em maiusculo.|
|s.center(width, char)	|Retorna uma nova string no tamanho width centralizada com espaços ou char preenchendo ambos o lados.|
|s.ljust(width, char)	|Retorna uma nova string no tamanho width alinhada a esquerda e com espaços ou char preenchendo o restante à direita.|
|s.rjust	|Retorna uma nova string no tamanho width alinhada a direita e com espaços ou char preenchendo o restante à esquerda.|
|s.count(t, end)	|Retorna o número de ocorrências de t em s ou na fatia de s finalizado em end.|
|s.find(t, start, end)	|Retorna a posição de t mais a esquerda em s ou na fatia começando por start e terminado em end. Se nada for encontrado retorna -1.|
|s.rfind(t, start, end)	|O mesmo que find() porém buscando a partir da direita.|
|s.isalnum()	|Retorna True se s não for vazia e cada caractere de s é alfanumérico.|
|s.isalpha()	|Retorna True se s não for vazia e cada caractere de s é uma letra.|
|s.isdecimal()	|Retorna True se s não for vazia e cada caractere de s é um numérico Unicode.|
|s.isdigit()	|Retorna True se s não for vazia e cada caractere de s é é um numérico ASCII.|
|s.isidentifier()	|Retorna True se s não for vazia e um identificador valido.|
|s.islower()	|Retorna True se s não for vazia e todos os caracteres estão em minusculas.|
|s.isuper()	|Retorna True se s não for vazia e todos os caracteres estão em maiúscula.|
|s.isspace()	|Retorna True se s não for vazia e todos os caracteres são espaços.|
|s.join(t)	|Fatia t é insere s entre cada pedaço de t, exemplo: s = ‘.’ t=’dois’ s.join(t)=’d.o.i.s’|
|s.lower()	|Retorna uma nova string toda em minusculas.|
|s.upper()	|Retorna uma nova string toda em maiúsculas.|
|s.partition(t)|	Retorna uma tupla de três strings a parte de s antes de t, t e e a parte de s depois de t.|
|s.split(t, n)|	Retorna uma lista de strings fragmentas pela string t no máximo n vezes. Se n não for dado fragmenta tudo. Se t não for dado fragmenta pelos espaços em branco.|
|s.splitlines(f)|	Retorna um lista de strings fragmentadas no finalizador de linhas e sem os finalizadores ou com eles caso f seja True.|
|s.strip(t)|	Retorna uma nova string retirando os caracteres de espaço a direita e a esquerda ou se for dado os caracteres em t.|
|s.lstrip(chars)|	Retorna uma nova string retirando os caracteres de espaço a a esquerda ou se for dado os caracteres em chars.|
|s.rstrip(chars)|	Retorna uma nova string retirando os caracteres de espaço a a direita ou se for dado os caracteres em chars.|
|s.swapcase()|	Retorna uma nova string trocando maiúsculas por minusculas e vice versa.|
|s.title()|	Retorna uma nova string com a primeira letra de cada palavra em maiúscula.|
|s.zfill(n)|	Retorna uma nova string em que se s for menor que n o que estiver a esquerda e substituído por zeros.|
###  2.2 Number
* Inteiro

```python
a=10
```

| Méthodo  | Descrição  | Exemplo| Resultado|
|----------|------------|--------|-----------|
|bit_length |  Quantidade de bit para guardar o Inteiro         | bin(a); a.bin_length()       |  '0b1010' , 4        |
|to_bytes|  Retonar uma array com os bytes que representam o inteiro.         |   a.to_bytes(2, byteorder='big')     |   b'\x00\n'       |


* Float

```python
a=10.1
```

| Méthodo  | Descrição  | Exemplo| Resultado|
|---------|-------------|-------|-----------|
as_integer_ratio| Retorna um par de inteiros cuja proporção é exatamente igual ao float original e com um denominador positivo.          |        |          |
fromhex| Retorna o float hex de uma string          | a.fromhex('b')       | 11.0         |
hex| Converte um float em Hex          | a.hex()       |  '0x1.4333333333333p+3'        |
is_integer|  Verifica se o conteúdo do float é Inteiro         |   float(10).is_integer() |  True         |

###  2.4 List
* list

```python
lista=[]
```

| Méthodo  | Descrição  | Exemplo| Resultado |
|----------|------------|--------|-----------|
|append    | Adiciona um item no final da lista           |  lista.append('jose')      |  lista ['jose']         |
|copy  | Faz uma copia da lista           |   lista_b = lista.copy()     |  lista_b ['jose']         |
|count  |  retorna o número de ocorrência de um item          | lista.count('jose')       |  1         |
|extend  | Prolonga a lista, adicionando no fim todos os elementos de outra lista            | lista.extend([10,'maria')       |   lista['jose',10,'maria']        |
|index  |Devolve o índice do primeiro item cujo valor é igual a x| lista.index('jose')       |  0         |
|insert  | Insere um item em uma posição especificada. | lista.insert(0,'pedro')       | lista['pedro','jose',10,'maria']          |
|pop  |Remove o item na posição dada e o devolve. |   lista.pop() lista.pop(0)     |    maria pedro       |
|remove  | Remove o primeiro item encontrado na lista conforme o valor passado.     |   lista.remove('jose')     |           |
|reverse  |Inverte a ordem dos elementos na lista             |    lista.reverse()    |   [10, jose]  |
|sort  |  Ordena os itens na própria lista           |   lista.sort()     |  [1,2,3]         |
|clear  | Limpa toda a lista (remove tudo)           |   lista.clear()     |           | lista [ ]
###  2.5 Tuple
###  2.5 Dicionário
###  2.6 Set
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
