from flask import redirect, request, Blueprint, session, flash, url_for
from flask_bcrypt import generate_password_hash, check_password_hash

from app.domain.user.model import User
from app.forms.forms import FormLogin, FormRegister
from app.db.config import db

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/auth', methods=['POST'])
def authenticate(): 

    form = FormLogin(request.form) 

    user = User.query.filter_by(login=form.login.data).first()
    decrypt_pass = check_password_hash(user.password, form.password.data)

    if user and decrypt_pass:
        session['username'] = user.login
        flash(f"Usuário {user.login} logado com sucesso!")
        return redirect(url_for('index_bp.list_page'))           
    else:
        flash("Usuário ou senha inválidos!")
        return redirect('/login')
    
@auth_bp.route('/register', methods=['POST'])
def register():

    form = FormRegister(request.form)

    if not form.validate_on_submit():
        return redirect(url_for('index_bp.register_page'))
    
    form_name = form.name.data
    form_login = form.login.data
    form_password = generate_password_hash(form.password.data).decode('utf-8')
    
    user = User.query.filter_by(login=form_login).first()
    if user:
        flash("Nome de usuário já existe!")
        return redirect(url_for('index_bp.register_page'))
    
    new_User = User(name=form_name,
                    login=form_login,
                    password=form_password)
    
    db.session.add(new_User)
    db.session.commit()

    flash("Usuário cadastrado com sucesso!")
    return redirect(url_for('index_bp.login_page'))

    
@auth_bp.route('/logout')
def logout():
    session['username'] = None
    flash("Usuário deslogado!")
    return redirect(url_for('index_bp.index'))