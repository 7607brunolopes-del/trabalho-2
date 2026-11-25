import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuração da Base de Dados (SQLite)
basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'guia.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from app import routes, models

# Cria as tabelas na base de dados (se ainda não existirem)
with app.app_context():
    db.create_all()
