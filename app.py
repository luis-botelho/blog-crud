from flask import Flask, render_template, redirect, request, session, flash
from flask_mail import Mail, Message 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)