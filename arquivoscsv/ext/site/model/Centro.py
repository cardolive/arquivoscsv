from .ext.db import db

class Centro(db.Model):
    __tablename__ = "centro"
    id = db.Column("id", db.Integer, primary_key=True)
    nome = db.Column("nome", db.Unicode, unique=True)
    dtaalt = db.Column("dtaalt", db.DateTime)
    codpesalt = db.Column("codpesalt", db.Integer)

        
    def __init__(self, nome, dtaalt, codpesalt):
        self.nome = nome
        self.dtaalt = dtaalt
        self.codpesalt = codpesalt
