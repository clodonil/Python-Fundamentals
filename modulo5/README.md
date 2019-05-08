__Python Fundamentals__ - Módulo 5
 ====================== 
 
## Objetivo

Apresentar o `framework` para desenvolvimento web em Pytonn (`Flask`). 

## Conteúdo:
> 1.  [Flask](#1-Flask)
> 2.  [Template](#2-Template)</br>
> 3.  [Static](#3-Static)</br>
> 4.  [Debug Mode](#4-Debug-Mode)</br>
> 5.  [Logging](#5-Logging)</br>
> 6.  [Sessions](#6-Sessions)</br>
> 9.  [Blueprint](#8-Blueprint) </br>
> 8.  [Database](#7-Database)</br>
> 9.  [Aplicação de Exemplo](#8-Aplicação-de-Exemplo)</br>
> 10. [Laboratório](#9-laboratório)
> 11. [Lista de Exercício](#10-lista-de-exercício)

## 1 Flask
Python é bastante versátil, com um conjunto de framework para diferente funções. Entre esses framework em Python, podemos destacar os seguintes para desenvolvimento Web:

* [Django](https://www.djangoproject.com/)
* [Flask](http://flask.pocoo.org/)
* [Pyramid](https://trypyramid.com/)

Nesse módulo, vamos utilizar o framework `Flask` devido a sua simplicidade e flexibilidade na construção do escopo de desenvolvimento.

O Flask é considerado um `microframework`, foi baseado no [Werkzeug](https://www.palletsprojects.com/p/werkzeug/) e [Jinja2](http://jinja.pocoo.org/docs/2.10/). utiliza a licença BSD.

A ideia de `microframework` do Flask, vem em função de que é possível criar uma aplicação web em apenas um arquivo. 

Com isso também temos que o framework cuida apenas  do que é estritamente importante. Por exemplo, `driver` de conexão com o banco de dados e outras `libs` não estão presentes por padrão no framework.

Além dessas premissas também é importante citar que o Flask não define como o seu projeto deve ser organizado, você como arquiteto da solução que define.

 Antes de criarmos a nossa primeira aplicação, precisamos ter instalado o framework do `Flask`.

```bash

$ pip install Flask

```

Agora podemos criar a nossa primeira aplicação que basicamente será um 'Hello Flask'.

Apesar de simples, é super importante esse primeiro código [app1](https://github.com/clodonil/Python-Fundamentals/tree/master/modulo5/exemplos/app1) porque valida que tudo está preparado para o desenvolvimento.

```python
from flask import Flask 
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Flask!!!"
 
if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=True, port=8080)
```
Com pouco código, temos uma aplicação web rodando. Vamos entender as principais linhas desse código:

 1. Primeiramente importamos a classe do `Flask`. Uma instância dessa classe vamos utilizar em nossa aplicação;
 2. Criamos uma instância da Classe Flask. O primeiro argumento é o nome da aplicação ou pacote;
 4. Criamos um *`endpoint`* ou *`router()`* de acesso que nesse caso é "/";
 5. Criamos o métodos para processar o *`router`*;
 6. Retornamos para o navegador a string `Hello Flask!!!`;
 8. Verifica a classe `main`está sendo executada;
 9. Usamos o `app.run` para iniciar aplicação em um IP e porta especifica. Também é possível o modo debug se o programa estiver em desenvolvimento.

## 2 Templates

Gerar HTML de dentro do Python não é uma tarefa legal e natural, é na verdade, bastante trabalhoso, porque você precisa fazer o HTML escapar no return da função. Por causa disso, o Flask configura o mecanismo do template [Jinja2](http://jinja.pocoo.org/docs/2.10/) para você automaticamente.

Para renderizar um template, você pode usar o método `render_template()`. Tudo o que você precisa fazer é fornecer o nome do template e as variáveis que deseja passar para o mecanismo de template como argumentos.

Para utilizar um template, podemos utilizar 2 casos:

1 Caso: Esse é o exemplo mais simples, temos aplicação em um único arquivo e os arquivos de template estão localizados no diretório templates no mesmo nível da aplicação. 

```
/application.py
/templates
    /hello.html
```

2 Caso: Esse exemplo é mais interessante porque trabalha com pacotes, sendo o arquivo `__init__.py` o principal para carregar os outros módulos.

```
/application
    /__init__.py
    /templates
        /hello.html
```

Como exemplo, vamos utilizar o 1 caso. O [app2](https://github.com/clodonil/Python-Fundamentals/tree/master/modulo5/exemplos/app2) cria 2 rotas, sendo a primeira é uma rota para o "/" e a segunda é passado um parâmetro que é passado para o template. 

```python
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
@app.route("/<name>")
def hello(name=None):
    return render_template('hello.html', name=name)
 
if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=True, port=8080)

```
O exemplo acima, `render_template`  chamada o arquivo `hello.html`, passando como parâmetro a variável `name`.
O template em jinja2 recebe a variável e manipula a variável.

```
<!doctype html>
<title>Hello from Flask</title>
{% if name %}
  <h1>Hello {{ name }}!</h1>
{% else %}
  <h1>Hello, World!</h1>
{% endif %}
```

## 3 Statics

Aplicações web dinâmicas também precisam de arquivos estáticos. Normalmente, é de onde vêm os arquivos CSS e JavaScript. Idealmente, o seu servidor web é configurado para trabalhar com servidores de CDN ( Delivery Network - Rede de Distribuição de Conteúdo) atendê-los por você, mas durante o desenvolvimento,o Flask também pode fazer isso.
Basta criar uma pasta chamada `static` no seu pacote ou ao lado do seu módulo e estará disponível em `/ static` no aplicativo.

Para gerar URLs para arquivos estáticos, use o nome especial do terminal 'static':

```python
url_for ('static', filename = 'style.css')
```
no exemplo do `hello.html`:

```html
 <link rel="stylesheet" media="screen" href="{{ url_for ('static', filename = 'style.css') }}"> 
```

O arquivo deve ser armazenado no sistema de arquivos como static/style.css.

Em nosso exemplo, o [app3](https://github.com/clodonil/Python-Fundamentals/tree/master/modulo5/exemplos/app3) agora temos os arquivos estáticos.

```
/application.py
/static
    /style.css
/templates
    /hello.html
```

## 4 Debug Mode

Durante o desenvolvimento é bastante interessante habilitar o modo `debug` para encontrar erros e soluciona-lós de forma mais rápida.

Além de mostrar os erros de forma mais amigável, possibilita que os códigos salvos sejam automaticamente recarregado.

Para habilitar o `debug` ative o `True` na inicialização da aplicação.

```
app.run(host='0.0.0.0', debug=True, port=8080)
```
Durante a execução em modo `debug`, o console disponibiliza um `token`.

![cmd](https://github.com/clodonil/Python-Fundamentals/blob/master/Imagens/debug.png)

Com o `token` deve ser utilizado no browser para depurar os erros.

![browser](https://github.com/clodonil/Python-Fundamentals/blob/master/Imagens/browser.png)
 
## 5 Logging

Muitas vezes durante é necessário o lancamento de marcação para `debug`, `warning` ou `error`.

Para esses casos podemos utilizar em nossa aplicação a chamada `app.logger` conforme o exemplo abaixo.

```python
app.logger.debug('A value for debugging')
app.logger.warning('A warning occurred (%d apples)', 42)
app.logger.error('An error occurred')
```

## 6 Sessions

Ao contrário de um cookie, os dados da sessão são armazenados no servidor. Uma sessão de usuário é o intervalo de tempo em que um cliente efetua login em um servidor até efetua logout. Os dados, que precisam ser mantidos nessa sessão, são armazenados em um diretório temporário no servidor.

Uma sessão com cada cliente recebe um ID de sessão. Os dados da sessão são armazenados em cima dos cookies e o servidor os registra criptograficamente. Para essa criptografia, um aplicativo Flask precisa de um `SECRET_KEY` definido.

O objeto de sessão também é um objeto de dicionário que contém pares de valor-chave de variáveis de sessão e valores associados.

Por exemplo, para definir uma variável de sessão "username", use a instrução:

```
session["username"] = "admin"
```

Para liberar uma variável de sessão, use o método pop ().

```
session.pop ('username', None)
```
A seguir, um exemplo [app5](exemplo/app5/app5.py) de utilização de sessão, durante o login de um usuário.

O campo `app.secret_key` deve conter uma string complexa suficiente para servir de chave.
Uma forma de gerar essa chave pode ser feito da seguinte forma:

```python
python -c 'import os; print(os.urandom(16))'
b'i\x85%@Il,OB\x13@^6\xb2u{'
```
Nesse exemplo, as seguintes rotas são criadas:

| Routa| Descrição |
|------|-----------|
| /    | Verifica através da sessão se o usuário está logado          |
|/login| Formulário para login          |
|/logout| Logout, limpa a sessao          |


```python
from flask import Flask, session, redirect, url_for, escape, request

app = Flask(__name__)

app.secret_key = b'i\x85%@Il,OB\x13@^6\xb2u{'

@app.route('/')
def index():
    if 'username' in session:
        return 'Usuario logado, %s' % escape(session['username'])
    return 'Você não está logado'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))
```
Apesar da sessão guardar chave/valor, não devemos aguardar muita informação porque alguns navegadores tem limite para o tamanho da sessão.


## 7 Blueprint

O Flask como já mencionado não tem um padrão definido para desenvolvimento. Até o momento temos desenvolvido exemplo simples, que normalmente são suportados em apenas um arquivo.
Mas, no mundo real, pouquíssimos casos são aplicados nesse modelo. Normalmente desenvolvemos em módulos, separando o desenvolvimento em `features` e também em pequenos arquivos com finalidade especifica.

Para esses casos, o Flask disponibiliza o `Blueprint`. Com ele podemos desenvolver em módulos.

> Um módulo no python é um diretório com o arquivo __init__.py

Vamos utilizar como exemplo uma aplicação que deve ter os seguintes módulos:

- autenticacao
- usuarios
- produtos
- venda

Transpondo essa estrutura para o Flask, teremos os sequintes diretórios:

```
 / app.py
   /authenticao/__init__.py
   /usuario/__init__.py
   /produto/__init__.py
   /venda/__init__.py
   /templates
       /autenticacao/index.html
       /usuario/index.html
       /produto/index.html
       /venda/index.html
   /static
       /js
       /css
```

Antes do código em python, vamos entender como funciona essa estruturação.

1. O `app.py` é o arquivo principal, nele que são orquestrada as chamadas do módulos;
2. Cada diretório virá um módulo (autenticacao,usuario,produto,venda), e o código desse módulo está localizado no arquivo __init__.py.
3. Utilizando o módelo MVC, os diretório dos módulos funciona como `controller` e o templates como `view`. 
4. Os templates dos módulos ficam dentro do diretório template separado pelo nome do módulo.
5. Os arquivos estáticos ficam dentro do diretório `static`;

Agora que conhecemos a estrutura do projeto, vamos começar a entrar nos detalhes do desenvolvimento, começando pelo arquivo `app.py`.


```
from flask import Flask, Blueprint

app = Flask(__name__)

# Importando os módulos
from autenticacao import auth
from usuario    import user
from produto    import product
from venda      import ecommerce  


# Registrando as rotas
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(product, url_prefix='/product')
app.register_blueprint(venda, url_prefix='/ecommerce')


if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=True, port=8080)

```

Os pontos importantes nesse arquivo são:

- Instânciar a variável app com o objeto Flask `app=Flask(__name__)`
- Importa os módulos `from autenticacao import auth`, o nome `auth` é o nome da rota definido dentro do módulos
- Registrar o blueprint com uma rota definida `app.register_blueprint(auth, url_prefix='/auth')`

Todo o código pode ser desenvolvido no módulo. Vamos utilizar como exemplo o módulo  `autenticacao`. Portanto dentro do arquivo `autenticacao/__init__.py` termos toda a regra de negócio desse módulo.

Dentro do módulo precisa definir o nome do registro do blueprint, que deve ser o mesmo definido no arquivo `app.py` na linha `pp.register_blueprint(auth, url_prefix='/auth')`.

```
from flask import Flask,Blueprint, render_template

# Registra o rota com o blueprint
auth = Blueprint('auth',__name__)

# Definie o nome da rotas para o módulo
# Portanto para acessar esse módulo pode ser chamado da seguinte forma:
# auth/ ou auth/index.html
@auth.route('/')
@auth.route('/index.html')
def login():
    return render_template('autenticacao/index.htm
```

Linhas importantes:

- Registra o blueprint `auth = Blueprint('auth',__name__)`.
- O nome do registro o blueprint deve ser o mesmo importado no arquivo app.py;
- Define duas rotas para o módulo autenticacao;
- Define o método para desenvolvimento `def login()`; 
- Chama o template definido o diretório do módulo `return render_template('autenticacao/index.htm`

E para finalizar temos o arquivo de template `autenticacao/index.html` com um formulário html, bastante simples.

```
<h1> Login</h1>

<form>
    <p>Login</p>
    <p><input type=text name=username></p>
    <p>Password</p>
    <p><input type=password name=password></p>
    <p><input type=submit value=Login>
</form>
```

Os outros módulos seguem o mesma mecânica, e o código completo pode ser obtico [aqui](exemplos/app6/). 

Muitos projetos utilizarm esse modelo de organização de código, entretanto existe outras formas, e o blueprint é flexível para permitir as mudança necessárias.

Por exemplo, essa mesmo projeto poderia ser organizado dessa forma, sendo o módulo contendo todos os outros arquivos:

```
 / app.py
   /authenticao/
       __init__.py
      /templates
         /index.html
   /usuario/
      __init__.py
      /templates
         /index.html      
   /produto/
      __init__.py
      /templates
         /index.html      
   /venda/
      __init__.py
      /templates
         /index.html      
   /static
       /js
       /css
```


## 8 Database


## 9 Aplicação de Exemplo

Para melhorar a compreensão do desenvolvimento web em Python, recomendo fazer o exercício abaixo. Nele é construído uma aplicação de cadastro de tarefas.

- [Jornada do Code em Dev ao Deploy em AWS](https://github.com/clodonil/apptask)

## 10 Laboratório
No link abaixo temos o laboratório dirigido, faça o laboratório para práticar os conhecimentos apreendidos
> [Laboratório](Labs)

## 11 Lista de Exercício
Após realizar o laboratório e brincar com os códigos, teste o seu conhecimento com a lista de exercício:
> [Lista de Exercício](Exercicios)

***
> By:
```python
Autor   = ['Clodonil Honorio Trigo','clodonil@nisled.org']
linkdin = 'https://www.linkedin.com/in/clodonil-trigo-4155722a'
Blog    = 'http://www.devops-sys.com.br'
```
