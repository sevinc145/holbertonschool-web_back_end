#!/usr/bin/env python3
"""
learn flask_babel
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
import pytz
from pytz.exceptions import UnknownTimeZoneError


app = Flask(__name__)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user['locale']

    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_timezone():
    """
    Determine the best time zone based on URL parameters or user settings.
    Defaults to UTC.
    """
    timezone = request.args.get('timezone')
    if timezone:
        try:
            return pytz.timezone(timezone)
        except UnknownTimeZoneError:
            pass

    if g.user and g.user.get('timezone'):
        try:
            return pytz.timezone(g.user['timezone'])
        except UnknownTimeZoneError:
            pass
    return pytz.timezone(app.config['BABEL_DEFAULT_TIMEZONE'])


babel = Babel(app, locale_selector=get_locale, timezone_selector=get_timezone)


def get_user():
    """Get user based on login_as parameter."""
    user_id = request.args.get('login_as')
    if user_id and user_id.isdigit():
        user_id = int(user_id)
        return users.get(user_id)
    return None


@app.before_request
def before_request():
    """
    before_request should use
      get_user to find a user
      if any, and set it as a
      global on flask.g.user.
    """
    g.user = get_user()


@app.route('/')
def index():
    """A single / route and an index.html template."""

    return render_template(
        '5-index.html',
        username=g.user['name'] if g.user else None)


if __name__ == '__main__':
    app.run(debug=True)
