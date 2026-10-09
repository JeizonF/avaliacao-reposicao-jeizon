from flask import flash, redirect, session, url_for


def exigir_login():
    # Complete esta função durante a avaliação.
    if 'usuario_id' not in session:
        flash('n tem session')
        return redirect(url_for('auth.login'))
    return None
