from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Olá, este é o sistema de catálogo de pneus!"

if __name__ == '__main__':
    app.run(debug=True)