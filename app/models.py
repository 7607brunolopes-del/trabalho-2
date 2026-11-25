from app import db


class Restaurante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    zona = db.Column(db.String(100), nullable=False)
    especialidade = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.String(20), nullable=False)  # Barato, Médio, Caro


class Local(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    zona = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(100), nullable=False)  # Museu, Monumento, Jardim...
    preco = db.Column(db.String(20), nullable=False)  # Gratuito, Barato, Médio, Caro
