import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
from limite.tela_padrao import TelaPadrao

class TelaLogin(TelaPadrao):
    def __init__(self, master, controladorSistema, controladorUsuario, erro=""):
        self.mensagem_erro = erro
        self.senha = None
        self.email = None
        super().__init__(master, controladorSistema, controladorUsuario)
    
    def conteudo(self):
        width_px = 570
        height_px = 80

        #Frame Login
        frame_login = ttk.Frame(self,
                                width=770,
                                height=608,
                                padding=20,
                                style='light')
        
        frame_login.pack(fill="none",
                         expand=False,
                         pady=32)

        titulo_label = ttk.Label(frame_login,
                                 text="LOGIN",
                                 style="inverse-light",
                                 font=("Helvetica", 14, "bold"))
        titulo_label.pack(pady=10)

        # Campo de entrada para o email
        self.entry_email = ttk.Entry(frame_login,
                                     bootstyle='primary',
                                     width=height_px)
        self.entry_email.insert(0, "Email")
        self.entry_email.bind("<FocusIn>", self.clear_email_placeholder)
        self.entry_email.bind("<FocusOut>", self.restore_email_placeholder)
        self.entry_email.pack(pady=5)

        # Campo de entrada para a senha
        self.entry_senha = ttk.Entry(frame_login,
                                     show="*",
                                     bootstyle='primary',
                                     width=height_px)
        self.entry_senha.insert(0, "Senha")
        self.entry_senha.bind("<FocusIn>", self.clear_password_placeholder)
        self.entry_senha.bind("<FocusOut>", self.restore_password_placeholder)
        self.entry_senha.pack(pady=5)

        # Botão de login
        self.botao_login = ttk.Button(frame_login,
                                      text="Entrar",
                                      command=self.enviar_dados,
                                      bootstyle='primary',
                                      width=height_px)
        self.botao_login.pack(pady=10)

        # Label para mensagem de erro
        self.mensagem_erro_label = ttk.Label(frame_login,
                                             text=self.mensagem_erro,
                                             foreground="red")
        self.mensagem_erro_label.pack()

    def clear_email_placeholder(self, event):
        if self.entry_email.get() == "Email":
            self.entry_email.delete(0, tk.END)

    def restore_email_placeholder(self, event):
        if not self.entry_email.get():
            self.entry_email.insert(0, "Email")

    def clear_password_placeholder(self, event):
        if self.entry_senha.get() == "Senha":
            self.entry_senha.delete(0, tk.END)
            self.entry_senha.config(show="*")

    def restore_password_placeholder(self, event):
        if not self.entry_senha.get():
            self.entry_senha.config(show="")
            self.entry_senha.insert(0, "Senha")

    def enviar_dados(self):
        email = self.entry_email.get()
        senha = self.entry_senha.get()
        self.controladorUsuario.efetuar_login(email, senha)