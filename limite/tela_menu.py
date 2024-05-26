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
         # criação de usuários
        self.add_user_button = ttk.Button(self.frame_menu,
                                         text="Cadastrar usuários",
                                         width=30,
                                         command=self.controlador.
                                         tela_criar_usuarios)
        self.add_user_button.pack(padx=10, pady=10)

        # Ver usuarios
        self.view_users_button = ttk.Button(self.frame_menu,
                                           text="Listar usuários",
                                           width=30,
                                           command=self.controlador.
                                           tela_usuarios)
        self.view_users_button.pack(padx=10, pady=10)

        # editar calculadora
        self.calculadora = ttk.Button(self.frame_menu,
                                           text="Editar Calculadora",
                                           width=30,
                                           command=self.controlador.
                                           tela_calculadora)
        self.calculadora.pack(padx=10, pady=10)

        # Relatórios
        self.relatorio_vendas = ttk.Button(self.frame_menu,
                                           text="Relatório de Vendas",
                                           width=30)
        self.relatorio_vendas.pack(padx=10, pady=10)

        self.relatorio_restauracao = ttk.Button(self.frame_menu,
                                           text="Relatório de Restauração",
                                           width=30)
        self.relatorio_restauracao.pack(padx=10, pady=10)

        self.menu_fun()

    def menu_fun(self):

        self.view_users_button = ttk.Button(self.frame_menu,
                                           text="Menu peças",
                                           width=30,
                                           command=self.controlador.
                                           tela_menu_pecas)
        self.view_users_button.pack(padx=10, pady=10)

        self.reserva = ttk.Button(self.frame_menu,
                                           text="Reserva",
                                           width=30)
        self.reserva.pack(padx=10, pady=10)

        self.venda = ttk.Button(self.frame_menu,
                                           text="Venda",
                                           width=30)
        self.venda.pack(padx=10, pady=10)

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