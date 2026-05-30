#!/usr/bin/env python3

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'


app = Flask(__name__)
app.config.from_object(Config)


def get_locale():
    locale = request.args.get('locale')

    if locale and locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(
        app.config['LANGUAGES']
    )


babel = Babel(app, locale_selector=get_locale)


@app.route('/')
def index():
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
