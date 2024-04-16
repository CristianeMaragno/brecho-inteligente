from status import Status
from datetime import date

class statusReservada(Status):
    def __init__(self, nome, telefone, data_limite: date):
        self.__nome = nome
        self.__telefone = telefone
        self.__data_limite = data_limite
