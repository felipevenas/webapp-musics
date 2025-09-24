from flask import redirect, request, Blueprint, url_for, flash

from app.domain.music.model import Music
from app.db.config import db

# Esse controlador realiza ações e também pode redirecionar para outras páginas:

music_bp = Blueprint('music_bp', __name__)

@music_bp.route('/add', methods=['POST'])
def add_music():
    form_name = request.form['inputName']
    form_artist = request.form['inputArtist']
    form_genre = request.form['inputGenre']

    music = Music.query.filter_by(name=form_name).first()
    if music:
        flash("Música já cadastrada!")
        return redirect(url_for('index_bp.list_page'))
    
    new_music = Music(name=form_name,
                      artist=form_artist, 
                      genre=form_genre)
    
    db.session.add(new_music)
    db.session.commit()

    return redirect(url_for('index_bp.list_page'))