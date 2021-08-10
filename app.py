from flask import Flask, render_template, redirect, request, session, flash
from flask_mail import Mail, Message 
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://vavfnbof:Y8MjLf3KIuAZs-lycEKXP1l-1FBCgUkv@kesavan.db.elephantsql.com/vavfnbof'
app.secret_key = 'blug'

class Artigo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    titulo = db.Column(db.String(50), nullable=False)
    artigo = db.Column(db.String(500), nullable=False)
    autor = db.Column(db.String(50), nullable=False)
    def __init__(self, titulo, artigo, autor):
        self.titulo = titulo
        self.artigo = artigo
        self.autor = autor
        

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)