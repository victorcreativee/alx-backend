#!/usr/bin/env python3
"""Parametrize templates using gettext"""
from flask import Flask, render_template
from flask_babel import Babel, _

class Config:
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

@app.route('/')
def index():
    return render_template('3-index.html')

if __name__ == "__main__":
    app.run()
