from .ext.db import atf

class Sub_Centro(atf.Model):
    __tablename__ = "sub_centro"
    id = atf.Column("id", atf.Integer, primary_key=True)
    nome = atf.Column("nome", atf.Unicode, unique=True)
    dtaalt = atf.Column("dtaalt", atf.DateTime)
    codpesalt = atf.Column("codpesalt", atf.Integer)

        
    def __init__(self, nome, dtaalt, codpesalt):
	self.nome = nome
	self.dtaalt = dtaalt
        self.codpesalt = codpesalt
