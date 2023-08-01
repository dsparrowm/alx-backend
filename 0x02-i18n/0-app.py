#!/usr/bin/env python3
"""This is a basic flask app"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello():
    """a simple function that renders a html page"""
    return rwnder_template('0-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0")
