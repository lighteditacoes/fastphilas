from flask import Flask
from flask_login import LoginManager
from routes.usuarios_rota import usuario_bp
from database import db

from models.usuario import Usuario

app = Flask(__name__)

app.config["SECRET_KEY"] = "FastPhilasValdenicio&Ruan"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db.init_app(app)
app.register_blueprint(usuario_bp)

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "usuario.login"

@login_manager.user_loader
def load_user(id_usuario):
    return db.session.get(Usuario, int(id_usuario))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, use_reloader=False)