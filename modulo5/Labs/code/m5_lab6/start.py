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

   return render_template('lista.html', listas=list_dep)

@app.route("/gastos/<id>")
def deputado(id):
   obj    = DadosAbertos()
   info   = obj.deputado_id(id)
   gastos = obj.deputado_despesas(id)

   valores = {}
   for gasto in gastos:
       data = str(gasto['mes']) + '/' + str(gasto['ano'])

       if data in valores:
          valores[data] += gasto['valorLiquido']    
       else:
          valores[data] = gasto['valorLiquido']   
       
   line_labels = valores.keys()
   line_values = valores.values()

   return render_template('gastos.html', title='Gráfico de Gastos', max=10000, labels=line_labels, values=line_values)


if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=True, port=8080)
