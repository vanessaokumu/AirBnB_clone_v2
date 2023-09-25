#!/usr/bin/python3
"""
a script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)

# Define a method to handle teardown_appcontext
@app.teardown_appcontext
def teardown_db(exception):
    storage.close()

# Route to display a list of states
@app.route('/states', strict_slashes=False)
def states():
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('states.html', states=sorted_states)

# Route to display cities of a specific state
@app.route('/states/<id>', strict_slashes=False)
def state_cities(id):
    state = storage.get(State, id)
    if state:
        return render_template('state_cities.html', state=state)
    else:
        return render_template('not_found.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
