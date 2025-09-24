from flask import redirect, request, Blueprint, session, flash, url_for

from app.domain.user.model import User

user1 = User('Felipe Venas', 'felipe.venas', 'admin')
user2 = User('João Mendes', 'joao.mendes', 'mendes515')
user3 = User('Maria Luisa', 'maluluisa159', 'luisa2005')

users = {
    user1.login: user1,
    user2.login: user2,
    user3.login: user3
}

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/auth', methods=['POST'])
def authenticate(): 
    if request.form['inputUser'] in users:
        user_selected = users[request.form['inputUser']]

        if request.form['inputPass'] == user_selected.password:
            session['username'] = request.form['inputUser']
            flash(f"Usário {user_selected.login} logado com sucesso!", category="success")
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