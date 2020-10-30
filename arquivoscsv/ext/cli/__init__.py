from arquivoscsv.arquivoscsv.ext import db

def init_app(app):
    @app.cli.command()
    def create_db():
        """cria o banco de dados"""
        try:
            db.create_all()
        except expression as identifier:
            pass
        
                
    @app.cli.command()
    def listar_centros():
        """lista centros"""
        return "lista de centros"