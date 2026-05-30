#!/usr/bin/env python3
"""
basic Flask app
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """flask app configuration"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    Get a user from database.
    """
    user_id = request.args.get('login_as')
    if user_id and int(user_id) in users:
        return users[int(user_id)]
    return None


@babel.localeselector
def get_locale():
    """
    get_locale function
    """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    user = get_user()
    if user and user['locale'] and user['locale'] in app.config['LANGUAGES']:
        return user['locale']

    header_locale = request.headers.get('locale')
    if header_locale and header_locale in app.config['LANGUAGES']:
        return header_locale

    return app.config['BABEL_DEFAULT_LOCALE']


@app.before_request
def before_request():
    """
    Executed before all other functions
    """
    g.user = get_user()


@app.route('/')
def hello_world():
    """
    Render a template with a welcome message
    """
    welcome_message = gettext('You are not logged in.')
    if g.user:
        welcome_message = gettext(
            'You are logged in as %(username)s.',
            username=g.user['name'])
    return render_template('6-index.html', welcome_message=welcome_message)


@babel.timezoneselector
def get_timezone():
    """_summary_
    Returns:
        _type_: _description_
    """
    if g.get('timezone'):
        try:
            return pytz.timezone(g.timezone)
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    if request.cookies.get('timezone'):
        try:
            return pytz.timezone(request.cookies.get('timezone'))
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    if session.get('timezone'):
        try:
            return pytz.timezone(session.get('timezone'))
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    return pytz.utc


if __name__ == '__main__':
    app.run()