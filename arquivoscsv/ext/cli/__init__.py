from .ext.db import db

def init_app(app):
    @app.cli.command()
    def create_db():
        """cria o banco de dados"""
        db.create_all()