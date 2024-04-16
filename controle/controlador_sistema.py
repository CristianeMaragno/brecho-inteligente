from limite.tela_sistema import TelaSistema
from controle.controlador_usuarios import ControladorUsuarios

class ControladorSistema:

    def __init__(self):
        self.__controlador_usuarios = ControladorUsuarios(self)
        self.__tela_sistema = TelaSistema()

    def inicializa_sistema(self):
        self.abre_tela()

    def abre_tela(self):
        lista_opcoes_usuario_logado = {1: self.tela_usuarios, 0: self.encerra_sistema}

        lista_opcoes_usuario_deslogado = {}

        while True:
            if self.__controlador_usuarios.usuario_logado:
                opcao_escolhida = self.__tela_sistema.tela_opcoes_usuario_logado(self.__controlador_usuarios.usuario_logado.nome)
                funcao_escolhida = lista_opcoes_usuario_logado[opcao_escolhida]
                funcao_escolhida()
            else:
                opcao_escolhida = self.__tela_sistema.tela_opcoes_usuario_deslogado()
                funcao_escolhida = lista_opcoes_usuario_deslogado[opcao_escolhida]
                funcao_escolhida()

    def tela_usuarios(self):
        self.__controlador_usuarios.abre_tela_usuario()


    @property
    def controlador_usuarios(self):
        return self.__controlador_usuarios

    def encerra_sistema(self):
        exit(0)
