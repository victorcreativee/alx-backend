@babel.localeselector
def get_locale():
    """Locale from URL > User > Headers > Default"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    if g.get('user'):
        user_locale = g.user.get('locale')
        if user_locale in app.config['LANGUAGES']:
            return user_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])
