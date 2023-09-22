#!/usr/bin/python3
from flask import Flask, escape

app = Flask(__name__)

# Define a route for the root URL ("/") 
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

# Define a route for "/hbnb" 
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

# Define a route for "/c/<text>"
@app.route('/c/<text>', strict_slashes=False)
def c(text):
    text = escape(text).replace('_', ' ')
    return "C {}".format(text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
