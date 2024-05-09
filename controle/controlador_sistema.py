import limite
import tkinter as tk
from limite.tela_sistema import TelaSistema
from limite.tela_catalogo import TelaCatalogo
from persistencia.usuario_dao import UsuarioDAO
from controle.controlador_usuarios import ControladorUsuarios
from controle.controlador_peca import ControladorPeca


class ControladorSistema:

    def __init__(self, root):
        self.root = root
        self.root.geometry("600x600")
        self.__controlador_usuarios = ControladorUsuarios(self.root, self)
        self.__controlador_pecas = ControladorPeca(self.root, self)
        self.tela_atual = None

    def criar_adm_padrao(self):
        if UsuarioDAO().pegar_por_nome("Administrador Padrão"):
            None
        else:
            self.controlador_usuarios.criar_usuario(
                0, "Administrador Padrão", "adm0", "0", 1, False
            )

    def tela_sistema(self):
        if self.tela_atual:
            self.tela_atual.pack_forget()

        self.tela_atual = TelaSistema(self.root, self)
        self.tela_atual.pack(fill=tk.BOTH, expand=True)

    def tela_catalogo(self, master):
        if isinstance(self.tela_atual, (limite.tela_catalogo.TelaCatalogo, limite.tela_sistema.TelaSistema)):
            pass #caso já esteja na tela de catálogo não acontece nada

        else:
            if self.tela_atual:
                self.tela_atual.pack_forget()
            
            self.tela_atual = TelaCatalogo(master, self)
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
        if (isinstance(self.tela_atual, (limite.tela_login.TelaLogin)) 
            and self.tela_atual.mensagem_erro == erro):
            pass #caso já esteja na tela de login não acontece nada

        else:
            if self.tela_atual:
                self.tela_atual.pack_forget()

            self.tela_atual = self.__controlador_usuarios.abre_tela_login(erro)
            self.tela_atual.pack()

    def deslogar(self):
        if self.tela_atual:
            self.tela_atual.pack_forget()

        self.controlador_usuarios.deslogar_usuario()

        self.tela_atual = self.__controlador_usuarios.abre_tela_login("")
        self.tela_atual.pack()

    @property
    def controlador_usuarios(self):
        return self.__controlador_usuarios

    def encerra_sistema(self):
        exit(0)