from abc import ABC, abstractmethod
import secrets
import string


class Status(ABC):
    def __init__(self):
        self.__id = self.gen_id()

    @abstractmethod
    def __str__(self):
        pass

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    def gen_id(self, tamanho=16):
        caracteres = string.ascii_letters + string.digits
        chave = ''.join(secrets.choice(caracteres) for _ in range(tamanho))
        return chave


