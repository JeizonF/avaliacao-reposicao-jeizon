from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from database import *


auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        if buscar_usuario_por_email(email):
            flash('esse email ja existe')
            return redirect(url_for('auth.registro'))
        criar_usuario(nome,email,generate_password_hash(senha))
        return redirect(url_for("auth.login"))

    return render_template("registro.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form['email']
        senha = request.form['senha']

        usuario = buscar_usuario_por_email(email)
        if not usuario or not check_password_hash(usuario.senha_hash, senha):
            flash("email ou senha errados")
            return redirect(url_for("auth.login"))

        session['usuario_id'] = usuario.id
        session['usuario_nome'] = usuario.nome
        return redirect(url_for("leituras.index"))

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    session.pop('usuario_id', None)
    session.pop('usuario_nome', None)
    flash("Complete o logout removendo os dados da session.")
    return redirect(url_for("auth.login"))
