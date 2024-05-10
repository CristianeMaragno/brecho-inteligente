from limite.tela_padrao import TelaPadrao
import tkinter as tk
import ttkbootstrap as ttk

class TelaMenu(TelaPadrao):
    def __init__(self, master, controlador, controladorUsuario):
        super().__init__(master, controlador, controladorUsuario)
    
    def conteudo(self):
        papel = self.controladorUsuario.usuario_logado.papel
        if papel == 1:
            self.menu_adm()
        elif papel == 2:
            self.menu_fun()
        else:
            self.controladorUsuario.usuario_logado = None
            self.controlador.catalogo()
        
    def menu_adm(self):
         # Button to open User Creation Screen
        self.add_user_button = tk.Button(
            self,
            text="Cadastrar usuários",
            command=self.controlador.tela_criar_usuarios,
        )
        self.add_user_button.pack(pady=10)

        # Button to open View User Screen
        self.view_users_button = tk.Button(self,
                                           text="Listar usuários",
                                           command=self.controlador.
                                           tela_usuarios)
        self.view_users_button.pack(pady=10)

        self.view_users_button = tk.Button(
            self, text="Menu peças", command=self.controlador.tela_menu_pecas
        )
        self.view_users_button.pack(pady=10)

        # Button to logout
        self.logout = tk.Button(self,
                                text="Logout",
                                command=self.controlador.deslogar)
        self.logout.pack(pady=10)

    def menu_fun(self):
        self.view_users_button = tk.Button(
            self, text="Menu peças", command=self.controlador.tela_menu_pecas
        )
        self.view_users_button.pack(pady=10)
        self.logout = tk.Button(self,
                                text="Logout",
                                command=self.controlador.deslogar)
        self.logout.pack(pady=10)