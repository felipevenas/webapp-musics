from flask import render_template, Blueprint, session, redirect, url_for

from app.domain.music.model import Music

# Esse controlador serve apenas para renderizar as páginas:

index_bp = Blueprint('index_bp', __name__)

@index_bp.route('/')
def index():
    return render_template("index.html",
                           title = "Início")

@index_bp.route('/register')
def register_page():
    if session['username'] == None or 'username' not in session:
        return redirect(url_for('index_bp.login_page'))
    return render_template("add_music.html", 
                           title = "Cadastrar música")

@index_bp.route('/update')
def update_page():
    if session['username'] == None or 'username' not in session:
        return redirect(url_for('index_bp.login_page'))
    return render_template("edit_music.html",
                           title = "Editar música")

@index_bp.route('/musics')
def list_page():
    if session['username'] == None or 'username' not in session:
        return redirect(url_for('index_bp.login_page'))
    
    lista = Music.query.order_by(Music.id)

    return render_template("musics.html",
                           musics = lista,
                           title = "Lista de músicas")

@index_bp.route('/login')
def login_page():
    return render_template("auth/login.html",
                           title = "Login")

