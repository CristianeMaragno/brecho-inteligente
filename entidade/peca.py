class Peca:
    def __init__(self, id, descricao, status, imagem=None, titulo=None, preco=None):
        self.__id = id
        self.__descricao = descricao
        self.__titulo = titulo
        self.__status = status
        self.__imagem = imagem or 'assets/sem-imagem.png'
        self.__preco = preco

    @property
    def id(self):
        return self.__id

    @property
    def descricao(self):
        return self.__descricao

    @property
    def titulo(self):
        return self.__titulo

    @property
    def status(self):
        return self.__status

    @property
    def imagem(self):
        return self.__imagem


