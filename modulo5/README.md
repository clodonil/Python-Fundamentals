# Desenvolvimento WEB

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

Com pouco código, temos uma aplicação web rodando. Vamos entender as principais linhas desse código:

 1. Primeiramente importamos a classe do `Flask`. Uma instância dessa classe vamos utilizar em nossa aplicação;

 2. Criamos uma instância da Classe Flask. O primeiro argumento é o nome da aplicação ou pacote;

 4. Criamos um `endpoint` ou `router` de acesso que nesse caso é "/";

 5. Criamos o métodos para processar o `router` "/";

 6. Retornamos para o navegador a string `Hello Flask!!!`;

 8. Verifica a classe `main`está sendo executada;

 9. Inicializamos aplicação com o IP e porta necessário. O `debug=True` permite criar debug no navegador; 

 

```


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
