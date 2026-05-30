#!/usr/bin/env python3
"""
learn flask_babel
"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """
    In order to configure available languages
    in our app, you will create a Config class
    hat has a LANGUAGES class attribute equal
    to ["en", "fr"]
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """
    a single / route and an index.html template that simply
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
