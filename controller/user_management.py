from flask import (
    Blueprint, render_template, request,        # separa o backend em arquivos diferentes, manda para a pagina html, faz uma requisição para pegar do formulario os dados
    redirect, url_for, session, flash           # leva o usuario para outra pagina, cria links que ativa funções de backend, cria sessoes de usuarios, envia mensagem do back end para o front end
)
from sqlalchemy.orm import sessionmaker             # Cria conexao com o database

from model.database import engine, Usuario
from datetime import date

# Cria uma instancia do blueprint (isolamento da aplicação)
blueprint = Blueprint('user_management', __name__)

Session = sessionmaker(bind=engine)

cursor = Session()

@blueprint.route("/user_register", methods=["POST","GET"])
def user_register():
    if "user_id" in session:
        if request.method == "POST":
            nome = request.form.get("nome")
            cpf = request.form.get("cpf")
            nascimento = request.form.get("data_nascimento")
            endereco = request.form.get("endereco")
            telefone = request.form.get("telefone")
            email = request.form.get("email")
            tipo = int(request.form.get("tipo_usuario"))
            nascimento = nascimento.split("-")
            nascimento = date(int(nascimento[0]),int(nascimento[1]),int(nascimento[2]))
            cursor = Session()

            existe = cursor.query(Usuario).filter_by(cpf=cpf).first()
            if existe:

                if existe.ativo == False:
                    existe.ativo = True
                    cursor.commit()
                    cursor.close()
                    flash("Usuario cadastrado com sucesso","success")
                    return redirect(url_for("user_management.user_list"))
                
                flash("Esse CPF do usuário já esta cadastrado","danger")
                cursor.close()
                return redirect(url_for("user_management.user_register"))

            user = Usuario(nome=nome,cpf = cpf,nascimento=nascimento,
                        endereco=endereco,telefone=telefone,email=email, senha=str(nascimento).replace("-","/"),
                        tipo=tipo)
            cursor.add(user)
            cursor.commit()
            cursor.close()
            flash("Usuario cadastrado com sucesso","success")
            return redirect(url_for("user_management.user_list"))
        return render_template("user-register.html")
    flash("Para acessar faça login", "warning")
    return redirect(url_for("user_autentication.login"))

@blueprint.route("/user_list", methods=["POST","GET"])
def user_list():
    usuarios = cursor.query(Usuario).filter_by(ativo=True).all()
    return render_template("user-list.html",usuarios=usuarios)

@blueprint.route("/edit_user/<string:cpf>", methods=["POST","GET"])
def edit_user(cpf):
    if "user_id" in session:
        cursor = Session()
        if request.method == "POST":
            user = cursor.query(Usuario).filter_by(cpf=cpf).first()
            user.nome = request.form.get("nome")
            nascimento = request.form.get("data_nascimento").split("-")
            user.nascimento = date(int(nascimento[0]),int(nascimento[1]),int(nascimento[2]))
            user.endereco = request.form.get("endereco")
            user.telefone = request.form.get("telefone")
            user.email = request.form.get("email")
            user.tipo = int(request.form.get("tipo_usuario"))
            cursor.commit()
            cursor.close()
            flash("Usuario atualizado com sucesso!","success")
            return redirect(url_for("user_management.user_list"))
        
        usuario = cursor.query(Usuario).filter_by(ativo=True,cpf=cpf).first()
        cursor.close()
        return render_template("user-updater.html",usuario=usuario)
    flash("Para acessar faça login", "warning")
    return redirect(url_for("user_autentication.login"))

@blueprint.route("/delete_user/<string:cpf>")
def delete_user(cpf):
    if "user_id" in session:
        cursor = Session()
        user = cursor.query(Usuario).filter_by(ativo=True,cpf=cpf).first()
        print(user)
        if user:
            user.ativo = 0
            cursor.commit()
            flash("Usuario deletado com sucesso", "success")
        else:
            flash("Usuario não encontrado", "danger")
        cursor.close()
        return redirect(url_for("user_management.user_list"))
    flash("Para acessar faça login", "warning")
    return redirect(url_for("user_autentication.login"))
