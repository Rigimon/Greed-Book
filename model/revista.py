from .itemdoacervo import ItemDoAcervo

class Revista(ItemDoAcervo):

    def __init__(self, titulo:str, genero:str, editora:str, ano_publicacao:int, issn:str, mes_publicacao:str, edicao:str = "", volume:str = ""):
        super().__init__(titulo, genero, editora, ano_publicacao, edicao, volume)
        self.issn = issn
        self.mes_publicacao = mes_publicacao
    
    @property
    def issn(self) -> str:
        return self._issn
    
    @issn.setter
    def issn(self, novo:str):
        if novo.replace(" ","") != "":
            self._issn = novo
    
    @property
    def mes_publicacao(self) -> str:
        return self._mes_publicacao
    
    @mes_publicacao.setter
    def mes_publicacao(self, novo:str):
        if novo.replace(" ","") != "":
            self._mes_publicacao = novo
    
    def descrever(self):
        super().descrever()
        print(f"ISSN: {self.issn}\nMes de Publicação: {self.mes_publicacao}")