from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField, validators
from wtforms import StringField, SubmitField, SelectField, FileField, validators

class FormMusic(FlaskForm):
    name = StringField('Nome:', [validators.DataRequired(),
                                validators.length(min=2, max=30)])
    artist = StringField('Artista:', [validators.DataRequired(),
                                     validators.length(min=2, max=50)])
    
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

class FormLogin(FlaskForm):
    login = StringField('Login:', [validators.DataRequired(),
                        validators.length(min=6, max=20)])
    password = PasswordField('Senha:', [validators.DataRequired(),
                             validators.length(min=4, max=15)])
    button = SubmitField('Entrar')

class FormRegister(FlaskForm):
    name = StringField('Nome completo:', [validators.DataRequired(),
                        validators.length(min=2, max=50)])
    login = StringField('Login:', [validators.DataRequired(),
                        validators.length(min=6, max=20)])
    password = PasswordField('Senha:', [validators.DataRequired(),
                             validators.length(min=4, max=30)])
    button = SubmitField('Cadastrar')