#!/usr/bin/env python3
"""
learn flask_babel
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel

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
    BABEL_DEFAULT_LOCALE = 'en'
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


def get_user():
    """
    Define a get_user function that
    returns a user dictionary or None
    if the ID cannot be found or if
    login_as was not passed.
    """
    user_id = request.args.get('login_as')
    if user_id and user_id.isdigit():
        user_id = int(user_id)
        return users.get(user_id)
    return None


@app.before_request
def before_request():
    """
    Define a before_request function and
    use the app.before_request decorator
    to make it be executed before all
    other functions.
    """
    g.user = get_user()


@app.route('/')
def index():
    """
    A single / route and an index.html template that simply
    displays the translated strings.
    """
    return render_template(
        '5-index.html',
        username=g.user['name'] if g.user else None)


if __name__ == '__main__':
    app.run(debug=True)
