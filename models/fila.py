from database import db

class Filas(db.Model):
    __tablename__ = "filas"

    id_fila = db.Column(db.Integer, primary_key=True)
    uuid_usuario = db.Column(db.String(255), db.ForeignKey('usuarios.uuid_usuario'), nullable=False)
    tipo_fila = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    hora_entrada = db.Column(db.String(20), nullable=False)
    hora_chamada = db.Column(db.String(20), nullable=True)