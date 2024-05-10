from limite.tela_padrao import TelaPadrao
from controle.controlador_peca import ControladorPeca
import tkinter as tk
import ttkbootstrap as ttk

class TelaMenu(TelaPadrao):
    def __init__(self, master, controlador, controladorUsuario):
        super().__init__(master, controlador, controladorUsuario)
    
    def conteudo(self):
        papel = self.controladorUsuario.usuario_logado.papel
        if papel == 1:
            self.frame()
            self.menu_adm()
        elif papel == 2:
            self.frame()
            self.menu_fun()
        else:
            self.controladorUsuario.usuario_logado = None
            self.controlador.catalogo()
        
    def menu_adm(self):
         # Button to open User Creation Screen
        self.add_user_button = ttk.Button(self.frame_menu,
                                         text="Cadastrar usuários",
                                         width=30,
                                         command=self.controlador.
                                         tela_criar_usuarios)
        self.add_user_button.pack(padx=10, pady=10)

        # Button to open View User Screen
        self.view_users_button = ttk.Button(self.frame_menu,
                                           text="Listar usuários",
                                           width=30,
                                           command=self.controlador.
                                           tela_usuarios)
        self.view_users_button.pack(padx=10, pady=10)

        self.menu_fun()

    def menu_fun(self):

        self.button1 = ttk.Button(
            self.frame_menu,
            text="Registrar",
            #command=self.controller.tela_registrar,
            width=30,
        )
        self.button1.pack(padx=10, pady=10)

        self.button2 = ttk.Button(
            self.frame_menu,
            text="Update",
            #command=self.controller.tela_update,
            width=30,
        )
        self.button2.pack(padx=10, pady=10)

        self.button3 = ttk.Button(
            self.frame_menu,
            text="Apagar",
            #command=self.controller.tela_apagar,
            width=30,
        )
        self.button3.pack(padx=10, pady=10)

        self.button4 = ttk.Button(
            self.frame_menu,
            text="Mostrar",
            #command=self.controller.tela_mostrar,
            width=30,
        )
        self.button4.pack(padx=10, pady=10)

        # self.button5 = ttk.Button(
        #     self.frame_menu,
        #     text="Retornar",
        #     #command=self.controller.voltar,
        #     width=30,
        # )
        # self.button5.pack(padx=10, pady=10)

    def frame(self):
        self.frame_menu = ttk.Frame(self,
                                width=770,
                                height=608,
                                padding=20,
                                style='light')

        self.frame_menu.pack(fill="none",
                         expand=False,
                         pady=32)

        self.titulo = ttk.Label(self.frame_menu,
                                 text="MENU",
                                 style="inverse-light",
                                 font=("Helvetica", 14, "bold"))
        self.titulo.pack(pady=10)