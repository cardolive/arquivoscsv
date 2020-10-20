from flask import Flask

from ext.site.view import views


def create_app():
    """Factory principal"""
    app = Flask(__name__)
    views.init_app(app)
    return app
