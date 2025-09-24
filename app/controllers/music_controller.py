from flask import render_template, redirect, request, Blueprint, url_for

from app.domain.music.model import Music
from app.controllers.controller import lista

# Esse controlador realiza ações e também pode redirecionar para outras páginas:

music_bp = Blueprint('music_bp', __name__)

@music_bp.route('/add', methods=['POST'])
def add_music():
    name = request.form['inputName']
    artist = request.form['inputArtist']
    genre = request.form['inputGenre']
    newMusic = Music(name, artist, genre)
    lista.append(newMusic)

    return redirect(url_for('index_bp.list_page'))