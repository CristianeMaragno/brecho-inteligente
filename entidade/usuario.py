class Usuario():
    def __init__(self, id: int, nome: str, email: str, senha: str, papel: int):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__senha = senha
        self.__papel = papel

    @property
    def identificador(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    @property
    def papel(self):
        return self.__papel

    @papel.setter
    def papel(self, papel):
        self.__papel = papel
