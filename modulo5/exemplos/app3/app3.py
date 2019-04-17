from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
@app.route("/<name>")
def hello(name=None):
    
    return render_template('hello.html', name=name)
 
if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=True, port=8080)