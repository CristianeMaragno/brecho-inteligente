from status import Status

class statusRestauracao(Status):
    def __init__(self, custo_total, responsavel, categorias):
        self.__custo_total = custo_total
        self.__responsavel = responsavel
        self.__categorias = categorias
