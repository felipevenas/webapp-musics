from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, FileField, validators

class FormMusic(FlaskForm):
    name = StringField('Nome:', [validators.DataRequired(),
                                validators.length(min=2, max=30)])
    
    artist = StringField('Artista:', [validators.DataRequired(),
                                     validators.length(min=2, max=50)])
    
    genre = SelectField('Gênero:',
                        validators=[validators.DataRequired(message="Por favor, escolha um gênero.")],
                        choices=[
                            ('', 'Escolha...'),
                            ('Arrocha', 'Arrocha'),
                            ('Samba', 'Samba'),
                            ('Pop', 'Pop'),
                            ('Funk', 'Funk'),
                            ('Sertanejo', 'Sertanejo'),
                            ('Rock', 'Rock'),
                            ('MBP', 'MBP')
                            ]
                        )
    
    button = SubmitField('Cadastrar')