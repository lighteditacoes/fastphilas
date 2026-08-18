from flask import Blueprint, render_template, redirect, request
from database import db
from models.usuario import Usuario
from models.fila import Filas

usuario_bp = Blueprint("usuario", __name__)

@usuario_bp.route("/")
def index():
    return render_template("index.html")