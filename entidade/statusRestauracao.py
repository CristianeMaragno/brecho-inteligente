from entidade.status import Status

class StatusRestauracao(Status):
    def __init__(self, categorias, custo_total=None, responsavel=None):
        super().__init__()
        self.__id = super().gen_id()
        self.__custo_total = custo_total
        self.__responsavel = responsavel
        self.__categorias = categorias

    @property
    def categorias(self):
        return self.__categorias

    @property
    def custo_total(self):
        return self.__custo_total

    @property
    def responsavel(self):
        return self.__responsavel

    def __str__(self):
        return 'Em restauração'
