#!/usr/bin/python3
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
