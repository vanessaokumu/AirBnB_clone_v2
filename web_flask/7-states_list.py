#!/usr/bin/python3
"""
a script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)

# Define a method to handle teardown_appcontext
@app.teardown_appcontext
def teardown_db(exception):
    storage.close()

# Route to display a list of states
@app.route('/states_list', strict_slashes=False)
def states_list():
    states = storage.all("State").values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
