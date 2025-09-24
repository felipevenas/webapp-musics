from flask import render_template, Blueprint, session, redirect, url_for

from app.domain.music.model import Music

music1 = Music("Vai e chora", "Sorriso Maroto", "Samba")
music2 = Music("Camisa 10", "Turma do Pagode", "Samba")
music3 = Music("Amar não é pecado", "Silvanno Salles", "Arrocha")
lista = [music1, music2, music3]

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

@index_bp.route('/musics')
def list_page():
    if session['username'] == None or 'username' not in session:
        return redirect(url_for('index_bp.login_page'))
    return render_template("musics.html",
                           musics = lista,
                           title = "Lista de músicas")

@index_bp.route('/login')
def login_page():
    return render_template("auth/login.html",
                           title = "Login")
