from entidade.status import Status


class StatusAVenda(Status):
    def __init__(self, preco):
        self.__preco = preco

    @property
    def preco(self):
        return self.__preco

    def __str__(self):
        return 'À venda'
