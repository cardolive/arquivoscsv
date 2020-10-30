from arquivoscsv.arquivoscsv.ext import db


class Secao(db.Model):
    __tablename__ = "secao"
    id = db.Column("id", db.Integer, primary_key=True)
    nome = db.Column("nome", db.Unicode, unique=True)
    codpes = db.Column("codpes", db.Integer, default=0)
    dtaalt = db.Column("dtaalt", db.DateTime)
    codpesalt = db.Column("codpesalt", db.Integer)


    def __init__(self, nome, codpes, dtaalt, codpesalt):
        self.nome = nome
        self.codpes = codpes
        self.dtaalt = dtaalt
        elf.codpesalt = codpesalt


    def __init__(self, nome, dtaalt, codpesalt):
        self.nome = nome
        self.dtaalt = dtaalt
        self.codpesalt = codpesalt
