#!/usr/bin/python3
"""a script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000 """

from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Route for the root URL ("/")
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

# Disable strict slashes
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

if __name__ == '__main__':
    # Run on 0.0.0.0:5000
    app.run(host='0.0.0.0', port=5000)

