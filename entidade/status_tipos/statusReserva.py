from entidade.status_tipos.status import Status

class StatusReserva(Status):
    def __init__(self, nome, telefone, id=None):
        super().__init__()
        self.__id = id or super().gen_id()
        self.__nome = nome
        self.__telefone = telefone

    @property
    def nome(self):
        return self.__nome

    @property
    def id(self):
        return self.__id

    @property
    def telefone(self):
        return self.__telefone

    @id.setter
    def id(self, id):
        self.__id = id

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    def __str__(self):
        return "Reserva"
