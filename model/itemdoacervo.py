class ItemDoAcervo:

    def __init__(self, titulo:str, genero:str, editora:str, ano_publicacao:int, edicao:str="", volume:str=""):
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao
        self.edicao = edicao
        self.editora = editora
        self.volume = volume
        self.genero = genero
        self.disponivel = True

    @property
    def titulo(self) -> str:
        return self._titulo

    @titulo.setter
    def titulo(self, novo:str):
        if novo.replace(" ","") != "":
            self._titulo = novo
        else:
            self._titulo = "Indefinido"
    
    @property
    def genero(self) -> str:
        return self._genero

    @genero.setter
    def genero(self, novo:str):
        if novo.replace(" ","") != "":
            self._genero = novo
        else:
            self._genero = "Indefinido"

    @property
    def editora(self) -> str:
        return self._editora

    @editora.setter
    def editora(self, novo:str):
        if novo.replace(" ","") != "":
            self._editora = novo
        else:
            self._editora = "Indefinido"

    @property
    def ano_publicacao(self) -> int:
        return self._ano_publicacao

    @ano_publicacao.setter
    def ano_publicacao(self, novo:int):
        if novo > 0:
            self._ano_publicacao = novo
        else:
            self._ano_publicacao = None
    
    @property
    def edicao(self) -> str:
        return self._edicao

    @edicao.setter
    def edicao(self, novo:str):
        if novo.replace(" ","") != "":
            self._edicao = novo
        else:
            self._edicao = "Indefinido"
    
    @property
    def volume(self) -> str:
        return self._volume

    @volume.setter
    def volume(self, novo:str):
        if novo.replace(" ","") != "":
            self._volume = novo
        else:
            self._volume = "Indefinido"
    
    @property
    def disponivel(self) -> bool:
        return self._disponivel

    @disponivel.setter
    def disponivel(self, novo:bool):
        if isinstance(novo, bool):
            self._disponivel = novo
        else:
            self._disponivel = True
    
    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
        else:
            print(f"{self.titulo} já foi emprestado")
    
    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
        else:
            print(f"{self.titulo} já foi devolvido")
    
    def descrever(self):
        disponiblidade = "Disponivel" if self.disponivel else "Indisponivel" 
        print(f"-----<<{self.__class__.__name__}>>-----")
        print(f"Titulo: {self.titulo}\nGenero: {self.genero}\nEditora: {self.editora}\nEdição: {self.edicao}\nVolume: {self.volume}\nAno Publicação: {self.ano_publicacao}\nDisponibilidade: {disponiblidade}")