#!/usr/bin/env python3
"""Mock login and i18n with user info"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _

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
    """Get user from login_as param"""
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except Exception:
        return None

@app.before_request
def before_request():
    """Set user on g"""
    g.user = get_user()

@babel.localeselector
def get_locale():
    """Use locale from user or request"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    return render_template('5-index.html')

if __name__ == '__main__':
    app.run()
