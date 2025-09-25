from flask import render_template, Blueprint, session, redirect, url_for, flash

from app.domain.music.model import Music
from app.domain.upload.services import search_image

# Esse controlador serve apenas para renderizar as páginas:

index_bp = Blueprint('index_bp', __name__)

@index_bp.route('/')
def index():
    return render_template("index.html",
                           title = "Início")

@index_bp.route('/register')
def register_page():
    if session['username'] == None or 'username' not in session:
        flash("É necessário se autenticar!")
        return redirect(url_for('index_bp.login_page'))
    return render_template("register_page.html", 
                           title = "Cadastrar música")

@index_bp.route('/musics')
def list_page():
    if session['username'] == None or 'username' not in session:
        flash("É necessário se autenticar!")
        return redirect(url_for('index_bp.login_page'))
    
    lista = Music.query.order_by(Music.id)

    return render_template("list_page.html",
                           musics = lista,
                           title = "Lista de músicas")

@index_bp.route('/update/<int:id>')
def update_page(id):
    if session['username'] == None or 'username' not in session:
        flash("É necessário se autenticar!")
        return redirect(url_for('index_bp.login_page'))
    
    find_music = Music.query.filter_by(id=id).first()

    album = search_image(id)

    return render_template('update_page.html', 
                           title = "Editar música",
                           music = find_music,
                           album_music = album)

@index_bp.route('/login')
def login_page():
    return render_template("auth/login_page.html",
                           title = "Login")

