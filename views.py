from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template("homepage.html")

@app.route('/blog')
def blog():
    return "Bem vindo ao blog"