 __Python Fundamentals__ - Módulo 1
 ====================== 
 
## Objetivo
Capacitar estudantes com nenhum ou prévio conhecimento na linguagem Python a desenvolver aplicações ricas com acesso a banco de dados e interface WEB

## Conteúdo:
  > 1. [História](#historia)
  > 2. [Filosofia da Linguagem](#conceitodalinguagem)
  > 3. [Ambiente de Desenvolvimento](#ambientededesenvolvimento)
  > 4. [Sintaxe básica](#sintaxebasica)
  > 5. [Variável](#variavel)
  > 6. [Operadores](#operadores)
  > 7. [Controle de fluxo](#controlefluxo)
  > 8. [Estrutura de dados](#estruturadedados)
  > 9. [Laboratório](#laboratório)
  > 10.[lista Exercícios](#exercicio)


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

## 3 Ambiente de Desenvolvimento;
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
Outra possibilidade também é utilizar uma IDE que está na cloud. No meu ponto de vista a melhor delas é o [cloud9](https://c9.io/login). É só se cadastrar e sair usando.


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

### 5.2 Estrutura de Dados
Podemos estrutura os dados em Python com variáveis em do tipo:
* String;
* Number (Integer e Float);
* Lista;
* Tuple;
* Dicionário;

#### 5.2.1 String 
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
texto[6]   # Retorno "z"
   
# Recuperar do inicio da string ate posição 10
texto[0:10]  # Retorno "As vezes vo"
  
# Recuperar da posição 10 até a posição 15
texto[10:15] # retorno "
```   
#### 5.2.2 Numbers
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
#### 5.2.3 List
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
#### 5.2.4 Tuple
As tuple são uma sequencia de itens, semelhante a uma lista. A diferença que a tuples são imultavél. Uma vez que a tupla são criadas,não podem ser modificadas.

As tuplas são usadas para dados que são protegidas contra gravação e por não serem modificadas dinamicamente, elas são usualmente mais rapidas que as listas. 

Exemplo:
```python
t = (10,40,'jose','maria',6.5)

print(t[1])
```
#### 5.2.5 Dictionary
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

#### 5.2.6 Set
Set é uma coleção não ordenada de itens exclusivos (não pode ter itens repetidos). Set é definido por valores separados por vírgula entre chaves {}.

Podemos realizar operações de conjunto como união, interseção em dois conjuntos. Conjunto tem valores exclusivos. Eles eliminam duplicatas.

Como o conjunto é uma coleção não ordenada, a indexação não funciona. Portanto, o operador [ ] não funciona.
```python
posicao_chegada={3,4,1,7,8}
print(posicao_chegada)
```
#### 5.2.7 frozenset
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
#### 5.2.7 Conversão entre tipos
Nós podmeos converter entre diferentes tipo de dados usando diferentes funções de conversão semelhante a `int()`, `float()`, `str()`...etc.

| Descrição| Função | Exemplo |
|----------|-----------|-----|
| Converte para intero.|  int(x) | num=int(a)|
| Converte para float.|float(x) |num = float(a) |
| Converte para número Complexos|complex(x) |num = complex(a)  |
| Converte para String |str(x) | letra = str(num)  |
| Converts object x to an expression string.|repr(x) | |
| Evaluates a string and returns an object.|eval(str) | |
| Converte para uma tuple|tuple(s) |t_lista = tuple(lista) |
| Converte para Lista.|list(s) |lista = list(a) |
| Converte para Set.|set(s) | l = set(lista) |
| Converte um set em frozenset.| frozenset(s) |frozenset(x) |
| Converte um número em um string da tabela ascii.|chr(x) | chr(95) |
| Converte uma string em um valor da tabela ascii.| ord(x) | ord('a') |
| Converte para Hexdecimal.| hex(x) |h=hex(10) |
| Converte uma string para um Inteiro octal| oct(x) | oct(10)|


## 5.3 Operadores
fdsfsdf
| Operação | Operador |
|----------|---------|
|adição	| + |
|subtração	| - |
|multiplicação	| * |
|divisão	| / |


## 5.3 Controle de Fluxo
O controle de fluxo de dados no Python podem ser realizado utilizado
If
```python
x=10
if x > 10:
    print("Maior que 10")
```   
* Case
* While
* For

* Until


## 6. Laboratório
No link abaixo temos o laboratório dirigido, faça o laboratório para práticar os conhecimentos apreendidos
> [Laboratório](https://github.com/clodonil/curso_python/tree/master/modulo1/Labs)

## 7. Lista de Exercício
Após realizar o laboratório e brincar com os códigos, teste o seu conhecimento com a lista de exercicio:
> [Lista de Exercício](exercicios/README.md)

***
> By:
```python
Autor   = ['Clodonil Honorio Trigo','clodonil@nisled.org']
linkdin = 'https://www.linkedin.com/in/clodonil-trigo-4155722a'
Blog    = 'http://www.devops-sys.com.br'
```
