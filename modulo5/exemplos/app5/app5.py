from flask import Flask, session, redirect, url_for, escape, request

app = Flask(__name__)

app.secret_key = b'i\x85%@Il,OB\x13@^6\xb2u{'

@app.route('/')
def index():
    if 'username' in session:
        return 'Usuario logado, %s' % escape(session['username'])
    return 'Você não está logado'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p>Nome:<input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=True, port=8080)