#!/usr/bin/python3
from flask import Flask
""" Start a Flask web app """
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """display "Hello HBNB!" """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display "HBNB" """
    return "HBNB"


if __name__ == '__main__':
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
