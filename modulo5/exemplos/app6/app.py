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
app.register_blueprint(ecommerce, url_prefix='/ecommerce')


if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=True, port=8080)