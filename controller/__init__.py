from flask import Flask                                 # Import o modulo do flask para a criação da aplicação
from datetime import date                               # Importa o tipo de dados date para a criação do usuario Master
from werkzeug.security import generate_password_hash    # Importa um modulo que cria um hash para a senha do usuario Master
from sqlalchemy.orm import sessionmaker                 # Importa um modulo para estabeler a sessão de conexão com o banco de dados

# Importa os módulos do back-end
from . import user_autentication
from . import user_management
from . import book_management
from . import book_rent

# importa banco de dados
from model.database import tabela, engine, Usuario

# importa a biblioteca para manipular o sistema operacional
import os

# Fnção que cria a aplicação do flask
def create_application():
    app = Flask(__name__, template_folder="../templates", static_folder="../static")
    
    # Chave de segurança
    app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", "123456")

    # Mapeia os arquivos de backend importatos
    app.register_blueprint(user_autentication.blueprint)
    app.register_blueprint(book_management.blueprint)
    app.register_blueprint(user_management.blueprint)
    app.register_blueprint(book_rent.blueprint)

    # Configurações de Cookies (HTTPS) - Serve para manter os dados armazenados no navegador de forma segura
    app.config["SESSION_COOK_SAMESITE"] = "Lax"
    app.config["SESSION_COOK_SECURE"] = True

    ## Criação de Banco de dados e usuário master ##
    # Converte o Python em sql
    try:
        tabela.metadata.create_all(engine)

        print("Banco de dados Talvez criado com sucesso!")
    except Exception as e:
        print("Erro:",e)

    # Configura a sessão de usuario
    Session = sessionmaker(bind=engine)

    cursor = Session()

    if not cursor.query(Usuario).filter_by(cpf="000.000.000-00").first():
        # Criando o ADM
        user = Usuario(nome="ADM", cpf="000.000.000-00", nascimento=date(2000,1,1), endereco="Servidor", telefone="00000000000", email="adm@greedbook.com", senha=generate_password_hash("abc123!!", method="pbkdf2:sha256"), tipo=0)
        
        # add o adm ao banco
        cursor.add(user)
        cursor.commit()
        cursor.close()

        ## feed back
        print("ADM criado com sucesso")

    # Retorna a aplicação
    return app
