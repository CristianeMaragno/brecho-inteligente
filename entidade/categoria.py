class tipoRestauracao:
    LAVAR = 'Lavagem'
    PASSAR = 'Passar'
    REPARO = 'Reparo de danos'
    DETALHES = 'Restauração de detalhes'
    REMOCAO = 'Remocão de manchas'
    TINGIMENTO = 'Tingimento'
    CUSTOMIZACAO = 'Customização'

class Categoria:
    def __init__(self, id, tipo, custo: float):
        self.__id = id
        self.__tipo = tipo
        self.__custo = custo