#!/usr/bin/env python3
"""
learn flask_babel
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)



class Config:
    """
    In order to configure available languages
    in our app, you will create a Config class
    that has a LANGUAGES class attribute equal
    to ["en", "fr"]
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'fr'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


def get_locale():
    """
    Determine the best match with our supported languages.
    """
    lang = request.args.get('locale')
    if lang in app.config['LANGUAGES']:
        return lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel = Babel(app, locale_selector=get_locale)


@app.route('/')
def index():
    """
    A single / route and an index.html template that simply
    displays the translated strings.
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
