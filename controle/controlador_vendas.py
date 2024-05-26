from limite.tela_menu import TelaMenu
from limite.tela_registrar_venda import TelaRegistrarVenda
from persistencia.peca_dao import PecaDAO
from entidade.peca import Peca
from entidade.status_tipos.statusRestauracao import StatusRestauracao


class ControladorVendas:

    def __init__(self, master, controlador, usuarios):
        self.master = master
        self.controlador = controlador
        self.usuarios = usuarios
        self.pecaDAO = PecaDAO()

    def abre_tela_registrar_venda(self):
        return TelaRegistrarVenda(self.master, self, self.controlador, self.usuarios)

    def voltar(self):
        self.usuario = None
        self.controlador.tela_menu()
    def abre_tela_menu(self):
        return TelaMenu(self.master, self.controlador, self)

    def pegar_peca_por_id(self, id):
        return self.pecaDAO.get_by_id(id)

    def realizar_pagamento(self, total, forma_pagamento, pecas):
        if total == 0 or forma_pagamento is None:
            return False

        #trocar status/atualizar preço da peça
        return True

    def altera_status_peca(self, peca):
        pass
