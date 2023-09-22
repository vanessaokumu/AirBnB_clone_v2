#!/usr/bin/python3
from flask import Flask, escape

# Create a Flask application
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

# Define a route for "/python/<text>" with a default value of "is cool"
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    text = escape(text).replace('_', ' ')
    return "Python {}".format(text)

if __name__ == '__main__':
    # Run the Flask app on 0.0.0.0:5000
    app.run(host='0.0.0.0', port=5000)
