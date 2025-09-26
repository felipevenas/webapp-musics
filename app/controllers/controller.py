from flask import render_template, Blueprint, session, redirect, url_for, flash

from app.domain.music.model import Music
from app.domain.upload.services import search_image
from app.forms.forms import FormMusic, FormLogin, FormRegister
from app.forms.forms import FormMusic

# Esse controlador serve apenas para renderizar as páginas:

index_bp = Blueprint('index_bp', __name__)

@index_bp.route('/')
def index():
    if session['username'] == None or 'username' not in session:
        flash("É necessário se autenticar!")
        return redirect(url_for('index_bp.login_page'))
    return render_template("index.html",
                           title = "Início")

@index_bp.route('/add')
def add_page():
    if session['username'] == None or 'username' not in session:
        flash("É necessário se autenticar!")
        return redirect(url_for('index_bp.login_page'))
    return render_template("add_music.html", 
                           title = "Cadastrar música")

@index_bp.route('/update')
def update_page():
    if session['username'] == None or 'username' not in session:
        return redirect(url_for('index_bp.login_page'))
    return render_template("edit_music.html",
                           title = "Editar música")
    
    form = FormMusic()
    
    return render_template("add_page.html", 

    
    form = FormMusic()
    
    return render_template("register_page.html", 
                           title = "Cadastrar música",
                           form=form)

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

    form = FormMusic()

    form.name.data = find_music.name
    form.artist.data = find_music.artist
    form.genre.data = find_music.genre

    album = search_image(id)

    return render_template('update_page.html', 
                           title = "Editar música",
                           form = form,
                           music = form,
                           album_music = album,
                           id=id)

@index_bp.route('/login')
def login_page():
    form = FormLogin()
    return render_template("auth/login_page.html",
                           title = "Login",
                           form=form)
    return render_template("auth/login_page.html",
                           title = "Login")

@index_bp.route('/register')
def register_page():
    form = FormRegister()
    return render_template("auth/register_page.html",
                           title = "Registre-se",
                           form=form)