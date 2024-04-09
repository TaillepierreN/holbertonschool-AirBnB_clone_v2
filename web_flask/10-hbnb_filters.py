#!/usr/bin/python3
""" Start a Flask web app"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def shutdown(exception):
    """close the storage after each requests"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """return list of states and amenities"""
    temp = storage.all(State)
    states = []
    for elem in temp:
        states.append(temp[elem])

    temp = storage.all(Amenity)
    amenities = []
    for elem in temp:
        amenities.append(temp[elem])

    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


if __name__ == '__main__':
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
