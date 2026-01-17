from flask import (
    Blueprint, render_template, request,        # separa o backend em arquivos diferentes, manda para a pagina html, faz uma requisição para pegar do formulario os dados
    redirect, url_for, session, flash           # leva o usuario para outra pagina, cria links que ativa funções de backend, cria sessoes de usuarios, envia mensagem do back end para o front end
)
from sqlalchemy.orm import sessionmaker             # Cria conexao com o database

from model.database import engine, Livro

# Cria uma instancia do blueprint (isolamento da aplicação)
blueprint = Blueprint('book_management', __name__)

Session = sessionmaker(bind=engine)

@blueprint.route("/book_register", methods=["POST","GET"])
def book_register():
    if "user_id" in session:
        if request.method == "POST":
            isbn = request.form.get("isbn")
            titulo = request.form.get("titulo")
            autor = request.form.get("autor")
            editora = request.form.get("editora")
            edicao = request.form.get("edicao")
            volume = request.form.get("volume")
            genero = request.form.get("genero")
            paginas = request.form.get("paginas")
            ano_publicacao = request.form.get("ano_publicacao")
            qtde_exemplares = request.form.get("quantidade")

            cursor = Session()

            existe = cursor.query(Livro).filter_by(isbn=isbn).first()
            if existe:

                if existe.ativo == False:
                    existe.ativo = True
                    cursor.commit()
                    cursor.close()
                    flash("Livro cadastrado com sucesso","success")
                    return redirect(url_for("book_management.book_list"))

                flash("Esse ISBN do livro já esta cadastrado","danger")
                cursor.close()
                return redirect(url_for("book_management.book_register"))

            liv = Livro(isbn=isbn,titulo = titulo,autor=autor,
                        editora=editora,edicao=edicao,volume=int(volume),
                        genero=genero,paginas=int(paginas),ano_publicacao=int(ano_publicacao),
                        qtde_exemplares=qtde_exemplares)
            cursor.add(liv)
            cursor.commit()
            cursor.close()
            flash("Livro cadastrado com sucesso","success")
            return redirect(url_for("book_management.book_list"))
        return render_template("book-register.html")
    flash("Para acessar faça login", "warning")
    return redirect(url_for("user_autentication.login"))

@blueprint.route("/book_list")
def book_list():
    if "user_id" in session:
        cursor = Session()
        livros = cursor.query(Livro).filter_by(ativo=True).order_by(Livro.titulo).all()
        cursor.close()
        return render_template("book-list.html",livros=livros)
    flash("Para acessar faça login", "warning")
    return redirect(url_for("user_autentication.login"))

@blueprint.route("/edit_book/<string:isbn>", methods=["POST","GET"])
def edit_book(isbn):
    if "user_id" in session:
        cursor = Session()
        if request.method == "POST":
            liv = cursor.query(Livro).filter_by(isbn=isbn).first()
            liv.titulo = request.form.get("titulo")
            liv.autor = request.form.get("autor")
            liv.editora = request.form.get("editora")
            liv.edicao = request.form.get("edicao")
            liv.volume = int(request.form.get("volume"))
            liv.genero = request.form.get("genero")
            liv.paginas = int(request.form.get("paginas"))
            liv.ano_publicacao = int(request.form.get("ano_publicacao"))
            liv.qtde_exemplares = int(request.form.get("quantidade"))
            cursor.commit()
            cursor.close()
            flash("Livro atualizado com sucesso!","success")
            return redirect(url_for("book_management.book_list"))
        
        livro = cursor.query(Livro).filter_by(ativo=True,isbn=isbn).first()
        print(livro)
        cursor.close()
        return render_template("book-updater.html",livro=livro)
    flash("Para acessar faça login", "warning")
    return redirect(url_for("user_autentication.login"))

@blueprint.route("/delete_book/<string:isbn>", methods=['POST','GET'])
def delete_book(isbn):
    if "user_id" in session:
        cursor = Session()
        livro = cursor.query(Livro).filter_by(ativo=True,isbn=isbn).first()
        print(livro)
        if livro:
            livro.ativo = 0
            cursor.commit()
            flash("Livro deletado com sucesso", "success")
        else:
            flash("Livro não encontrado", "danger")
        cursor.close()
        return redirect(url_for("book_management.book_list"))
    flash("Para acessar faça login", "warning")
    return redirect(url_for("user_autentication.login"))
