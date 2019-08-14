__Python Fundamentals__ - Módulo 3
 ====================== 
 
## Objetivo
Apresentar os vários estilos (paradigmas) de programação em Python, focando nos paradigmas estruturadas e OOP.

## Conteúdo:
> 1. [MultiParadigma](#1-MultiParadigma)</br>
> 2. [Estruturada](#2-Estruturada)</br>
> 2.1 [Escopo de Variável](#2.1-Escopo-de-Variável)</br>
> 3. [Orientado a Objeto](#3-Orientado-a-Objeto)</br>
> 3.1. [Classes](#3.1-Classes)</br>
> 3.2. [Encapsulamento](#3.2-Encapsulamento)</br>
> 3.3 [Herança](#3.3-Herança)</br>
> 4. [Laboratório](#4-laboratório)</br>
> 5. [Lista de Exercício](#5-lista-de-exercício)</br>

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

## 2. Estruturada

O desenvolvimento estruturada, também conhecida como [paradigma procedural](https://en.wikipedia.org/wiki/Procedural_programming), estrutura a execução através de rotinas estanques que são chamadas conforme a necessidade. Normalmente as chamamos de procedures/funções.


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

### 2.1 Escopo de Variável

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
Para finalizar o estudo do paradigma procedural, vamos exemplicar implementando um exemplo de estruturação de procedures para desenvolvimento de uma movimentação financeira.

Imagine que precisamos implementar a seguinte estrutura de dados:


**Procedures:**
```
criar_conta
deposito
saque
extrato
```

**Atributos da Conta:**
```
Numero da Conta
titular
Saldo
Limite
```
Vamos começar implementando o `criar_conta`, que vai receber como parâmetro o `Numero da Conta`,`titular`, `Saldo`,`limite` e cria a estrutura de dados como dicionário.

Salve os códigos abaixo no arquivo `banco.py`.

```python

def criar_conta(nconta, titular, saldo, limite):
   conta = {"nconta": nconta, "titular": titular, "saldo": saldo, "limite": limite}
   return conta

```
Para validar a implementação, abra o python em modo interativo e execute os comandos:

```bash
>>> from banco import criar_conta
>>> clodonil = criar_conta(123,'clodonil',100,500)
>>> clodonil['nconta']
123

```

> O mesmo procedimento pode ser feito para as outras procedures:

Agora vamos implementar a procedure para realizar o depósito na conta.

```python
def deposito(conta, valor): 
    conta ["saldo"] += valor
```    
Da mesma forma vamos implementar o módulo saque.

```python
def saque(conta,valor):
    conta["saldo"] -= valor
```
```
def extrato(conta):
    print("Sr(a) {0} o Saldo é {1}".format(conta["titular"],conta["saldo"]))
```
Agora que as procedures estão prontas, podemos importadas no programa principal e realizar as chamadas, conforme o exemplo a seguir:

```python
from banco import criar_conta, deposito, saque, extrato

conta_do_jose = criar_conta(3123,'Jose',50,1500)
deposito(conta_do_jose, 100)
extrato(conta_do_jose)
saque(conta_do_jose, 50)
```
>  Como sugestão, melhore as procedures para não realizar o saque além do limite, para criar contas apenas com saldo positivo.

## 3. Orientado a Objeto

O Paradigma [orientação a objetos](https://en.wikipedia.org/wiki/Object-oriented_programming)(OO), tem como proposta resolver problemas atráves de troca de mensagens entre `Objetos`, que são representações dos problemas atuais.

O modelo de OO é formado por quatro componentes básicos (`objeto`, `mensagem`, `método` e `classes`):

- **Objeto**: Um objeto consiste em um conjunto de operações encapsuladas (métodos) e um `estado` (determinado pelo valor dos atributos) que grava e recupera os efeitos destas operações. Um objeto tem determinadas propriedades que o caracterizam, e que são armazenadas no próprio objeto.  Objeto é uma instância de uma classe.

 - **Mensagem**: Mensagens são requisições enviadas de um objeto para outro, para que o objeto “receptor” forneça algum  resultado  desejado  através  da  execução  de  uma  operação.

 - **Métodos**: Métodos são similares a procedimentos e funções e consistem nas descrições das operações que um objeto  executa  quando  recebe  uma  mensagem.

 - **Atributos**: Um atributo consiste em um dado ou informação de estado, para o qual cada objeto de uma classe tem  seu  próprio  valor.  Existem  dois  tipos  de  atributos  em  um  sistema  orientado  a  objetos:  os  atributos  de objetos e os atributos de classes.

 - **Classes**: Uma classe é uma estrutura que abstrai um conjunto de objetos com características similares. Uma classe define o comportamento de seus objetos - através de métodos - e os estados possíveis destes objetos - através de atributos.

Entre as principais características da OOP, destaca-se a `reutilização de código` e a abstração dos detalhes dos  componentes  do  software.

Modelagem por objetos, vê o  mundo  como  uma  coletânea  de  objetos  que  interagem  entre  si,  apresentam  características próprias  que  são representadas pelos seus atributos (dados) e operações (processos).

### 3.1. Classes

Para entramos mais na prática, vamos utilizar o exemplo de `conta bancária` que utilizamos no estilo procedural. Nesse modelo podemos facilmente identificar o objeto `Conta`.

Antes de instânciar o objeto `Conta`, precisamos definir a classe que vai conter os atributos e métodos:

- Os métodos `deposito`, `saque` e `extrato`, basicamente ficaram igual, porém agora encapsulado dentro da classe.
- O método especial `__init__()` representa o construtor da classe e será executada somente quando a classe é criada;
- `Self` representa o endereçamento do objeto na mémoria, utilizado para acessar os atributos e métodos.


```python
# Arquivo: banco.py
class Conta:
    def __init__(self,nconta, titular, saldo, limite):
       print("Construindo objeto...")
       self.nconta = nconta
       self.titular = titular
       self.saldo = saldo
       self.limite = limite

    def deposito(self, valor):
       self.saldo += valor

    def saque(self, valor):
       self.saldo -= valor

    def extrato(self):
       print("Sr(a) {0} o Saldo eh {1}".format(self.titular,self.saldo))

```

Agora que temos a classe Conta, podemos criar vários objetos do tipo conta:

```bash
>> from banco import Conta
>>> x = Conta(12321,'Clodonil',100,200)
Construindo objeto...
>>> x
<banco.Conta object at 0x7f1ba4093d10>
>>> x.saldo
100
>>> x.deposito(100)
>>> x.saldo
200
>>> 
```
### 3.2. Encapsulamento

Com a chamada da classe, podemos criar um objeto e executar o método `deposito`, e acessar o atributo `saldo`. Os atributos estão públicos e podem ser acessados, entretanto nem sempre isso é desejado. No exemplo, o `saldo` deveria ser acessivel apenas pelos métodos.

Para isso, podemos deixar o atributo no modo privado, e para isso adicionamos `__` (underscore) antes do nome da variável. O mesmo conceito é valido para os métodos.

```python
class Conta:
    def __init__(self,nconta, titular, saldo, limite):
       print("Construindo objeto...")
       self.__nconta = nconta
       self.__titular = titular
       self.__saldo = saldo
       self.__limite = limite
```
A ação de tornar privado o acesso aos atributos, no mundo Orientado a Objetos, chamamos de encapsulamento. Com isso, definimos que o acesso deve ocorrer apenas por meio dos métodos.

Entretanto é comum o desenvolvimento implementar métodos para acessar os `getters` e `setter` para ter acesso ao atributo protegido.

Exemplo de implementação do `getters` diretamente:

```python

def get_titular():
    return self. __titular
```
No Python podemos utilizar a palavra reservada `@property` para implementar os get e set da melhor forma possível:

```python
@property
def saldo(self):
    return self.__saldo

@property
def titular(self):
    return self.__titular 

@property
def limite(self):
    return self.__limite

@limite.setter
def limite(self, limite):
    self.__limite = limite
```

### 3.3. Herança 
A Herança é um conceito do paradigma da orientação à objetos que determina que uma classe pode herdar atributos e métodos de uma outra classe e, assim, evitar que haja muita repetição de código.

Utilizando o exemplo da conta, vamos criar a classe de `Investimento`, herdando todos os métodos e atributos da classe `Conta`.

```python
class Conta:
    def __init__(self,nconta, titular, saldo, limite):
       print("Construindo objeto...")
       self.__nconta = nconta
       self.__titular = titular
       self.__saldo = saldo
       self.__limite = limite


    def deposito(self, valor):
       self.__saldo += valor

    def saque(self, valor):
       self.__saldo -= valor

    def extrato(self):
       print("Sr(a) {0} o Saldo eh {1}".format(self.__titular,self.__saldo))

    @property
    def saldo(self):
       return self.__saldo

    @property
    def titular(self):
       return self.__titular

    @property
    def limite(self):
       return self.__limite

    @limite.setter
    def limite(self, limite):
      self.__limite = limite

class Investimento(Conta):
    pass
```

Validando a implementação:

```bash
>>> from conta import Conta, Investimento
>>> maria = Investimento(1321,'Maria',100,200)
Construindo objeto...
>>> maria.titular
'Maria'
>>> maria.limite
200
```

No modelo de conta `Investimento`, precisamos do atributo de taxa de juros. Portanto vamos dar uma sobrecarga no método `__init__()` e instânciar o método `__init__()` da classe `Conta` usando o método `super()`.

```python
class Investimento(Conta):
    def __init__(self, nconta,titular, saldo, limite,juros):
      super().__init__(nconta, titular, saldo, limite)
      self.__juros = juros
      
```
Na conta investimento vamos implementar o método `rendimento()` que aplica a taxa de juros no saldo. Na classe `Conta`, os atributos estão privados, portanto precisamos mudar esse estado para as classes filhas acessarem os atributos. Por definição, mudamos os atributos para (_)(underscore).

```python
class Conta:
    def __init__(self,nconta, titular, saldo, limite):
       print("Construindo objeto...")
       self._nconta = nconta
       self._titular = titular
       self._saldo = saldo
       self._limite = limite

    def deposito(self, valor):
       self.__saldo += valor

    def saque(self, valor):
       self.__saldo -= valor

    def extrato(self):
       print("Sr(a) {0} o Saldo eh {1}".format(self.__titular,self.__saldo))

    @property
    def saldo(self):
       return self.__saldo

    @property
    def titular(self):
       return self.__titular

    @property
    def limite(self):
       return self.__limite

    @limite.setter
    def limite(self, limite):
      self.__limite = limite

class Investimento(Conta):
    def __init__(self, nconta,titular, saldo, limite, juros):
      super().__init__(nconta, titular, saldo, limite)
      self.__juros = juros

    def redimento(self):
        self._saldo += (self._saldo * self.__juros)
        return self._saldo
```

## 5. Laboratório
No link abaixo temos o laboratório dirigido, faça o laboratório para práticar os conhecimentos apreendidos
> [Laboratório](https://github.com/clodonil/curso_python/tree/master/modulo3/Labs/README.md)

## 4. Lista de Exercício
Após realizar o laboratório e brincar com os códigos, teste o seu conhecimento com a lista de exercicio:
> [Lista de Exercício](https://github.com/clodonil/curso_python/tree/master/modulo3/exercicios/README.md)

***
> By:
```python
Autor   = ['Clodonil Honorio Trigo','clodonil@nisled.org']
linkdin = 'https://www.linkedin.com/in/clodonil-trigo-4155722a'
Blog    = 'http://www.devops-sys.com.br'
```