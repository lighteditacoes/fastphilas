from database import db
from flask_login import UserMixin


class Usuario(UserMixin, db.Model):
    __tablename__ = "usuarios"

    id_usuario = db.Column(db.Integer, primary_key=True)
    uuid_usuario = db.Column(db.String(150), nullable=False)
    nome = db.Column(db.String(40), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    telefone = db.Column(db.String(11), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    preferencial = db.Column(db.String(3), nullable=False)
    senha_fila = db.Column(db.Integer)
    funcao = db.Column(db.String(30), nullable=False)

    def get_id(self):
        return str(self.id_usuario)

    def __repr__(self):
        return f"{self.nome} - {self.id_usuario}"
