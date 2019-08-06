__Python Fundamentals__ - Módulo 3
 ====================== 
 
## Objetivo
Apresentar os vários estilos (paradigmas) de programação em Python, visando a OOP.

## Conteúdo:
> 5. [Classes](#p1)
> 6. [Herança](#p1)
> 7. [Polimorfismo](#p1)
> 8. [Métodos](#p1)
> 9. [Atributos](#p1)
> 10. [Encapsulamento](#p1)
> 11. [Laboratório](#10-laboratório)
> 12. [Lista de Exercício](#11-lista-de-exercício)

## 1. MultiParadigma

Como todas as linguagens modernas, Python é multiParadigma. Isso significa que pode ser "programada" em mais de um estilo. Com isso você pode ter mais ferramentas para usar no dia a dia. Você pode aumentar sua capacidade de expressar ideias de diferentes maneiras.

Python tem o estilo básico de programação [imperativa](https://en.wikipedia.org/wiki/Imperative_programming), que são a maiorias do comandos que controlam o fluxo, atribuição de variáveis.

> Na programação imperativa, o foco está no ato de mudar variáveis. A computação se dá pela modificação dos estados das variáveis iniciais. Sendo assim, vamos pensar que tudo é definido no início e vai se modificando até que o resultado esperado.


```python
# Gerar uma lista da string # Imperativo
string = 'Python'
lista = [] # estado inicial

for l in string:
    lista.append(l) # cada iteração gera um novo estado

print(lista) # ['P', 'y', 't', 'h', 'o', 'n']
```

Python também tem influência do [`paradigma funcional`](https://en.wikipedia.org/wiki/Functional_programming), permitindo recursão, uso de lambda, compreensões de coleções de dados, etc. 

> Na programação funcional, se tem a noção de que o estado deve ser substituído, no caso da avaliação, para criação de um novo 'objeto' que no caso são funções.

```python
# Gerar uma lista da string # Funcional
string = lambda x: x

lista = list(map(str, string('Python'))) # atribuição a um novo objeto

print(lista) # ['P', 'y', 't', 'h', 'o', 'n']
```

## Procedural

O desenvolvimento através do [paradigma procedural](https://en.wikipedia.org/wiki/Procedural_programming) estrutura a execução através de rotinas estanques que são chamadas conforme a necessidade. Normalmente as chamamos de procedures/funções.


Em algumas linguagens a diferenciação entre procedures e funções se dá pelo fato que função retorna algum valor e o procedure, apenas processa algo. No `Python` a função `return` devolve o conteúdo da variável declarada como retorno.

A programação em procedures (procedimentos), procura seguir o procedimento e comportamento.

```python

def soma(x,y):
    result = x + y
    return result


if __name__ == "__main__":
    x= soma(10,30)
    print(x)
```

> * O `if __name__ == "__main__"` é utilizado quando queremos que seja executado somente quando o arquivo é executado diretamente. Quando importado de outro arquivo, não deve ser executado.* 

No desenvolvimento procedural, é muito comum serem criados bibliotecas de funções, como o exemplo a seguir:

```python
#filename: calc.py
def soma(x,y):
    return x+y

def subtracao(x,y):
    return x-y

def divisao(x,y):
    return x/y

def multiplicacao(x,y):
    return x*y
```

Com a criação da biblioteca `calc.py`, pode ser utilizada em várias partes do programa, sendo necessário apenas importar `import`.

Pode ser importado o arquivo inteiro, com todas as funções ou apenas funções especificas.

```python
import calc

if __name__ == "__main__":
    x= calc.soma(10,30)
    print(x)
```

No exemplo anterior, importamos todas as funções do arquivo `calc.py`, entretanto precisamos especificar o nome do arquivo na chamada da função. Já no próximo exemplo, importamos apenas a função `soma`. Quando usamos o `from` a escrita fica mas simplificada, não precisando apontar o nome do arquivo na chamada da função.

```python
from calc import soma

if __name__ == "__main__":
    x= soma(10,30)
    print(x)
```

Em caso de organizar os códigos em subdiretórios, a chamada da função trata os diretórios como [Modulos](https://docs.python.org/3/tutorial/modules.html). 

No próximo exemplo, temos o arquivo `main.py` que chama o `calc.py` que está dentro do subdiretório `libs`.

```
 /main.py
   /libs/
       calc.py
```
Nesse caso, fica assim `from libs.calc import soma`. Perceba que o caminho do arquivo é definido, usando o ponto do separador.

## Escopo de Variável

O escopo de variável no Python é um tanto peculiar, é importante conhecer. 

Toda variável declarada fora de uma função, são do tipo `global` e podem ser acessadas pelas funções, mais não podem ser modificadas diretamente.

Exemplo:

```python
x = 30
y = 20
controle = 0
def verifica():
    if x > y:
       print('maior')
    else:
       print('menor')   


verifica()
```

Utilizando o mesmo exemplo, se tentarmos atualizar a variável `controle` dentro do `if x > y`, vai apresentar um erro.

```python
x = 30
y = 20
controle = 0
def verifica():
    if x > y:
       print('maior')
       controle += x
    else:
       print('menor')   


verifica()
```

> Erro apresentado: UnboundLocalError: local variable 'controle' referenced before assignment

Caso queira de fato alterar o conteúdo da variável `global`, é necessário declarar explicitamente:

```
x = 30
y = 20
controle = 0
def verifica():
    global controle
    if x > y:
       print('maior')
       controle += x
    else:
       print('menor')   


verifica()
```



## OOP

[ orientação a objetos](https://en.wikipedia.org/wiki/Object-oriented_programming)


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