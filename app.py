from flask import Flask, render_template, request

app = Flask(__name__)

from views import *

if __name__ == '__main__':
    app.run(debug=True)