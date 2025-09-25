from flask import redirect, request, Blueprint, url_for, flash, send_from_directory

from app.domain.music.model import Music
from app.db.config import db
from app.domain.upload import config
 
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

    archive = request.files['inputFile']

    archive_name = archive.filename
    archive_name = archive_name.split('.')
    extension = archive_name[len(archive_name)-1]

    folder = config.UPLOAD_FOLDER
    archive.save(f'{folder}album{new_music.id}.{extension}')

    return redirect(url_for('index_bp.list_page'))

@music_bp.route('/update', methods=['POST'])
def update_music():
    
    music = Music.query.filter_by(id=request.form['inputId']).first()
    
    music.name = request.form['inputName']
    music.artist = request.form['inputArtist']
    music.genre = request.form['inputGenre']

    db.session.add(music)
    db.session.commit()

    archive = request.files['inputFile']

    archive_name = archive.filename
    archive_name = archive_name.split('.')
    extension = archive_name[len(archive_name)-1]

    folder = config.UPLOAD_FOLDER
    archive.save(f'{folder}album{music.id}.{extension}')

    return redirect(url_for('index_bp.list_page'))

@music_bp.route('/delete/<int:id>')
def delete_music(id):

    Music.query.filter_by(id=id).delete()
    flash("Música excluída com sucesso!")
    db.session.commit()

    return redirect(url_for('index_bp.list_page'))

@music_bp.route('/uploads/<name_image>')
def show_image(name_image):
    return send_from_directory('uploads', name_image)
