from flask import Flask,Blueprint, render_template

auth = Blueprint('auth',__name__)

@auth.route('/')
@auth.route('/index.html')
def login():
    
    return render_template('autenticacao/index.html')
    1