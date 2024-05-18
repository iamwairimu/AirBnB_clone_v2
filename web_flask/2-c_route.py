#!/usr/bin/python3
from flask import Flask
"""new web app"""
app = Flask(__name__)

"""Define route of URL to return string"""
@app.route("/", strict_slashes=False)
def hello_holberton():
    return "Hello HBNB!"

"""Define route for hbnb"""
@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"

"""Define route for c text"""
@app.route("/c/<text>", strict_slashes=False)
def Cisfun(text):
    """replace underscore with space"""
    text = text.replace("_", " ")
    return "C " + text

"""start Flask app"""
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
