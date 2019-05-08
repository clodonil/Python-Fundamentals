from flask import Flask,Blueprint, render_template

ecommerce = Blueprint('ecommerce',__name__)

@ecommerce.route('/')
def vendas():
    
    return render_template('venda/index.html')