from limite.tela_padrao import TelaPadrao
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
        self.add_user_button = tk.Button(self.frame_menu,
                                         text="Cadastrar usuários",
                                         width=30,
                                         command=self.controlador.
                                         tela_criar_usuarios)
        self.add_user_button.pack(pady=10)

        # Button to open View User Screen
        self.view_users_button = tk.Button(self.frame_menu,
                                           text="Listar usuários",
                                           width=30,
                                           command=self.controlador.
                                           tela_usuarios)
        self.view_users_button.pack(pady=10)

        self.view_users_button = tk.Button(self.frame_menu,
                                           text="Menu peças",
                                           width=30,
                                           command=self.controlador.
                                           tela_menu_pecas)
        self.view_users_button.pack(pady=10)

    def menu_fun(self):

        self.view_users_button = tk.Button(self.frame_menu,
                                           text="Menu peças",
                                           width=30,
                                           command=self.controlador.
                                           tela_menu_pecas)
        self.view_users_button.pack(pady=10)

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