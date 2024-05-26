import tkinter as tk
from limite.tela_catalogo import TelaCatalogo
from persistencia.usuario_dao import UsuarioDAO
from controle.controlador_usuarios import ControladorUsuarios
from controle.controlador_peca import ControladorPeca
from controle.controlador_calculadora import ControladorCalculadora


class ControladorSistema:

    def __init__(self, root):
        self.root = root
        self.root.geometry("800x800")
        self.__controlador_usuarios = ControladorUsuarios(self.root, self)
        self.__controlador_pecas = ControladorPeca(self.root, self)
        self.__controlador_calculadora = ControladorCalculadora(self.root, self)
        self.tela_atual = None

    def criar_adm_padrao(self):
        if UsuarioDAO().pegar_por_nome("Administrador Padrão"):
            None
        else:
            self.controlador_usuarios.criar_usuario(
                0, "Administrador Padrão", "adm0", "0", 1, False
            )

    def tela_catalogo(self):
        if self.tela_atual:
            self.tela_atual.pack_forget()

        self.tela_atual = TelaCatalogo(self.root, self, self.controlador_usuarios)
        self.tela_atual.pack(fill=tk.BOTH, expand=True)

    def tela_usuarios(self):
        if self.tela_atual:
            self.tela_atual.pack_forget()

        self.tela_atual = self.__controlador_usuarios.abre_tela_usuario()
        self.tela_atual.pack()

    def tela_menu_pecas(self):
        if self.tela_atual:
            self.tela_atual.pack_forget()

        self.tela_atual = self.__controlador_pecas.tela_menu()

    def tela_criar_usuarios(self):
        if self.tela_atual:
            self.tela_atual.pack_forget()

        self.tela_atual = self.__controlador_usuarios.abre_tela_criar_usuario()
        self.tela_atual.pack()

    def tela_login(self, erro=None):
        if self.tela_atual:
            self.tela_atual.pack_forget()

        self.tela_atual = self.__controlador_usuarios.abre_tela_login(erro)
        self.tela_atual.pack(fill=tk.BOTH, expand=True)

    def deslogar(self):
        if self.tela_atual:
            self.tela_atual.pack_forget()

        self.controlador_usuarios.deslogar_usuario()

        self.tela_atual = self.__controlador_usuarios.abre_tela_login("")
        self.tela_atual.pack(fill=tk.BOTH, expand=True)

    def tela_menu(self):
        if self.tela_atual:
            self.tela_atual.pack_forget()
    
        self.tela_atual = self.controlador_usuarios.abre_tela_menu()
        self.tela_atual.pack(fill=tk.BOTH, expand=True)

    def tela_calculadora(self):
        if self.tela_atual:
            self.tela_atual.pack_forget()
    
        self.tela_atual = self.controlador_calculadora.abre_tela_calculadora()
        self.tela_atual.pack(fill=tk.BOTH, expand=True)

    @property
    def controlador_usuarios(self):
        return self.__controlador_usuarios

    @property
    def controlador_calculadora(self):
        return self.__controlador_calculadora

    def encerra_sistema(self):
        exit(0)
    

