'''
classe: m5_lab2
descricao: Construa uma aplicação WEB que mostra uma tabela com cadastro do deputado (Foto, Id,Nome, Estado e Partido) 
autor: Clodonil Honorio Trigo
email: clodonil@nisled.org
data: 09 de maio de 2019
'''
from flask import Flask, render_template
from lib import DadosAbertos

app = Flask(__name__)



@app.route("/")
def deputados():
   obj = DadosAbertos()
   list_dep = obj.deputados()

   partidos = {}

   for dep in list_dep:
       partido = dep['siglaPartido']
       if partido in partidos:
             partidos[partido] += 1
       else:
          partidos[partido] =  1
      
   bar_labels=partidos.keys()
   bar_values=partidos.values()

   return render_template('index.html', max=100, labels=bar_labels, values=bar_values)

if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=True, port=8080)
