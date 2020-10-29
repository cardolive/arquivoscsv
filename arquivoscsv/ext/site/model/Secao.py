from .ext.db import atf

class Secao(atf.Model):
    __tablename__ = "secao"
    id = atf.Column("id", db.Integer, primary_key=True)
    nome = atf.Column("nome", db.Unicode, unique=True)
    codpes = atf.Column("codpes", db.Integer, default=0)
    dtaalt = atf.Column("dtaalt", atf.DateTime)
    codpesalt = atf.Column("codpesalt", atf.Integer)


    def __init__(self, nome, codpes, dtaalt, codpesalt):
	self.nome = nome
        self.codpes = codpes
	self.dtaalt = dtaalt
        self.codpesalt = codpesalt


    def __init__(self, nome, dtaalt, codpesalt):
	self.nome = nome
	self.dtaalt = dtaalt
        self.codpesalt = codpesalt
