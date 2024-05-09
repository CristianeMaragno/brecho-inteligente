import tkinter as tk
import ttkbootstrap as ttk
from abc import ABC, abstractmethod
from ttkbootstrap import Style

class TelaPadrao(ABC, tk.Frame):
    def __init__(self, master, controlador, controladorUsuario = None):
        super().__init__(master)
        self.controlador = controlador
        self.style = Style(theme="cerculean")
        self.pack(fill=tk.BOTH, expand=True)
        self.controladorUsuario = controladorUsuario

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

    def criar_navbar(self):
        navbar_frame = ttk.Frame(self, style="primary.TFrame", padding=10)
        navbar_frame.pack(side="top", fill="x")

        brecho_button = ttk.Button(
            navbar_frame,
            text="Brechó inteligente",
            style="primary.TButton",
            command=self.exibir_catalogo,
        )
        brecho_button.pack(side="left", padx=5)

        login_button = ttk.Button(
            navbar_frame, text="Login", style="primary.TButton", command=self.controlador.tela_login
        )
        login_button.pack(side="right", padx=5)

    def exibir_catalogo(self):
        pass