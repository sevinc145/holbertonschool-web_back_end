#!/usr/bin/env python3
""" Route module """


from flask import Flask, request, render_template, g
from flask_babel import Babel
from os import getenv
from typing import Union

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Setup - Babel configuration """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('5-app.Config')


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """ GET / Return: 4-index.html"""
    return render_template('5-index.html')


@babel.localeselector
def get_locale() -> str:
    """ Determines best match for supported languages """
    if request.args.get('locale'):
        locale = request.args.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> Union[dict, None]:
    """ Returns user dict if ID can be found """
    if request.args.get('login_as'):
        user = int(request.args.get('login_as'))
        if user in users:
            return users.get(user)
    else:
        return None


@app.before_request
def before_request():
    """ Finds user and sets as global on flask.g.user """
    g.user = get_user()


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
