#!/usr/bin/python3
""" starts a web application"""

from flask import Flask
from flask import escape
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Returns: (str) Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns: (str) HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Returns: (str) C, followed by the value of the text variable"""
    text = text.replace('_', ' ') if text else ""
    return "C {}".format(escape(text))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """Returns: (str) Python, followed by the value of the text variable"""
    text = text.replace('_', ' ') if text else ""
    return "Python {}".format(escape(text))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Returns: (str) n is a number if n is an integer"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Returns: (HTML) Number: n inside an H1 tag"""
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """ args:
            n: number passed
        Returns: (HTML) number odd or even
    """
    odd_or_even = ''
    odd_or_even = 'even' if n % 2 == 0 else 'odd'
    return render_template('6-number_odd_or_even.html', number=n,
                           odd_or_even=odd_or_even)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
