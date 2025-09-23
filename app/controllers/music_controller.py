from flask import render_template, redirect, request, Blueprint

from app.domain.music.model import Music

music1 = Music("Vai e chora", "Sorriso Maroto", "Samba")
music2 = Music("Camisa 10", "Turma do Pagode", "Samba")
music3 = Music("Amar não é pecado", "Silvanno Salles", "Arrocha")
lista = [music1, music2, music3]

# Esse controlador realiza ações e também pode redirecionar para outras páginas:

music_bp = Blueprint('music_bp', __name__)

@music_bp.route('/musics')
def list_musics():
    return render_template("musics.html",
                           musics = lista,
                           title = "Lista de músicas")

@music_bp.route('/add', methods=['POST'])
def add_music():
    name = request.form['inputName']
    artist = request.form['inputArtist']
    genre = request.form['inputGenre']
    newMusic = Music(name, artist, genre)
    lista.append(newMusic)

    return redirect('/musics')