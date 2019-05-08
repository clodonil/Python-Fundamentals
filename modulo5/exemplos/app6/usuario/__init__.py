from flask import Flask,Blueprint, render_template

user = Blueprint('user',__name__)

@user.route('/')
def usuario():
    
    return render_template('usuario/index.html')