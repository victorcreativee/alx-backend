#!/usr/bin/env python3
"""Determine user timezone"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
import pytz

class Config:
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

def get_user():
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except Exception:
        return None

@app.before_request
def before_request():
    g.user = get_user()

@babel.localeselector
def get_locale():
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@babel.timezoneselector
def get_timezone():
    try:
        tz_param = request.args.get('timezone')
        if tz_param:
            return pytz.timezone(tz_param).zone
        if g.user:
            return pytz.timezone(g.user.get('timezone')).zone
    except Exception:
        pass
    return 'UTC'

@app.route('/')
def index():
    return render_template('7-index.html')

if __name__ == "__main__":
    app.run()
