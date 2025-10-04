from .itemdoacervo import ItemDoAcervo
class Livro(ItemDoAcervo):

    def __init__(self, titulo:str, genero:str, editora:str, ano_publicacao:int, autor:str, isbn:str, numero_paginas:int, edicao:str = "", volume:str = ""):
        super().__init__(titulo, genero, editora, ano_publicacao, edicao, volume)
        self.autor = autor
        self.isbn = isbn
        self.numero_paginas = numero_paginas
    
    @property
    def autor(self) -> str:
        return self._autor
    
    @autor.setter
    def autor(self, novo:str):
        if novo.replace(" ","") != "":
            self._autor = novo
        else:
            self._autor = "Indefinido"
    
    @property
    def isbn(self) -> str:
        return self._isbn
    
    @isbn.setter
    def isbn(self, novo:str):
        if novo.replace(" ","") != "":
            self._isbn = novo
        else:
            self._isbn = "Indefinido"
    
    @property
    def numero_paginas(self) -> int:
        return self._numero_paginas
    
    @numero_paginas.setter
    def numero_paginas(self, novo:int):
        if novo > 0:
            self._numero_paginas = novo
        else:
            self._numero_paginas = 0
    
    def descrever(self):
        super().descrever()
        print(f"Autor: {self.autor}\nISBN: {self.isbn}\nNumero de Paginas: {self.numero_paginas}")