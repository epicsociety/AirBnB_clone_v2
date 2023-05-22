#!/usr/bin/python3
"""
    My flask script which will run on 0.0.0.0
"""
from flask import Flask
app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hello_HBNB():
    return 'hello HBNB!'


if __name__ == "__main__":
    app.run("0.0.0.0")
