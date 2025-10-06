# from model import Livro
# from model import Revista

# print("1 - livro")
# print("2 - revista")
# esc = 1#int(input("qual vc deseja cadastrar"))

# titulo = "Harry potter"#input("Digite o titulo: ")
# genero = "Ficção"#input("Digite o Genero: ")
# editora = ""#input("Digite a Editora: ")
# ano_publicacao = 1#int(input("Digite o ano de publicação: "))
# edicao = ""#input("Digite a Edição: ")
# volume = ""#input("Digite o Volume: ")

# match esc:
#     case 1:
#         autor = "J. K. Rolling"#input("Digite o Autor: ")
#         isbn = "11111"#input("Digite o ISBN: ")
#         numero_pagina = 350#int(input("Digite o número de paginas: "))
#         item = Livro(titulo,genero,editora,ano_publicacao,autor,isbn,numero_pagina,edicao,volume)
#     case 2:
#         issn = input("Digite a ISSN: ")
#         mes_publicacao = input("Digite o mes de publicação: ")
#         item = Revista(titulo,genero,editora,ano_publicacao,issn,mes_publicacao,edicao,volume)

# item.descrever()

from controller import create_application
from sqlalchemy import create_engine

# Cria uma instancia da web
app = create_application()

if __name__ == "__main__":
    app.run(debug=True)
