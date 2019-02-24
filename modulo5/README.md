# Desenvolvimento WEB

 

Entre os frameworks em Python para desenvolvimento Web, podemos citar como principais:

 

* Django

* Flask

* Pyramid

 

Vamos utilizar o Flask basicamente pela simplicidade e flexibilidade na construção do escopo de desenvolvimento.

 

Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions. And before you ask: It's BSD licensed!

 

A ideia de microframework do Flask, vem em função de que é possível criar uma aplicação web em apenas um arquivo.

Com isso também temos que o framework cuida apenas  do que é estritamente importante.  Por exemplo, driver de conexão com o banco de dados e outras libs não estão presentes por padrão no framework.

 

Além dessas premissas também é importante citar que o Flask não define como o seu projeto deve ser organizado, você como arquiteto da solução que define.

 

Antes de criarmos a nossa primeira aplicação, precisamos ter instalado o framework do `Flask` instalado.

 

```bash

$ pip install Flask

```

 

Agora podemos criar a nossa primeira aplicação que basicamente será um 'Hello Flask'.

Apesar de simples, é super importante esse primeiro código porque valida que tudo está preparado para o desenvolvimento.

 

```python

from flask import Flask

 

app = Flask(__name__)

 

@app.route("/")

def hello():

    return "Hello Flask!!!"

 

 

if __name__ == "__main__":

   app.run(host='0.0.0.0', debug=True, port=8080)     

```

 

Com pouco código temos uma aplicação web rodando. Vamos entender as principais linhas desse código:

 

1. Primeiramente importamos a classe do Flask. Uma instância dessa classe vamos utilizar em nossa aplicação;

2. Criamos uma instância da Classe Flask. O primeiro argumento é o nome da aplicação  ou pacote.

 

```

Next we create an instance of this class. The first argument is the name of the application’s module or package. If you are using a single module (as in this example), you should use __name__ because depending on if it’s started as application or imported as module the name will be different ('__main__' versus the actual import name). This is needed so that Flask knows where to look for templates, static files, and so on. For more information have a look at the Flask documentation.

```

 

3. Usamos *router()* para o FLask relacionar as URLs com as funções .

5. Usamos o `app.run` para iniciar aplicação em um IP e porta especifica. Também é possível o modo debug se o programa estiver em desenvolvimento.

 

 

 

## Statics

 

## Templates

 

## Debug Mode

 

 

## Sessions

 

 

## Logging

 

```python

app.logger.debug('A value for debugging')

app.logger.warning('A warning occurred (%d apples)', 42)

app.logger.error('An error occurred')

```

 

## Database
