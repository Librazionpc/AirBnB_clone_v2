#!/usr/bin/python3
"""Write a script that starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Returns Hello HBNB when the url is called"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_again():
    """Returns HBNB when the url is called"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """Returns the formated text along side the C when the url is called"""
    underscore_to_space = text.replace('_', ' ')
    return "C {}".format(underscore_to_space)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
