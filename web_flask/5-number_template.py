#!/usr/bin/python3
""" Start a Flask web app"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """display "Hello HBNB!" """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display "HBNB" """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """display C followed by the value of the text variable"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """display python followed by value of the text variable
    text default = "is cool"
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ display "<n> is a number" if n is int"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    """ Main Function """
    app.run(host='0.0.0.0', port='5000')
