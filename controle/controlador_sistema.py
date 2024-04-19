from limite.tela_sistema import TelaSistema
from controle.controlador_usuarios import ControladorUsuarios

class ControladorSistema:

    def __init__(self, root):
        self.root = root
        self.__controlador_usuarios = ControladorUsuarios(self.root, self)
        self.tela_atual = None


    def tela_sistema(self):
        if self.tela_atual:
            self.tela_atual.pack_forget()

        self.tela_atual = TelaSistema(self.root, self)
        self.tela_atual.pack()

    def tela_usuarios(self):
        if self.tela_atual:
            self.tela_atual.pack_forget()

        self.tela_atual = self.__controlador_usuarios.abre_tela_usuario()
        self.tela_atual.pack()

    def tela_criar_usuarios(self):
        if self.tela_atual:
            self.tela_atual.pack_forget()

        self.tela_atual = self.__controlador_usuarios.abre_tela_criar_usuario()
        self.tela_atual.pack()

    @property
    def controlador_usuarios(self):
        return self.__controlador_usuarios

    def encerra_sistema(self):
        exit(0)
