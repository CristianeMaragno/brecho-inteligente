from entidade.status import Status


class StatusAVenda(Status):
    def __init__(self, preco):
        super().__init__()
        self.__id = super().gen_id()
        self.__preco = preco

    @property
    def preco(self):
        return self.__preco

    def __str__(self):
        return 'À venda'
