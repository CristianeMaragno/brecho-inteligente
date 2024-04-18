class Peca:
    def __init__(self, id, descricao, status, custo_aquisicao, titulo=None, imagem=None, preco=None):
        self.__id = id
        self.__descricao = descricao
        self.__titulo = titulo or ''
        self.__status = status
        self.__custo_aquisicao = custo_aquisicao
        self.__imagem = imagem or 'assets/sem-imagem.png'
        self.__preco = preco or 0.0

    @property
    def id(self):
        return self.__id

    @property
    def custo_aquisicao(self):
        return self.__custo_aquisicao

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

    @property
    def preco(self):
        return self.__preco
