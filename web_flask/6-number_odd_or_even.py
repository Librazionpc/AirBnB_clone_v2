#!/usr/bin/python3
"""Write a script that starts a Flask web application
"""
from os import name
from flask import Flask, render_template
from numpy import number

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


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text):
    """Returns the foormatedd text along sice with python when called"""
    underscore_to_space = text.replace('_', ' ')
    return "Python {}".format(underscore_to_space)


@app.route('/number/<int:n>', strict_slashes=False)
def is_it_a_number(n):
    """Return the formated integer when called"""
    return " {} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_templates(n):
    """Return formated html page"""
    return render_template('5-number.html', number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def Odd_or_even(n):
    """Return formated html page"""
    if (n % 2) == 0:
        parity = "is even"
    else:
        parity = "is odd"
    return render_template("6-number_odd_or_even.html", number=n,
                           parity=parity)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
