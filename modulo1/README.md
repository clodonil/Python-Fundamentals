# Módulo 1  - Python Fundamentals

## Objetivo
Capacitar estudantes com nenhum ou prévio conhecimento na linguagem Python a desenvolver aplicações ricas com acesso a banco de dados e interface WEB

## Conteúdo:
   - [História](#historia)
   - [Conceitos da Linguagem](#conceitodalinguagem)
   - [Ambiente de Desenvolvimento](#ambientededesenvolvimento)
   - [Sintaxe básica](#sintaxebasica)
   - [Variável](#variavel)
   - [Operadores](#operadores)
   - [Controle de fluxo](#controlefluxo)
   - [Estrutura de dados](#estruturadedados)


## História
No Brasil em 1989, Collor de Melo vencia a primeira eleição direta, na Alemanha caia o muro de Belim e na Holanda o Guido Van Rossum criava a linguagem Python.

A história da linguagem é fantástica e seu aprendizado vai se tornar mais divertido após tomar conhecimento de alguns eventos que aconteceram.

Não vou escrever sobre a história do Python porque já tem muita coisa boa escrita, segue alguns links que vale a pena ler:

* [http://mindbending.org/pt/a-historia-do-python](http://mindbending.org/pt/a-historia-do-python)
* [https://www.python-course.eu/python3_history_and_philosophy.php](https://www.python-course.eu/python3_history_and_philosophy.php)
* [https://wiki.python.org.br/HistoriaDoPython](https://wiki.python.org.br/HistoriaDoPython)

## Conceitos da Linguagem
## Ambiente de Desenvolvimento;
## Sintaxe básica
## Variável
```python
   dados=10
```
Atribuição em cadeia
```python
   dados=x=filho=10
```
### Escopo de Variável
### Estrutura de Dados
   #### String 
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
   
   String is sequence of Unicode characters. We can use single quotes or double quotes to represent strings. Multi-line strings can be denoted using triple quotes, ''' or """.
   #### Numbers
   #### List
   #### Tuple
   #### Dictionary
   #### Conversão entre tipos

## Operadores
## Controle de Fluxo
O controle de fluxo de dados no Python podem ser realizado utilizado
If
```python
x=10
if x > 10:
    print("Maior que 10")
```   
Case
While
For
Until

