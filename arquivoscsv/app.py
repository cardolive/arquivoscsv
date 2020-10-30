from flask import Flask
from .ext import site
from .ext import toolbar
from .ext import config
from .ext import db
from .ext import cli



def create_app():
    """[summary]: Factory principal

    Returns:
        [type]: [app]
    """
    app = Flask(__name__) # topo da inicialização
    config.init_app(app) # depois de iniciar a app
    db.init_app(app)
    cli.init_app(app) # depois de iniciar o db
    toolbar.init_app(app) # debug de paginas web, antes de inicar o site
    site.init_app(app)
    return app
