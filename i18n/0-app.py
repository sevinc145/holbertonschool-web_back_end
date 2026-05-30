#!/usr/bin/env python3
"""
learn flask_babel
"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)


@app.route('/')
def index():
    """
    a single / route and an index.html template that simply
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
