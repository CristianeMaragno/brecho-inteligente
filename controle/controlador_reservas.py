from limite.tela_menu import TelaMenu
from limite.tela_reserva import TelaReserva
from entidade.status_tipos.statusReserva import StatusReserva

class ControladorReservas:

    def __init__(self, master, controlador, controlador_usuarios):
        self.master = master
        self.controlador = controlador
        self.controlador_usuarios = controlador_usuarios
        self.__tela_reserva= None

    def abre_tela_reserva(self):
        self.__tela_reserva = TelaReserva(self.master, self, self.controlador, self.controlador_usuarios)
        return self.__tela_reserva

    def voltar(self):
        self.controlador.tela_menu()
    def abre_tela_menu(self):
        return TelaMenu(self.master, self.controlador, self)

    def pegar_peca_por_id(self, id):
        controlador_pecas = self.controlador.controlador_pecas
        return controlador_pecas.get_peca(id)

    def realizar_reserva(self, nome, telefone, data, pecas):
        if nome is None or telefone is None:
            return False

        controlador_pecas = self.controlador.controlador_pecas

        dadosReserva = {
            'nome': nome,
            'telefone': telefone,
            'data': data
        }

        for peca in pecas:
            dados_update = {
                'id': peca["id"],
                'custo_aquisicao': peca["custo_aquisicao"],
                'descricao': peca["descricao"],
                'status': 'reserva',
                'ajustes': [],
                'imagem': peca["imagem"],
                'titulo': peca["titulo"],
                'preco': peca["preco"]
            }
            controlador_pecas.update(dados_update, None, dadosReserva)

        return True

    def pegar_reservas(self):
        controlador_pecas = self.controlador.controlador_pecas
        pecas = controlador_pecas.get_todas_pecas()

        reservas = []

        for peca in pecas:
            if isinstance(peca.status, StatusReserva):
                reservas.append(
                    {
                        'id': peca.id,
                        'nome': peca.status.nome,
                        'telefone': peca.status.telefone,
                        'data': peca.status.data,
                    }
                )

        return reservas