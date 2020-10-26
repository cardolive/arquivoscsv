from flask import Flask
from arquivoscsv.ext import site
UPLOAD_FOLDER = "/uploads"


def create_app():
    """Factory principal"""
    app = Flask(__name__)
    app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
    site.init_app(app)
    return app
