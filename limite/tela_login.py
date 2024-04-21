import tkinter as tk
from tkinter import ttk

class TelaLogin(tk.Frame):
    def __init__(self, master, controlador, erro):
        super().__init__(master)
        self.controlador = controlador
        self.mensagem_erro = erro
        self.abre_tela_login()
        self.senha = None
        self.email= None
    
    def abre_tela_login(self):

        ## Título da tela de login
        titulo_label = tk.Label(self, text="LOGIN", font=("Helvetica", 14, "bold"))
        titulo_label.pack(pady=10)

        # Label e Entry para email
        self.label_email = tk.Label(self, text="Email:")
        self.label_email.pack(anchor="w")
        self.entry_email = tk.Entry(self)
        self.entry_email.pack(pady=5)

        # Label e Entry para senha
        self.label_senha = tk.Label(self, text="Senha:")
        self.label_senha.pack(anchor="w")
        self.entry_senha = tk.Entry(self, show="*")
        self.entry_senha.pack(pady=5)

        # Botão de login
        self.botao_login = tk.Button(self, text="Entrar", command=self.enviar_dados)
        self.botao_login.pack(pady=10)

        # Botão para voltar
        self.go_back_button = tk.Button(self, text="Voltar", command=self.controlador.voltar)
        self.go_back_button.pack(pady=10)

        # Label para mensagem de erro
        self.mensagem_erro = tk.Label(self, text=self.mensagem_erro, fg="red")
        self.mensagem_erro.pack()

    def enviar_dados(self):
        email = self.entry_email.get()
        senha = self.entry_senha.get()

        # Chama o método do controlador para efetuar o login
        self.controlador.efetuar_login(email, senha)