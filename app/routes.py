from flask import render_template
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/locais')
def locais():
    return render_template('locais.html')

@app.route('/gastronomia')
def gastronomia():
    return render_template('gastronomia.html')