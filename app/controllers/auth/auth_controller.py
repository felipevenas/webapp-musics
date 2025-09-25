from flask import redirect, request, Blueprint, session, flash, url_for

from app.domain.user.model import User

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/auth', methods=['POST'])
def authenticate(): 

    user = User.query.filter_by(login=request.form['inputUser']).first()
    if user:
        if request.form['inputPass'] == user.password:
            session['username'] = request.form['inputUser']
            flash(f"Usuário {user.login} logado com sucesso!", category="success")
            return redirect(url_for('index_bp.list_page'))       
        else:
            flash("Senha inválida!", category="error")
            return redirect('/login')       
    else:
        flash("Usuário inválido!", category="error")
        return redirect('/login')
    
@auth_bp.route('/logout')
def logout():
    session['username'] = None
    flash("Usuário deslogado!")
    return redirect(url_for('index_bp.index'))