#!/usr/bin/python3
""" flask module that returns routes '/' and '/hbnb' """


from flask import Flask
from flask import escape

app = Flask('__name__')


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Returns: (str) hello hbnb"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Returns: (str) hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ Returns: (str) c, dynamic_text"""
    return "C {}".format(escape(text.replace('_', ' ')))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """ Returns: (str) static text"""
    text = text.replace('_', ' ') if text else "is cool"
    return "Python {}".format(escape(text))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
