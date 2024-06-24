from entidade.status_tipos.status import Status


class StatusReserva(Status):
    def __init__(self, nome, telefone, data, id=None):
        self.__id = id or super().gen_id()
        self.__nome = nome
        self.__telefone = telefone
        self.__data = data
        super().__init__()

    @property
    def nome(self):
        return self.__nome

    @property
    def id(self):
        return self.__id

    @property
    def telefone(self):
        return self.__telefone

    @property
    def data(self):
        return self.__data

    @id.setter
    def id(self, id):
        self.__id = id

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @data.setter
    def data(self, data):
        self.__data = data

    def __str__(self):
        return "Reservada"
