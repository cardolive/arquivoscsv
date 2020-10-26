from flask import Flask
from .ext import site
UPLOAD_FOLDER = "/uploads"


def create_app():
    """[summary]: Factory principal

    Returns:
        [type]: [app]
    """
    app = Flask(__name__)
    app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
    site.init_app(app)
    return app