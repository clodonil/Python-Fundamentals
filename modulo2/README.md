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

* abs

**Descrição:** a função `abs()` retorna o valor absoluto de um número, isso é retorna o valor positivo.

**Exemplo:**
```pyton
print(abs(-100))   # retorna 100
print(abs(100))    # retorna 100
print(abs(-100.1)) # retorna 100.1
```

* dict

Descrição: A função `dict()` cria um novo dicionário de dados. É a mesma coisa que `{` e `}`.

Exemplo:
```pyton
a = dict()
a['jose'] = 10
print(a)
```
* help

Descrição: A função `help()` retorna uma ajuda para as funções internas do Python.

Exemplo:
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

Descrição: A função `all()` retorna True se todos os elementos de uma interação é True (ou se a interação estiver vázio).

Exemplo:
```pyton
x = [1,True]
print(all(x))     # Retorna True
x = [0,True]
print(all(x))     # Retorna False
```

* dir

Descrição: A função `dir()` retorna todas as variável e  função do escopo local.  Se um parâmetro for passado, será retornado todos os metodos daquela função.

Exemplo:
```pyton
a="teste"
print(dir())
print(dir(a))
```

* hex

Descrição: A função `hex()`, converte um número em string hexadecimal.

Exemplo:
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

Descrição: A função `any()`, retorna True se algum elemento da interação for verdade. Se a interação estiver vázia, retorna False.

Exemplo:
```pyton
x = [False,True]
print(any(x))     # Retorna True
x = []
print(any(x))     # Retorna False
```

* divmod
Descrição: `divmod()`

Exemplo:
```pyton
sdfsd
```

* id

Descrição: `id()`

Exemplo:
```pyton
sdfsd
```

* object

Descrição: `object()`

Exemplo:
```pyton
sdfsd
```

* sorted

Descrição: `sorted()`

Exemplo:
```pyton
sdfsd
```

* ascii

Descrição: `ascii()`

Exemplo:
```pyton
sdfsd
```

* enumerate

Descrição: `enumerate()`

Exemplo:
```pyton
sdfsd
```

* input
Descrição: `input()`

Exemplo:
```pyton
sdfsd
```

* oct

Descrição: A função `oct()`, converte um inteiro para uma string octal com prefixo "0o".

Exemplo:
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

Descrição: A função `bin`, converte um número inteiro em uma string binária.

Exemplo:
```pyton
print(bin(10))  # Retorna '0b1010'
```

* eval

Descrição: `eval()`

Exemplo:
```pyton
sdfsd
```

* int

Descrição: `int()`

Exemplo:
```pyton
sdfsd
```

* open

Descrição: `open()`

Exemplo:
```pyton
sdfsd
```

* str

Descrição: `str()`

Exemplo:
```pyton
sdfsd
```

* bool

Descrição: A função `bool()`, converte um valor, True, False, 0 e 1 para o  tipo booleano.

Convert a value to a Boolean

Exemplo:
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

Descrição: `isinstance()`

Exemplo:
```pyton
sdfsd
```

* ord

Descrição: A função `ord()`, retorna um inteiro como representação da string Unicode.

Exemplo:
```pyton
print(ord('a'))
```

* sum()

Descrição: `sum`

Exemplo:
```pyton
sdfsd
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

Descrição: `issubclass()`

Exemplo:
```pyton
sdfsd
```

* pow

Descrição: `pow()`

Exemplo:
```pyton
sdfsd
```

* super

Descrição: `super()`

Exemplo:
```pyton
sdfsd
```

* bytes

Descrição: `bytes()`

Exemplo:
```pyton
sdfsd
```

* float

Descrição: `float()`

Exemplo:
```pyton
sdfsd
```

* iter

Descrição: `iter()`

Exemplo:
```pyton
sdfsd
```

* print

Descrição:  A função `print()`, imprime na saída padrão

Exemplo:
```pyton
print("Olá Python")
```

* tuple

Descrição: `tuple()`

Exemplo:
```pyton
sdfsd
```

* callable

Descrição: `callable()`

Exemplo:
```pyton
sdfsd
```

* format

Descrição: `format()`

Exemplo:
```pyton
sdfsd
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

Descrição: A função `type()`, retorna o tipo do objeto.

Exemplo:
```pyton
print(type('a'))
```

* chr

Descrição: A função `chr()`, retorna a representação de uma string baseado code unicode da tabela ascii. A entrada sempre é um inteiro.


Exemplo:
```pyton
print(chr(97))   # Retorna 'a'
```

* frozenset

Descrição: `frozenset()`

Exemplo:
```pyton
sdfsd
```

* list

Descrição: `list()`

Exemplo:
```pyton
sdfsd
```

* range

Descrição: `range()`

Exemplo:
```pyton
sdfsd
```

* vars

Descrição: `vars()`

Exemplo:
```pyton
sdfsd
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

Descrição: `locals()`

Exemplo:
```pyton
sdfsd
```

* repr

Descrição: `repr()`

Exemplo:
```pyton
sdfsd
```

* zip

Descrição: `zip()`

Exemplo:
```pyton
sdfsd
```

* compile

Descrição: `compile()`

Exemplo:
```pyton
sdfsd
```

* globals

Descrição: `globals()`

Exemplo:
```pyton
sdfsd
```

* map

Descrição: `map()`

Exemplo:
```pyton
sdfsd
```

* reversed

Descrição: `reversed()`

Exemplo:
```pyton
sdfsd
```

* __import__

Descrição: `__import__()`

Exemplo:
```pyton
sdfsd
```

* complex

Descrição: `complex()`

Exemplo:
```pyton
sdfsd
```

* hasattr

Descrição: `hasattr()`

Exemplo:
```pyton
sdfsd
```

* max

Descrição: `max()`

Exemplo:
```pyton
sdfsd
```

* round	 

Descrição: `round()`

Exemplo:
```pyton
sdfsd
```

* delattr

Descrição: `delattr()`

Exemplo:
```pyton
sdfsd
```

* hash

Descrição: `hash()`

Exemplo:
```pyton
sdfsd
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

Descrição: A função `set()`, retorna um novo objeto com a estrutura de dados.

Exemplo:
```pyton
conj = set([1,2])
print(conj)
```



## 2. Principais bibliotecas
###  2.1 Strings
###  2.2 Number


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
