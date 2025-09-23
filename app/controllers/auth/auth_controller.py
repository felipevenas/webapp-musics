from flask import redirect, request, Blueprint, session, flash

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/auth', methods=['POST'])
def authenticate(): 
    if request.form['inputPass'] == 'admin':
        session['username'] = request.form['inputUser']
        flash("Usário logado com sucesso!")
        return redirect('/musics')
    else:
        flash("Usuário ou senha inválidos!")
        return redirect('/login')
    
@auth_bp.route('/logout')
def logout():
    session['username'] = None
    return redirect('/')