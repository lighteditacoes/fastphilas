from flask import Blueprint, render_template, url_for, redirect, request
from database import db
from models.usuario import Usuario
from models.fila import Filas

import uuid
from passlib.context import CryptContext

usuario_bp = Blueprint("usuario", __name__)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_senha(senha: str) -> str:
    return pwd_context.hash(senha)

@usuario_bp.route("/")
def home():
    return render_template("index.html")

@usuario_bp.route("/insert", methods=["GET", "POST"])
def insert_usuario():
    try:
        if request.method == "POST":
            uuid_usuario = str(uuid.uuid4())
            nome = request.form["nome"]
            cpf = request.form["cpf"]
            telefone = request.form["telefone"]
            email = request.form["email"]
            senha = hash_senha(request.form["senha"])
            preferencial = request.form["preferencial"]
            senha_fila = None
            funcao = request.form["funcao"]

            novo_usuario = Usuario(
                uuid_usuario=uuid_usuario,
                nome=nome,
                cpf=cpf,
                telefone=telefone,
                email=email,
                senha=senha,
                preferencial=preferencial,
                senha_fila=senha_fila,
                funcao=funcao
                )

            db.session.add(novo_usuario)
            db.session.commit()
            return redirect(url_for("usuario.home"))

    except Exception as e:
        return f"Erro ao cadastrar usuário: {e}"