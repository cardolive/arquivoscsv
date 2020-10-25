from flask import Flask
from .ext.site.views import view

UPLOAD_FOLDER = "uploads"

def create_app():
    """Factory principal"""
    app = Flask(__name__)
    app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
    views.init_app(app)aplu
    return app
