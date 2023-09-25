#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) #Listening on port 5000
