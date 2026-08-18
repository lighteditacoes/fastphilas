from database import db

class Filas(db.Model):
    __tablename__ = "filas"

    id_fila = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), nullable=False)
    posicao = db.Column(db.Integer, nullable=False)