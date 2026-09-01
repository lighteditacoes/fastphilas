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
            nome = request.form["nome"].strip()
            cpf = request.form["cpf"].strip()
            telefone = request.form["telefone"].strip()
            email = request.form["email"].strip()
            senha_crua = request.form["senha"].strip()
            preferencial = request.form["preferencial"].strip()
            senha_fila = None
            funcao = request.form["funcao"].strip()

            msg = []

            campos_obrigatorios = [nome, cpf, telefone, email, senha_crua, preferencial, funcao]
            if any(not campo for campo in campos_obrigatorios):
                msg.append("Todos os campos obrigatórios devem ser preenchidos.")

            if nome and (len(nome) < 8 or len(nome) > 40):
                msg.append("O Nome deve ter entre 8 e 40 caracteres.")

            if cpf and len(cpf) != 11:
                msg.append("O CPF deve ter exatamente 11 caracteres.")

            if telefone and (len(telefone) < 10 or len(telefone) > 11):
                msg.append("O Telefone deve ter 10 ou 11 caracteres.")

            if email and (len(email) < 11 or len(email) > 100):
                msg.append("O E-mail deve ter entre 11 e 100 caracteres.")

            if senha_crua and (len(senha_crua) < 8):
                msg.append("A senha deve ter no mínimo 8 caracteres.")

            if preferencial and len(preferencial) > 3:
                msg.append("O campo Preferencial deve ter no máximo 3 caracteres.")

            if funcao and len(funcao) > 30:
                msg.append("A Função deve ter no máximo 30 caracteres.")

            if msg:
                return render_template("index.html", erros=msg)
            
            senha = hash_senha(senha_crua)

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
        db.session.rollback()
        return {"erros": [f"Erro interno no servidor: {str(e)}"]}, 500

    return render_template("index.html")