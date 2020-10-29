from flask import Flask
from .ext import site
from .ext import toolbar
from .ext import config
from .ext import db


def create_app():
    """[summary]: Factory principal

    Returns:
        [type]: [app]
    """
    app = Flask(__name__)
    config.init_app(app)
    db.init_app(app)
    toolbar.init_app(app)
    site.init_app(app)
    return app
