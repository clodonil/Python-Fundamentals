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
       
   colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]

   obj = DadosAbertos()
   proposicoes = obj.proposicoes()
   

   dados = {} 
   for proposicao in proposicoes:
       partido = proposicao['siglaTipo']   
       if partido in dados:
          dados[partido] +=1   
       else:
          dados[partido] = 1   
   
   labels=dados.keys()
   values=dados.values()

   
   return render_template('index.html', title='Proposições X Partidos', max=100, set=zip(values, labels, colors))

if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=True, port=8080)
