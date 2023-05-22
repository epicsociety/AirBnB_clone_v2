#!/usr/bin/python3
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
    return ('C' + replace)


if __name__ == "__main__":
    app.run("0.0.0.0")
