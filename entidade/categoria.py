class Categorias:

    tipos = {
        "LAVAR": 'Lavagem',
        "PASSAR": 'Passar',
        "REPARO": 'Reparo de danos',
        "DETALHES": 'Restauração de detalhes',
        "REMOCAO": 'Remocão de manchas',
        "TINGIMENTO": 'Tingimento',
        "CUSTOMIZACAO": 'Customização',
        "NENHUM": 'Nenhum ajuste'
    }

class Categoria:
    def __init__(self, id, nome, custo_padrao, feito=False):
        self.__id = id
        self.__nome = nome
        self.__custo_padrao = custo_padrao
        self.__feito = feito

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def custo_padrao(self):
        return self.__custo_padrao

    @custo_padrao.setter
    def custo_padrao(self, custo_padrao):
        self.__custo_padrao = custo_padrao

    @property
    def feito(self):
        return self.__feito

    @feito.setter
    def feito(self, feito):
        self.__feito = feito