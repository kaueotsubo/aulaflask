from projeto import app
from flask import render_template

@app.route('/')
def homepage():
    return 'Pagína inicial, para acessar as outras pagínas criadas digitar as proximas URL: <br>  <br> /sobre <br>  /linkinpark <br>  /spliknot <br> /nossahistoria <br>  /contato <br> /ghost'

@app.route('/sobre/')
def sobre():
    return render_template('sobre.html')

@app.route('/linkinpark/')
def park():
    return render_template('park.html')

@app.route('/spliknot/')
def knot():
    return render_template('knot.html')

@app.route('/ghost/')
def ghost():
    return render_template('ghost.html')

@app.route('/nossahistoria/')
def nossahistoria():
    return 'Alvaro nos ensinou como usa o flask'

@app.route('/contato/')
def contato():
    return 'Kauê numero: +215 (99) 99909-9876'
