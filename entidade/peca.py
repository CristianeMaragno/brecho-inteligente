class Peca:
    def __init__(self,
                 id,
                 descricao,
                 status,
                 custo_aquisicao,
                 titulo=None,
                 imagem=None,
                 preco=None):
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
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, value):
        self.__descricao = value

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, value):
        self.__titulo = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    @property
    def custo_aquisicao(self):
        return self.__custo_aquisicao

    @custo_aquisicao.setter
    def custo_aquisicao(self, value):
        self.__custo_aquisicao = value

    @property
    def imagem(self):
        return self.__imagem

    @imagem.setter
    def imagem(self, value):
        self.__imagem = value

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, value):
        self.__preco = value
