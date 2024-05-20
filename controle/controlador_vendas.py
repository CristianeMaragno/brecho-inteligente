from limite.tela_menu import TelaMenu
from limite.tela_registrar_venda import TelaRegistrarVenda
from persistencia.peca_dao import PecaDAO


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

    def realizar_pagamento(self, total):
        #trocar status/atualizar preço da peça
        return 1
