#!/usr/bin/python3

#!/usr/bin/python3
"""a script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000"""

from flask import Flask

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

# Route to display "C " followed by the value of the text variable
@app.route('/c/<text>', strict_slashes=False)
def c(text):
    text = text.replace('_', ' ')
    return "C {}".format(text)

# Run the Flask app on 0.0.0.0, port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
