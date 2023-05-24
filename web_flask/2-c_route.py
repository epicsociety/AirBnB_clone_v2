#!/usr/bin/python3
<<<<<<< HEAD
""" flask module that returns routes '/' and '/hbnb' """


from flask import Flask

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
    msg = text.replace('_', " ")
    return "C {}".format(msg)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
=======
"""
    Flask script that those alot of things
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    replace = text.replace("_", " ")
    return ('C ' + replace)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
>>>>>>> upstream/master
