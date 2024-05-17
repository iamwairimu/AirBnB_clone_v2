#!/usr/bin/python3
from flask import Flask

"""Create a new Flask web app"""
app = Flask(__name__)

"""Define route root URL that returns a string"""
@app.route("/", strict_slashes=False)
def hello_holberton():
    return "Hello HBNB!"

"""Define route URL hbnb to return string"""
@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"

"""start Flask app"""
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
