import tkinter as tk
from tkinter import ttk

class TelaLogin(tk.Frame):
    def __init__(self, master, controlador):
        super().__init__(master)
        self.controlador = controlador
        self.abre_tela_login()
        self.senha = None
        self.email= None
    
    def abre_tela_login(self):

        ## Título da tela de login
        titulo_label = tk.Label(self, text="LOGIN", font=("Helvetica", 14, "bold"))
        titulo_label.grid(row=0, columnspan=2, pady=10)

        # Label e Entry para email
        self.label_email = tk.Label(self, text="Email:")
        self.label_email.grid(row=1, column=0, sticky="w")
        self.entry_email = tk.Entry(self)
        self.entry_email.grid(row=1, column=1, pady=5)

        # Label e Entry para senha
        self.label_senha = tk.Label(self, text="Senha:")
        self.label_senha.grid(row=2, column=0, sticky="w")
        self.entry_senha = tk.Entry(self, show="*")
        self.entry_senha.grid(row=2, column=1, pady=5)

        # Botão de login
        self.botao_login = tk.Button(self, text="Entrar", command=self.enviar_dados)
        self.botao_login.grid(row=3, columnspan=2, pady=10)

        # Botão para voltar
        self.go_back_button = tk.Button(self, text="Voltar", command=self.controlador.voltar)
        self.go_back_button.grid(row=4, columnspan=2, pady=10)
    
    def enviar_dados(self):
        email = self.entry_email.get()
        senha = self.entry_senha.get()

        # Chama o método do controlador para efetuar o login
        self.controlador.efetuar_login(email, senha)
