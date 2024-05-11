import tkinter as tk
import ttkbootstrap as ttk
from abc import ABC, abstractmethod
from ttkbootstrap import Style


class TelaPadrao(ABC, tk.Frame):
    def __init__(self, master, controlador, controladorUsuario):
        super().__init__(master)
        self.controlador = controlador
        self.style = Style(theme="cerculean")
        self.pack(fill=tk.BOTH, expand=True)
        self.controladorUsuario = controladorUsuario
        self.master = master

        self.tela()

    def tela(self):
        self.criar_navbar()

        self.conteudo()

        # Footer
        self.footer_frame = ttk.Frame(self, style="primary.TFrame", padding=2)
        self.footer_frame.pack(side="bottom", fill="x")

        self.footer_label = ttk.Label(
            self.footer_frame,
            text="INE5608 - Análise e Projeto de Sistemas (04238B)",
            style="primary.inverse.TLabel",
            padding=2,
        )
        self.footer_label.pack()

    @abstractmethod
    def conteudo(self):
        pass

    def abrir_catalogo(self):
        self.controlador.tela_catalogo()

    def criar_navbar(self):
        navbar_frame = ttk.Frame(self, style="primary.TFrame", padding=10)
        navbar_frame.pack(side="top", fill="x")

        brecho_button = ttk.Button(navbar_frame,
                                   text="Brechó inteligente",
                                   style="primary.TButton",
                                   command=self.abrir_catalogo)
        brecho_button.pack(side="left", padx=5)

        if self.controladorUsuario.usuario_logado:
            menu_button = ttk.Button(navbar_frame,
                                     text = "M",
                                     style="primary.TButton",
                                     command=self.controlador.tela_menu)
            menu_button.pack(side="left", padx=5)

            self.logout = ttk.Button(navbar_frame,
                                text="Logout",
                                style="primary.TButton",
                                command=self.controlador.deslogar)
            self.logout.pack(side="right", padx=5)

            nome_label = ttk.Label(navbar_frame,
                                   text=self.controladorUsuario.usuario_logado.nome,
                                   style="primary.inverse.TLabel")
            nome_label.pack(side="right", padx=5)

            
        else:
            login_button = ttk.Button(navbar_frame,
                                    text="Login",
                                    style="primary.TButton",
                                    command=self.controlador.tela_login)
            login_button.pack(side="right", padx=5)
