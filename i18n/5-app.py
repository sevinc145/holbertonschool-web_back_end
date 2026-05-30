#!/usr/bin/env python3
"""basic Flask app"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext as _

app = Flask(__name__, template_folder='templates')
babel = Babel(app)


class Config:
    """class cofig for the Flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id):
    """Get a user from database."""
    return users.get(user_id)


@app.before_request
def before_request():
    """Set the global user for each request."""
    user_id = request.args.get('login_as')
    g.user = get_user(int(user_id)) if user_id else None


@babel.localeselector
def get_locale():
    """
    get_locale function
    """
    user = getattr(g, 'user', None)
    if user is not None:
        locale = user['locale']
        if locale in app.config['LANGUAGES']:
            return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=["GET"])
def index():
    """
    index template
    """
    return render_template(
        '5-index.html',
        username=g.user['name'] if g.user else None)


if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)
