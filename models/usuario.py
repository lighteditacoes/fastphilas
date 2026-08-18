from database import db

class Usuario(db.Model):
    __tablename__ = "usuarios"

    id_usuario = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    telefone = db.Column(db.String(11), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    senha = db.Column(db.String(150), nullable=False)
    preferencial = db.Column(db.String(3), nullable=False)
    senha_fila = db.Column(db.Integer, nullable=False)
    funcao = db.Column(db.String(11), nullable=False)

    def __repr__(self):
        return f"{self.nome} - {self.id}"