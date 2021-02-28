from flask import Flask, request, g
from flask_static_digest import FlaskStaticDigest
from flask_babel import Babel
from config import Config


app = Flask(__name__)
app.config.from_object(Config)

flask_static_digest = FlaskStaticDigest()
flask_static_digest.init_app(app)

# set up babel
babel = Babel(app)
@babel.localeselector
def get_locale():
    if not g.get('lang_code', None):
        g.lang_code = request.accept_languages.best_match(app.config['LANGUAGES'])
    return g.lang_code

from app import routes
