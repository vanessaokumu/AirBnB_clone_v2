#!/usr/bin/python3
"""
a script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
"""
from flask import Flask, render_template

# Create a Flask application
app = Flask(__name__)

# Route to display "Hello HBNB!"
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

# Route to display "HBNB"
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

# Route to display "C ", followed by the value of the text variable
@app.route('/c/<text>', strict_slashes=False)
def c(text):
    text = text.replace('_', ' ')
    return "C {}".format(text)

# Route to display "Python ", followed by the value of the text variable
@app.route('/python/<text>', strict_slashes=False)
def python(text='is_cool'):
    text = text.replace('_', ' ')
    return "Python {}".format(text)

# Route to display "n is a number" only if n is an integer
@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    if isinstance(n, int):
        return "{} is a number".format(n)
    else:
        return "Not a valid number"

# Route to display an HTML page only if n is an integer
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    if isinstance(n, int):
        return render_template('number_template.html', number=n)
    else:
        return "Not a valid number"

# Run the Flask app on 0.0.0.0, port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
