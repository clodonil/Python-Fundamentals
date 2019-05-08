from flask import Flask,Blueprint, render_template

product = Blueprint('product',__name__)

@product.route('/')
def produto():
    
    return render_template('produto/index.html')
