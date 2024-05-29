from limite.tela_menu import TelaMenu
from limite.tela_registrar_venda import TelaRegistrarVenda
from entidade.peca import Peca
from entidade.status_tipos.statusRestauracao import StatusRestauracao

class ControladorVendas:

    def __init__(self, master, controlador, controlador_usuarios):
        self.master = master
        self.controlador = controlador
        self.controlador_usuarios = controlador_usuarios
        self.__tela_registrar_venda = None

    def abre_tela_registrar_venda(self):
        self.__tela_registrar_venda = TelaRegistrarVenda(self.master, self, self.controlador, self.controlador_usuarios)
        return self.__tela_registrar_venda

    def voltar(self):
        self.usuario = None
        self.controlador.tela_menu()
    def abre_tela_menu(self):
        return TelaMenu(self.master, self.controlador, self)

    def pegar_peca_por_id(self, id):
        controlador_pecas = self.controlador.controlador_pecas
        return controlador_pecas.get_peca(id)

    def realizar_pagamento(self, total, forma_pagamento, pecas):
        if total == 0 or forma_pagamento is None:
            return False

        controlador_pecas = self.controlador.controlador_pecas

        for peca in pecas:
            dados_update = {
                'id': peca["id"],
                'custo_aquisicao': peca["custo_aquisicao"],
                'descricao': peca["descricao"],
                'status': 'a_venda',
                'ajustes': [],
                'imagem': peca["imagem"],
                'titulo': peca["titulo"],
                'preco': peca["preco"]
            }

            dadosVenda = {
                'desconto': peca["desconto"],
                'forma_pagamento': forma_pagamento
            }
            controlador_pecas.update(dados_update, dadosVenda)
        return True
