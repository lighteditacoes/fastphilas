from flask import Blueprint, render_template, url_for, redirect, request, session
from database import db
from models.fila import Filas
from models.usuario import Usuario
from flask_login import login_required, current_user
from datetime import datetime

fila_bp = Blueprint("fila", __name__)

@fila_bp.route("/fila/entrar", methods=["GET", "POST"])
@login_required
def entrar_fila():
    if request.method == "POST":
        uuid = current_user.uuid_usuario
        
        usuarios = Filas.query.filter_by(uuid_usuario=uuid, status="aguardando").all()

        if usuarios:
            return redirect(url_for('usuario.dashboard'))

        if current_user.preferencial == "sim":
            tipo_fila = "preferencial"
        else:
            tipo_fila = "normal"
        
        senha_fila = Filas(
            uuid_usuario=uuid,
            tipo_fila=tipo_fila,
            status="aguardando",
            hora_entrada=datetime.now(),
            hora_chamada=None
            )

        db.session.add(senha_fila)
        db.session.commit()

        return redirect(url_for('usuario.dashboard'))
    return (url_for('usuario.dashboard'))

@fila_bp.route("/fila/sair", methods=["GET", "POST"])
@login_required
def sair_fila():
    if request.method == "POST":
        uuid = current_user.uuid_usuario

        usuario = Filas.query.filter_by(uuid_usuario=uuid, status="aguardando").first()

        if usuario:
            usuario.status = "cancelado"
            db.session.commit()

        return redirect(url_for('usuario.dashboard'))
    return (url_for('usuario.dashboard'))