class Peca:
    def __init__(self, id, titulo, status, imagem=None, preco=None):
        self.__id = id
        self.__titulo = titulo
        self.__status = status
        self.__imagem = imagem or 'assets/sem-imagem.png'
        self.__preco = preco

    @property
    def id(self):
        return self.__id


