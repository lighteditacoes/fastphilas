from flask import Blueprint, render_template, url_for, redirect, request, session
from database import db
from models.fila import Filas

fila_bp = Blueprint("filas", __name__)