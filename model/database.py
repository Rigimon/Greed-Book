from sqlalchemy import (
    create_engine, Column, ForeignKey,                      # Criar Colunas, chaves estrangeiras
    Integer, String, Date, Text, Boolean                    # Tipos de Dados
)

# Importação do ORM (Object Relational Mapping) do SQL Alchemy
from sqlalchemy.orm import(
    declarative_base,                                       # Modulo que cria tabela de bd usando notação de OO
    relationship                                            # cria relações forward
)

import os

# Realiza a configuração do bd.
database_path = f"sqlite:///{os.environ.get('DATA_DIR')}"
engine = create_engine(database_path)

# Faz o SQlite interpretar cada classe do python como uma tabela do bd
tabela = declarative_base()

# Define uma tabela para armazenar as informações do aluno
class Usuario(tabela):

    #Nome da tabela
    __tablename__ = "usuario"

    # Atributos
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    cpf = Column(String(14), unique=True, nullable=False)
    nascimento = Column(Date, nullable=False)
    endereco = Column(String(200), nullable=False)
    telefone = Column(String(20), nullable=False)
    email = Column(String(100), nullable=False)
    senha = Column(String(255), nullable=False)
    tipo = Column(Integer, nullable=False)
    ativo = Column(Boolean, default=True)

    # Definir Relacionamento
    emprestimo = relationship("Emprestimo", back_populates="usuario")

    # Método que exibe todas as informações registradas
    def __repr__(self):
        return f"Usuario: {self.nome}, {self.cpf}, {self.email}, {self.tipo}"

# Define uma tabela para armazenar as informações do curso
class Livro(tabela):

    #Nome da tabela
    __tablename__ = "livro"

    # Atributos
    id = Column(Integer, primary_key=True)
    isbn = Column(String(20), unique=True, nullable=False)
    titulo = Column(String(100), nullable=False)
    autor = Column(Text, nullable=False)
    editora = Column(String(100), nullable=False)
    edicao = Column(String(50), nullable=True)
    volume = Column(Integer, nullable=True)
    genero = Column(String(100), nullable=False)
    paginas = Column(Integer, nullable=False)
    ano_publicacao = Column(Integer, nullable=False)
    qtde_exemplares = Column(Integer, nullable=True)
    ativo = Column(Boolean, default=True)

    # Definir Relacionamento
    emprestimo = relationship("Emprestimo", back_populates="livro")

    # Método que exibe todas as informações registradas
    def __repr__(self):
        return f"Livro: {self.titulo}, {self.autor}"

# Define uma tabela para armazenar as informações do curso
class Emprestimo(tabela):

    #Nome da tabela
    __tablename__ = "emprestimo"

    # Atributos
    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey("usuario.id"), nullable=False)
    id_livro = Column(Integer, ForeignKey("livro.id"),nullable=False)
    data_emprestimo = Column(Date, nullable=False)
    data_devolucao_prev = Column(Date, nullable=False)
    status = Column(String(20), nullable=False)
    ativo = Column(Boolean, default=True)

    # Definir Relacionamento
    usuario = relationship("Usuario", back_populates="emprestimo")
    livro = relationship("Livro", back_populates="emprestimo")

    # Método que exibe todas as informações registradas
    def __repr__(self):
        return f"Emprestimo: {self.id} - Usuario: {self.id_usuario} - Livro: {self.id_livro}"
