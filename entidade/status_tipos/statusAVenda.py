from entidade.status_tipos.status import Status


class StatusAVenda(Status):
    def __init__(self, vendido=False, id=None, desconto=None, forma_pagamento=None):
        super().__init__()
        self.__id = id or super().gen_id()
        self.__vendido = vendido
        self.__desconto = desconto
        self.__forma_pagamento = forma_pagamento

    @property
    def vendido(self):
        return self.__vendido

    @property
    def id(self):
        return self.__id

    @property
    def desconto(self):
        return self.__desconto

    @property
    def forma_pagamento(self):
        return self.__forma_pagamento

    @id.setter
    def id(self, id):
        self.__id = id

    @vendido.setter
    def vendido(self, vendido):
        self.__vendido = vendido

    @desconto.setter
    def desconto(self, desconto):
        self.__desconto = desconto

    @forma_pagamento.setter
    def forma_pagamento(self, forma_pagamento):
        self.__forma_pagamento = forma_pagamento

    def __str__(self):
        return "À venda"
