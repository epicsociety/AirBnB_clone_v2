#!/usr/bin/python3
"""
    My flask script which will run on 0.0.0.0
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return 'hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return 'HBNB'


if __name__ == "__main__":
    app.run("0.0.0.0")
