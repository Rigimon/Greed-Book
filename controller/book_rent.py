from flask import (
    Blueprint, render_template, request,        # separa o backend em arquivos diferentes, manda para a pagina html, faz uma requisição para pegar do formulario os dados
    redirect, url_for, session, flash           # leva o usuario para outra pagina, cria links que ativa funções de backend, cria sessoes de usuarios, envia mensagem do back end para o front end
)
from sqlalchemy.orm import sessionmaker             # Cria conexao com o database
from werkzeug.security import check_password_hash   # Compara as senhas criptografadas

from model.database import engine, Livro, Usuario, Emprestimo
from datetime import date

# Cria uma instancia do blueprint (isolamento da aplicação)
blueprint = Blueprint('book_rent', __name__)

Session = sessionmaker(bind=engine)

@blueprint.route("/list_rental")
def list_rental():
    if "user_id" in session:
        cursor = Session()
        emprestimos = cursor.query(Emprestimo).filter_by(ativo=1).all()
        cursor.close()
        table = []
        for emprestimo in emprestimos:
            leitor = cursor.query(Usuario).filter_by(id=emprestimo.id_usuario).first()
            livro = cursor.query(Livro).filter_by(id=emprestimo.id_livro).first()
            data = {"id":emprestimo.id,"leitor":leitor.nome,"livro":livro.titulo,"data_emprestimo":emprestimo.data_emprestimo,"data_devolucao_prev":emprestimo.data_devolucao_prev,"status":emprestimo.status}
            table.append(data)
        print(table)
        return render_template("list-rental.html",emprestimos=table)
    flash("Para acessar faça login", "warning")
    return redirect(url_for("user_autentication.login"))

@blueprint.route("/book_rental", methods=["POST","GET"])
def book_rental():
    if "user_id" in session:
        cursor = Session()
        if request.method == "POST":
            leitor = request.form.get("leitor")
            livro = request.form.get("livro")
            emprestimo = request.form.get("data_emprestimo")
            devolucao = request.form.get("data_devolucao")

            emprestimo = emprestimo.split("-")
            emprestimo = date(int(emprestimo[0]),int(emprestimo[1]),int(emprestimo[2]))

            devolucao = devolucao.split("-")
            devolucao = date(int(devolucao[0]),int(devolucao[1]),int(devolucao[2]))

            existe_livro = cursor.query(Livro).filter_by(id=int(livro)).first()
            existe_leitor = cursor.query(Usuario).filter_by(id=int(leitor)).first()
            if not existe_livro and not existe_leitor:
                
                flash("Leitor ou Livro não encontrado","danger")
                cursor.close()
                return redirect(url_for("book_tent.book_rental"))

            emp = Emprestimo(id_usuario=leitor,id_livro=livro,data_emprestimo=emprestimo,
                             data_devolucao_prev=devolucao,status="Emprestado")
            cursor.add(emp)
            cursor.commit()
            cursor.close()
            flash("Emprestimo cadastrado com sucesso", "success")
            return redirect(url_for("book_rent.list_rental"))
        livros = cursor.query(Livro).filter_by(ativo=1)
        leitores = cursor.query(Usuario).filter_by(ativo=1,tipo=1)
        return render_template("book-rental.html",livros=livros,leitores=leitores)
    flash("Para acessar faça login", "warning")
    return redirect(url_for("user_autentication.login"))

@blueprint.route("/book_loan")
def book_loan():
    return render_template("book-loan.html")

@blueprint.route("/list_loan")
def list_loan():...

