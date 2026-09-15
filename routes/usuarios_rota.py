from flask import Blueprint, render_template, url_for, redirect, request, session
from database import db
from models.usuario import Usuario
from flask_login import login_user, logout_user, login_required, current_user
import uuid
from passlib.context import CryptContext

usuario_bp = Blueprint("usuario", __name__)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_senha(senha: str) -> str:
    return pwd_context.hash(senha)

@usuario_bp.route("/")
def home():
    return render_template("index.html")

@usuario_bp.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    try:
        if request.method == "POST":
            uuid_usuario = str(uuid.uuid4())
            nome = request.form["nome"]
            cpf = request.form["cpf"]
            telefone = request.form["telefone"]
            email = request.form["email"]
            senha = request.form["senha"]
            preferencial = request.form["preferencial"]
            senha_fila = None
            funcao = request.form["funcao"]

            if not nome or not cpf or not telefone or not email or not senha or not preferencial or not funcao:
                return render_template("cadastro.html", erro="Nenhum campo pode está vázio")
            
            usuario  = Usuario.query.filter_by(cpf=cpf).first()
            if usuario:
                return render_template("cadastro.html", erro="CPF já cadastrado.")

            novo_usuario = Usuario(
                uuid_usuario=uuid_usuario,
                nome=nome,
                cpf=cpf,
                telefone=telefone,
                email=email,
                senha=hash_senha(senha),
                preferencial=preferencial,
                senha_fila=senha_fila,
                funcao=funcao
                )

            db.session.add(novo_usuario)
            db.session.commit()

            return redirect(url_for("usuario.login"))
        return render_template("cadastro.html")
    except Exception as e:
        return str(e)

@usuario_bp.route("/login", methods=["GET", "POST"])
def login():
    try:
        if request.method == "POST":
            cpf = request.form.get("cpf")
            senha = request.form.get("senha")

            if not cpf or not senha:
                return render_template("cadastro.html", erro="Nenhum campo pode está vázio")

            usuario  = Usuario.query.filter_by(cpf=cpf).first()

            if not usuario:
                return render_template("login.html", erro="CPF incorreto.")
            
            if not pwd_context.verify(senha, usuario.senha):
                return render_template("login.html", erro="Senha incorreta.")

            login_user(usuario)
            
            return redirect(url_for("usuario.dashboard"))
        return render_template("login.html")
    except Exception as e:
        return str(e)

@usuario_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('usuario.login'))
        
@usuario_bp.route("/dashboard")
@login_required
def dashboard():

    return render_template(
        "dashboard.html",
        usuario=current_user
    )