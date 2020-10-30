from arquivoscsv.arquivoscsv.ext import db
import click

def init_app(app):
    @app.cli.command()
    def create_db():
        """cria o banco de dados"""
        db.create_all()
       
                
    @app.cli.command()
    def listar_centros():
        """lista centros"""
        click.echo("lista de centros")