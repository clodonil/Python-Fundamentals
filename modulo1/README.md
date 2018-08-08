 __Python Fundamentals__ - Módulo 1
 ====================== 
 
## Objetivo
Apresentar o Python e introduzir os primeiros conceitos e ao final o aluno deve ter a capacidade de desenvolver pequenos programas.

## Conteúdo:

> 1. [História](#p1)
> 2. [Filosofia da Linguagem](#p2)
> 3. [Ambiente de Desenvolvimento](#p3)
> 4. [Sintaxe básica](#p4)
> 5. [Variável](#p5)
> 6. [Estrutura de Dados](#p6)
>     6.1. [String](#p6.1)
>     6.2. [Numbers](#p6.2)
>     6.3. [List](#p6.3)
>     6.4. [Tuple](#p6.4)
>     6.5. [Dictionary](#p6.5)
>     6.6. [Set](#p6.6)
>     6.7. [frozenset](#p6.7)
>     6.8. [Boolean](#p6.8)
>     6.9. [Conversão entre tipos](#p6.9)
> 7. [Operadores](#p7)
> 8. [Controle de Fluxo](#p8)
> 9. [Outras funções](#p9)
> 10. [Laboratório](#p10)
> 11. [Lista de Exercício](#p11)

## 1 História
No Brasil em 1989, Collor de Melo vencia a primeira eleição direta, na Alemanha caia o muro de Belim e na Holanda o Guido Van Rossum criava a linguagem Python.

A história da linguagem é fantástica e seu aprendizado vai se tornar mais divertido após tomar conhecimento de alguns eventos que aconteceram.

Não vou escrever sobre a história do Python porque já tem muita coisa boa escrita, segue alguns links que vale a pena ler:

* [http://mindbending.org/pt/a-historia-do-python](http://mindbending.org/pt/a-historia-do-python)
* [https://www.python-course.eu/python3_history_and_philosophy.php](https://www.python-course.eu/python3_history_and_philosophy.php)
* [https://wiki.python.org.br/HistoriaDoPython](https://wiki.python.org.br/HistoriaDoPython)

## 2 Filosofia da Linguagem
A linguagem Python tem uma filosofia. Siga e seja Feliz.

> O [Zen Python](https://www.python.org/dev/peps/pep-0020/) por Tim  Peters
* Bonito é melhor que feio.
* Explícito é melhor que implícito.
* Simples é melhor que complexo.
* Complexo é melhor que complicado.
* Linear é melhor que aninhado.
* Esparso é melhor que denso.
* Legibilidade conta.
* Casos especiais não são especiais o suficiente para violar as regras.
* Ainda que praticidade vença pureza.
* Erros nunca devem passar silenciosamente.
* A menos que sejam explicitamente silenciados.
* Em caso de ambiguidade, resista à tentação de adivinhar.
* Deve haver um - e somente um - jeito óbvio de fazer.
* Embora esse modo possa não ser óbvio a princípio a menos que você seja holandês.
* Agora é melhor que nunca.
* Embora nunca é frequentemente melhor que exatamente agora.
* Se a implementação é difícil de explicar, a ideia é ruim.
* Se a implementação é fácil de explicar, talvez a ideia seja boa.
* Namespaces são uma grande idéia - vamos fazer mais deles!

## 3 Ambiente de Desenvolvimento
Para começarmos a programar, precisamos ter instalado no computador a linguagem de Programação Python3 e também um editor de texto.
Caso você tenha dificuldade para instalar o Python, siga os seguintes links:

* [Instalação no Windows](https://python.org.br/instalacao-windows/)
* [Instalação no Ubuntu](https://python.org.br/instalacao-linux/)
* [Instalação no Centos7](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-centos-7)

Os editores que recomendo para o desenvolvimento com o Python são:
* code (microsoft)
* TextEdit
* Notepad++
* Vim

Para aqueles que desejam ter uma máquina virtual em Linux para desenvolver o seu código, estou deixando o código do Vagrant preparado para provisionar um centos7 com o Centos7 instalado (Você precisa ter o Vagrant instalado no seu computador e também o Virtualbox).

Para utilizar, entre na pasta 'vms' e digite:
```
$ vagrant up
 ```
 Após subir o Linux, entre e no Linux:
 
 ```
$ vagrant ssh python
```
Outra possibilidade também é utilizar uma IDE que está na cloud. No meu ponto de vista os melhores são:
* [cloud9](https://c9.io/login)
* [repl](https://repl.it/languages/python3)

É só se cadastrar e sair usando.

## 4 Sintaxe básica

Se você já programa em outra linguagem está acostumado declarar o tipo de dados que a variável vai receber. Isso é muito comum em `C`, `JAVA` e várias outras linguagem.

O Python é diferente, ela entra nos grupos de linguagem que tem tipagem dinâmica e forte. 

Dizemos que uma linguagem tem tipagem dinâmica quando o próprio interpretador infere o tipo de dados de uma variável recebe, sem a necessidade que você, o usuário da linguagem diga.

A tipagem forte significa que o interpretador do Python avalia as expressões (evaluate) e não faz coerções automáticas entre tipos não compatíveis (conversões de valores). Por ele ser dinâmica, não significa que todos os tipos de conversões são permitidas.

Além da tipagem dinâmica e forte, o Python tem uma sintaxe simples e direta. Porém, um ponto de dificuldade aos iniciantes, são os blocos de códigos.

Blocos de códigos em outas linguagem  são marcas por `{` e  `}`, como por exemplo em `C`:

```c
if (x > 5){
   printf("maior")
}else {
   printf("menor")
}
```

Outras linguagens como o Ruby utiliza o `do`e `end` para limitar o blodo de código:

```ruby
if x > 5
   echo "Maior"
else
   echo "Menor"
end
```
O Python não tem nada disso, todo o controle do bloco de código é realizado por espaçamento.Se os espaçamentos não forem realizados corretamente, o código não vai funcionar.

Exemplo do if com bloco de código:

```python
if x > 5
   print("Maior")
else
   print("Menor")
```
Perceba que o único controle que existe para determinar o bloco de código é o espaçamento. Como já falei, isso no inicio pode trazer problemas, mais é algo que é incorporado rapidamente.

A vantagen da tabulação que o código semple está aninhado, com as hieraquias bem definicas, tornando o código muito mais fácil de ler e realizar as modificações necessárias.

Os blocos de códigos em Python são marcados 

## 5 Variável

Como já falamos o Python tem tipagem forte e dinâmica de váriavel, não existe um local especifico para declarar as variáveis, você pode declarar no local que desejar. A única preocupação que você deve ter é não consultar uma variável que não existe. Se isso acontecer, um erro vai acontecer.

As variáveis podem ter nomes conforme a vontade do programador, com nomes longos, contendo letras e números. No entanto, elas devem necessariamente começar com 'letras minúsculas'.

Além dessa regra é importante também estar atento às palavras reservadas da linguagem, que não podem ser utilizadas como variáveis.

```bash
and       def       exec      if        not       return
assert    del       finally   import    or        try
break     elif      for       in        pass      while
class     else      from      is        print     yield
continue  except    global    lambda    raise
```

Para declarar um variável é muito, simples. Vamos criar uma variável com o nome `dados` e vamos 'armazenar' o valor inteiro 10.

```python
dados=10
```
Perceba que em nenhum momento foi citado que a variável dados é do tipo inteiro. A linguagem automáticamente faz isso.

Atribuição também pode ser realizado em cadeia, conforme o exemplo:

```python
dados=x=filho=10
```

Outra forma de realizar atribuição em cadeia:

```python
nome,idade,tel = 'jose',10,'56945-2342'

# Imprimir o conteúdo da variável
print(nome)
print(idade)
print(tel)
```

## 6 Estrutura de Dados
Podemos estrutura os dados em Python com variáveis em do tipo:
* String;
* Number (Integer e Float);
* Lista;
* Tuple;
* Dicionário;
* Boolean

### 6.1 String 
String é uma sequencia de caracteres Unicode. Para representar uma string pode ser utilizado aspas simples e aspa duplas.
Exemplo:
 ```python
texto="As vezes voce tem que levantar sozinho e seguir em frente"
```
Para declarar multiplas linhas utilize 3 aspas simple.
Exemplo:
   ```python
texto='''
     Tudo é possivel. 
     O impossível apenas demora mais
     '''
   ```
Semelhante a lista e Tuplas, as string também utilizam o operador [ ]. Dessa forma é possível obter apenas parte da string.
Exemplo:
```python
texto="As vezes voce tem que levantar sozinho e seguir em frente" 
# Recuperar o caractere da posição 5
print(texto[6])   # Retorno "e"
   
# Recuperar do inicio da string ate posição 10
print(texto[0:10])  # Retorno "As vezes v"
  
# Recuperar da posição 10 até a posição 15
print(texto[10:15]) # retorno "oce t"


```   
### 6.2 Numbers
Com python é possível utilizar 3 tipos de variável para números. São os Inteiros (int), Ponto Flutuante (float) e os números complexos (complex).
   
Não é necessário declarar os tipos que deseja utilizar, apenas declarar o conteúdo que o tipo automáticamente é alocado.
   
Exemplo:
     
> No exemplo abaixo utilizamos a função `type()` para mostrar o tipo da classe da variável. Também usamos a função `isinstance()` para verificar/comparar o tipo da váriavel. Se for o mesmo tipo ele retorno true.
  
```python
a = 5
print(a, "do tipo", type(a))

a = 2.0
print(a, "do tipo", type(a))

a = 1+2j
print(a, "numero complexo?", isinstance(1+2j,complex))
```
### 6.3 List
 Lista é Python é uma sequencia de item, equivale os array de outras linguagem. A lista é um dos tipos de dados mais utilizados em Python por ser muito flexivel.Todos os items de uma lista NÃO precisam ser do mesmo tipo.  
   
Exemplo:

```python 
lista=[10,60,'jose','45234234',50.9]
# Mostrando a lista
print("Conteudo da lista, lista)
```
Nas listas podemos utilizar o operador [ ]. Dessa forma podemos obter um elementro especifico da lista ou mostrar uma conjunto de elemento.

Exemplo:
```python
lista=[10,30,50,90,100,1,5,19]

# lista[2] = 50
print("lista[2] = ", lista[2])

# lista[0:3] = [10, 30, 50]
print("lista[0:3] = ", lista[0:3])

# lista[5:] = [1, 5, 19]
print("lista[5:] = ", lista[5:])
```
A lista podem ser alteradas.
```python
a = [1,2,3]
a[2]=4

# [1, 2, 4]
print(a)
```
### 6.4 Tuple
As tuple são uma sequencia de itens, semelhante a uma lista. A diferença que a tuples são imultavél. Uma vez que a tupla são criadas,não podem ser modificadas.

As tuplas são usadas para dados que são protegidas contra gravação e por não serem modificadas dinamicamente, elas são usualmente mais rapidas que as listas. 

Exemplo:
```python
t = (10,40,'jose','maria',6.5)

print(t[1])
```
### 6.5 Dictionary
Dicionário são estrutura de dados com um par conhecido como `chave/valor`. 

Geralmente é usado quando temos uma quantidade enorme de dados. Os dicionários são otimizados para recuperar dados. Nós devemos conhecer a chave para recuperar o valor.

No Python, os dicionários são definidos entre chaves {}, sendo cada item um par na chave do formulário: valor. Chave e valor podem ser de qualquer tipo de variável.

```python
login = {"user": "jose","passwd":"okri"}

print("Tipo", type(login))

#Recuperando o valor
print(login['uesr']

#Recuperando o valor
print(login['passwd'])
```
Usamos a chave para recuperar o valor. Mas o contrário não funciona.

### 6.6 Set
Set é uma coleção não ordenada de itens exclusivos (não pode ter itens repetidos). Set é definido por valores separados por vírgula entre chaves {}.

Podemos realizar operações de conjunto como união, interseção em dois conjuntos. Conjunto tem valores exclusivos. Eles eliminam duplicatas.

Como o conjunto é uma coleção não ordenada, a indexação não funciona. Portanto, o operador [ ] não funciona.
```python
posicao_chegada={3,4,1,7,8}
print(posicao_chegada)
```
### 6.7 frozenset
Frozen set são conjuntos similares ao set. A diferença que frozenset são imutável, portanto não podem ser modificados. Devido a isso, podem ser usados como chave no dicionário ou como elemento de outro conjunto. Mas como conjuntos, não é ordenado (os elementos podem ser definidos em qualquer índice).
```python
lisya = ('a', 'e', 'i', 'o', 'u')

fSet = frozenset(vowels)
print('O frozen set é:', fSet)
print('UM set vazio:', frozenset())
```
Um outro exemplo:

```python
# random dictionary
person = {"name": "John", "age": 23, "sex": "male"}

fSet = frozenset(person)
print('The frozen set is:', fSet)
```
### 6.8 Boolean
O tipo de dados Boolean em Python são criados pela classe `bool` que logicamente aceita 2 valores constante `True` e `False`.

```python
print(type(True))
```
Os booleanos também podem ser presentados por inteiros sendo 1 para `True`e 0 para `False`.

### 6.9 Conversão entre tipos
Nós podmeos converter entre diferentes tipo de dados usando diferentes funções de conversão semelhante a `int()`, `float()`, `str()`...etc.

| Descrição| Função | Exemplo |
|----------|-----------|-----|
| Converte para intero.|  int(x) | num=int(a)|
| Converte para float.|float(x) |num = float(a) |
| Converte para número Complexos|complex(x) |num = complex(a)  |
| Converte para String |str(x) | letra = str(num)  |
| Converte para uma tuple|tuple(s) |t_lista = tuple(lista) |
| Converte para Lista.|list(s) |lista = list(a) |
| Converte para Set.|set(s) | l = set(lista) |
| Converte um set em frozenset.| frozenset(s) |frozenset(x) |
| Converte um número em um string da tabela ascii.|chr(x) | chr(95) |
| Converte uma string em um valor da tabela ascii.| ord(x) | ord('a') |
| Converte para Hexdecimal.| hex(x) |h=hex(10) |
| Converte uma string para um Inteiro octal| oct(x) | oct(10)|


## 7 Operadores
Vamos começar pelos operadores matemáticos, igualmente as outras linguagem de programação, as operações básicas de matemáticas são realizadas pelos operadores `+`, `-`, `/` e `*`. 

| Descrição     | Operador |
|---------------|----------|
| adição	       | +        |
| subtração	    | -        |
| multiplicação	| *        |
| divisão	      | /        |

A utilização é bem simples.

```python
soma = 10 + 5
```
Python também segue as precedência definida pela Matemática, porém sempre recomendamos utilizar parentes `( )` para separar os operadores, para tornar mais legível.
Por exemplo:

```python 
result = 2+2*2   # Resultado 6
#dessa forma fica mais ligivel
result = (2+2)*2 # Resultado 8
```
Com os operadores básicos podemos acrescentar os operadores que fazem operação e atribuição.

| Descrição | Operador    |
|-----------|------------|
| soma e atribui         | +=       |
| subtrai e atribui      | -=       |
| dividi e atribui       | \*=       |
| multiplica e atribui   | /=       | 

Exemplo:
```python
a=10
a = a + 10 
a += 10
```
Além dos operadores básicos, também temos os operadores para exponenciação, extração do módulo da divisão, parte inteira de uma divisão.

|Descrição	|Operador|
|--------|-------|
|exponenciação	|**|
|parte inteira	|//|
|módulo|	%|

A sintaxe para utilização desses operadores.

```python
result = 2 ** 2  # resutado  2
result = 5 // 2  # resultado 2
result = 5 %  2  # resultado 1
```
Esses operadores que vimos também podem ser utilizados com outras estrutura de dados tais como string e list.
Um exemplo de utilização com string:

```python
result = "-"*50   
result = "Ola" + "Mundo"
```
Operadores com Lista:
```python
 lista = [1,2,3] * 10
 todos_numeros = [2,4,6,8] + [1,3,5,7] 
```
Além dos operadores matemáticos, também tempos os operadores lógicos que retornar `True` e `False`.

|Descrição	|Operador|
|----------|--------|
|Maior que	|>|
|Menor que	|<|
|Igual a	|==|
|Maior ou igual a	|>=|
|Menor ou igual a	|<=|
| Conjunção e    |  and |
| Disjunção ou   | or |
| negação        | not |

A utilização dos operadores lógicos também é bem simples. Eles não muito utilizados para tomada de decisão em `IF`.
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

Utilizamos muito operador `in` para verificar se um valor está em uma lista.
```python
x = 10 in [3,4,5,10]   | Retorna True
```
Já operdor `is` é para testar a identidade de um objetivo. Verificar se realmente o mesmo objeto.
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
E para finalizar vamos estudar os operadores binários. 

| Descrição | Operador|
|-----------|---------|
| OU binário     |   \|   |
| OU exclusivo          |   ^     |
| E Binário          |    &   |
| Desloca bit a direita         |  >>       |
| Desloca bit a esquerda          |  <<     |
|   Complemento        |  ~x     |

Exemplo de utilização dos operadores binários.
```python
a = int("1100100",2)
print(a)
print(a << 1)
print(a >> 1)
```
## 8 Controle de Fluxo

O controle de fluxo de dados no Python podem ser realizado utilizado desvio no fluxo de código ou através de sistema de repetição.

* __IF__

No desvio de fluxo, utilizamos o comando `IF`. A sintaxe é a seguinte:

```python
if (expressão):
   pass
elif (expressão):
   pass
else:
   pass
```

Como exemplo, vamos fazer uma entrada de dados via input, vamos transformar em inteiro e realizar as comparações. Se a condição da expressão foi `True`, bloco de código vai ser realizado.

```python
x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Valor negativo')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Apenas UM')
else:
    print('Muitos')
```   


* __For__

Além do desvio de fluxo, podemos repetir um pedaço de código. No python podemos utilizar o `for`ou `while`.

O `for` pode utilizar como controle de repetição uma lista. No exemplo a seguir, temos uma lista de palavaras `words`, e a cada interação (passagem pelo loop), uma palavra é atribuida a variável `w`. O len retorna o tamanho da palavra.

```python
words = ['gato', 'cachorro', 'coelho']
for w in words:
    print(w, len(w))
```
Caso não tenha uma lista de 'coisas', uma nova lista de números pode ser criada utilizando a função `range`. Por exemplo, se você precise gerar uma lista de números de 0 até 5 `range(5)`

```python
for i in range(5):
    print(i)
```
A sintaxe do `range` é a seguinte:

```python
range(inicio, fim, pulo)
```
Caso um valor apenas seja declarado no `range(100)`, é considerado como fim e o inicio começa de zero. Se dois valores são declarados `range(4,9)`, são considerados como inicio e fim respectivamente. Se treis valores são declarados `range(0,100,4)`, teremos o inicio, fim e o número de pulos (step). A interação pode dar pulos de 1 em 1 (padrão) ou você pode definir.

Exemplos:
```
range(5, 10)
   5, 6, 7, 8, 9

range(0, 10, 3)
   0, 3, 6, 9

range(-10, -100, -30)
  -10, -40, -70
```

* __While__

Como conforma de loop também temos o `while`. Com o `while` não possui uma lista, portanto não é possível saber a quantidade de vezes que o fluxo do programa vai ficar no `while. O fluxo vai ficar no `while` até a condição for `False`.

Sintaxe:
```
 while condição:
    pass
 else:
    pass
```
Como exemplo, vamos repetir um bloco de código enquanto o valor de x seja menor do que 10. Caso a expressão ( x < 10) retorne False, o bloco de código dentro do else pode ser executado. 

```python
x= 0

while x < 10:
    print('Numero',x)
    x += 1

else:
   print('Finalizado')
```   

No caso anterior, sabiamos por dedução a quantidade de vezes que o programa iria executadar. Em muitos casos isso não é possível. Por exemplo, podemos fazer um programa para ler um valor, armazenar na lista. E para o sistema parar de ler um novo valor, o usuário tem que digitar `fim`.

```python
x = 'incio'
lista = []
while x.lower() != 'fim':
    x = input("Digite o proximo nome:")
    lista.append(x)

print(lista)
```

* __break, continue e else para usar com o loop__

A instrução `break`, como em C, são interno para `for` ou `while` e quando invocado finaliza de forma bruta o loop.

As instruções de loop podem ter uma cláusula else; ele é executado quando o loop termina por esgotamento da lista (com for) ou quando a condição se torna falsa (com while), mas não quando o loop é finalizado por uma instrução `break`. Isso é exemplificado pelo seguinte loop, que procura por números primos:

```python
for n in range(2, 10):
     for x in range(2, n):
         if n % x == 0:
            print(n, 'igual', x, '*', n//x)
            break
     else:
         print(n, 'eh numero primor')
```

O `break`  sempre finaliza o loop e não executa o `else`, já o `continue` finaliza aquela parte do bloco de código e volta para o inicio do loop. 
```python
nomes=['maria','jose','carlos','eduardo']

for nome in nomes:
    if nome == 'jose':
        continue
    print(nome)
   
```
No exemplo, o nome 'jose' não vai ser mostrado porque ele está dentro de um `if` com `continue`.

## 9 Outras funções
Para o desenvolvimento do laboratório  e da lista de exercício, vamos precisar conhecer as seguintes funções:
* print

O print como já vimos em vários exemplos, é utilizado para imprimir (mostrar) algo na tela.

Vamos aprender com esses exemplos:

```python
# declarar variavel
nome, idade, salario ="jose",30, 100.00

# imprimendo texto
print("Inicio do programa")

# imprimindo apenas variável
print(nome)

# Imprime string com variável
print("Usuario:",nome)

# Imprime string com variável
print("O usuario:"+ nome)

# Usando o format
print("O usuario {0} tem {1:d} idade".format(nome, idade))

# Usando format com float
print("salario {0:0.2f} l".format(salario))

# alinha a direita com 20 espaços em branco
print("{0:>20}".format(nome))

# alinha a direita com 20 símbolos -
print("{0:->20}".format(nome))

# alinha ao centro usando 10 espaços em branco a esquerda e 10 a direita
print("{0:^20}".format(nome))

# imprime só as primeiras cinco letras
print("{0:.3}".format(nome))

#Imprime em hexdecimaç
print("{0:x}".format(23))

#Imprime em binário
print("{0:b}".format(123)) 
```

* split
A função `split` utiliza um padrão para 'quebrar' uma string e gerar uma lista. 

Como exemplo, vamos utilizar as seguinte string:

```
texto =  "jose:30anos:rua de baixo:sp"
```
Perceba que temos um delimitador na variável que é o ":". Podemos utilizar esse delimitador para quebrar a string em uma lista.

```python
lista = texto.split(":")  # ['jose','30anos','rua de baixo','sp']
print(lista[0])           # imprimir o nome
```
Qualquer caractere pode ser o delimitador.

## 10 Laboratório
No link abaixo temos o laboratório dirigido, faça o laboratório para práticar os conhecimentos apreendidos
> [Laboratório](https://github.com/clodonil/curso_python/tree/master/modulo1/Labs)

## 11 Lista de Exercício <span id="p11"></span>
Após realizar o laboratório e brincar com os códigos, teste o seu conhecimento com a lista de exercicio:
> [Lista de Exercício](exercicios/README.md)

***
> By:
```python
Autor   = ['Clodonil Honorio Trigo','clodonil@nisled.org']
linkdin = 'https://www.linkedin.com/in/clodonil-trigo-4155722a'
Blog    = 'http://www.devops-sys.com.br'
```

