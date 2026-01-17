from flask import (
    Blueprint, render_template, request,        # separa o backend em arquivos diferentes, manda para a pagina html, faz uma requisição para pegar do formulario os dados
    redirect, url_for, session, flash           # leva o usuario para outra pagina, cria links que ativa funções de backend, cria sessoes de usuarios, envia mensagem do back end para o front end
)
from sqlalchemy.orm import sessionmaker             # Cria conexao com o database
from werkzeug.security import check_password_hash   # Compara as senhas criptografadas

from model.database import engine, Usuario

# Cria uma instancia do blueprint (isolamento da aplicação)
blueprint = Blueprint('user_autentication', __name__)

Session = sessionmaker(bind=engine)

@blueprint.route("/",methods=["POST","GET"])
def login():
    if request.method == "POST":
        cpf = request.form.get("cpf")
        senha = request.form.get("senha")
        cursor = Session()
        usuario = cursor.query(Usuario.cpf, Usuario.senha, Usuario.nome, Usuario.id).filter_by(tipo=0,cpf=cpf,ativo=True).first()
        cursor.close()
        if usuario and cpf == usuario[0] and check_password_hash(usuario[1],senha):

            # grava informações do usuario em cookies do navegador
            session['user_id'] = usuario[3]
            session['username'] = usuario[2]
            return redirect(url_for("user_autentication.dashboard"))
        else:
    
            flash("Credenciais Inválidas", "danger")  # Manda a mensagem pro arrombado q n sabe digitar
            return redirect(url_for("user_autentication.login"))
    return render_template("index.html")

@blueprint.route("/logout")
def logout():
    session.clear()
    flash("Logout feito com sucesso", "success")
    return redirect(url_for("user_autentication.login"))

@blueprint.route("/dashboard")
def dashboard():
    if "user_id" in session:
        return render_template("dashboard.html")
    flash("Para acessar faça login", "warning")  # Manda a mensagem pro arrombado n hackear o site
    return redirect(url_for("user_autentication.login"))
