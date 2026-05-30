#!/usr/bin/env python3
"""
Basic Flask app with Babel localization
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Babel configuration"""
    LANGUAGES = ["en", "fr"]


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


def get_locale():
    """
    Returns the locale from URL parameter if supported,
    otherwise uses the best match from the request headers.
    """
    locale = request.args.get('locale')

    if locale and locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(
        app.config['LANGUAGES']
    )


babel = Babel(app, locale_selector=get_locale)


@app.route('/')
def index():
    """Render index page"""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
