#!/usr/bin/env python3
""" Basic Flask app """
import pytz
from typing import Dict
from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """ Config """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ Locale selector """
    requested_locale = request.args.get('locale')
    if requested_locale in app.config['LANGUAGES']:
        return requested_locale
    try:
        if g.user['locale'] in app.config['LANGUAGES']:
            return g.user['locale']
    except Exception:
        pass
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> Dict:
    """ Get user """
    try:
        user_id = request.args.get('login_as')
        if user_id is not None:
            user_id = int(user_id)
            return users.get(user_id)
    except (ValueError, TypeError):
        return None


@app.before_request
def before_request():
    """ Before request """
    g.user = get_user()


@babel.timezoneselector
def get_timezone():
    user = getattr(g, 'user', None)
    if user is not None:
        return user.timezone


@babel.timezoneselector
def get_timezone() -> str:
    """ time zone """
    try:
        if request.args.get("timezone"):
            return pytz.timezone(request.args.get("timezone"))
        elif g.user and g.user.get("timezone"):
            return pytz.timezone(g.user.get("timezone"))
        else:
            return app.config['BABEL_DEFAULT_TIMEZONE']
    except (pytz.exceptions.UnknownTimeZoneError, Exception):
        return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def root():
    """ Basic Flask app """

    try:
        guser = g.user['name']
    except Exception:
        guser = None
    return render_template('5-index.html', username=guser)


if __name__ == "__main__":
    app.run()
