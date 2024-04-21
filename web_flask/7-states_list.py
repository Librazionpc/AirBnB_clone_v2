#!/usr/bin/python3
"""Write a script that starts a Flask web application"""

from flask import Flask, jsonify, make_response, abort, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.teardown_appcontext
def teardown_app_context(exception):
    """Close the storage whjen called"""
    storage.close()

@app.route('/states_list', strict_slashes=False)
def states_list():
    """Returns the sorted list"""
    try:
        states = storage.all(State).values()
        sorted_states = sorted(states, key=lambda state: state.name)
        print(states)
        return render_template("7-states_list.html", states=sorted_states)
    except Exception as e:
        return f"An error occured: {str(e)}", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)