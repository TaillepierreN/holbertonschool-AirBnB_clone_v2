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
    amenities = storage.all(Amenity).values()
    states = storage.all(State).values()

    amenities = sorted(amenities, key=lambda x: x.name)
    states = sorted(states, key=lambda x: x.name)

    for state in states:
        if storage.__class__.__name__ == 'DBStorage':
            state.cities = sorted(state.cities, key=lambda x: x.name)
        else:
            state.cities = sorted(state.cities(), key=lambda x: x.name)
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


if __name__ == '__main__':
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
