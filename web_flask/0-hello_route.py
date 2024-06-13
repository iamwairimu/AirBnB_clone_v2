#!/usr/bin/python3
"""Import the Flask module & create a Flask Web application"""
from flask import Flask
app = Flask(__name__)

"""Define route for the root URL that returns the string"""
@app.route("/airbnb-onepage/", strict_slashes=False)
def hello_holberton():
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
