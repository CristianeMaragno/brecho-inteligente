from entidade.status_tipos.status import Status


class StatusRestauracao(Status):
    def __init__(self, categorias, id=None, custo_total=None):
        super().__init__()
        self.__id = id or super().gen_id()
        self.__custo_total = custo_total
        self.__categorias = categorias

    @property
    def categorias(self):
        return self.__categorias

    @property
    def custo_total(self):
        return self.__custo_total

    @property
    def id(self):
        return self.__id

    @categorias.setter
    def categorias(self, categorias):
        self.__categorias = categorias

    @id.setter
    def id(self, id):
        self.__id = id

    @custo_total.setter
    def custo_total(self, custo_total):
        self.__custo_total = custo_total

    def __str__(self):
        return 'Em restauração'

