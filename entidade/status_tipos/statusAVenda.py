from entidade.status_tipos.status import Status


class StatusAVenda(Status):
    def __init__(self, vendido=False, id=None):
        super().__init__()
        self.__id = id or super().gen_id()
        self.__vendido = vendido

    @property
    def vendido(self):
        return self.__vendido

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @vendido.setter
    def vendido(self, vendido):
        self.__vendido = vendido

    def __str__(self):
        return 'À venda'
