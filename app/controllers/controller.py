from flask import render_template, Blueprint

# Esse controlador serve apenas para renderizar as páginas:

index_bp = Blueprint('index_bp', __name__)

@index_bp.route('/')
def index():
    return render_template("index.html",
                           title = "Início")

@index_bp.route('/register')
def register_page():
    return render_template("add_music.html",
                           title = "Cadastrar música")

@index_bp.route('/login')
def login_page():
    return render_template("auth/login.html",
                           title = "Login")