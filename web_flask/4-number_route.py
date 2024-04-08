from flask import Flask
''' Start a Flask web app'''
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    '''display "Hello HBNB!" '''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''display "HBNB" '''
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    '''display C followed by the value of the text variable'''
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    '''display python followed by value of the text variable
    text default = "is cool"
    '''
    return "Python {}".format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
