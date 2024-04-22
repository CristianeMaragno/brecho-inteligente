import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

class TelaLogin(tk.Frame):
    def __init__(self, master, controlador, erro):
        super().__init__(master)
        self.controlador = controlador
        self.mensagem_erro = erro
        self.abre_tela_login()
        self.senha = None
        self.email = None
    
    def abre_tela_login(self):
        style = Style(theme='litera')
        width_px = 570
        height_px = 80

        #NavBar
        frame_navbar = ttk.Frame(self,
                                 height=72,
                                 width= 2000,
                                 padding=18)
        frame_navbar.pack(fill="x", side="top")

        label = ttk.Label(frame_navbar,
                          text="Brechó Inteligente",
                          font=("Helvetica", 14, "bold"))
        label.pack(side="top", anchor="w")

        #Frame Login
        frame_login = ttk.Frame(self,
                                width=770,
                                height=608,
                                padding=20,
                                style='light')
        frame_login.pack(fill="none",
                         expand=False,
                         padx=335,
                         pady=208)

        titulo_label = ttk.Label(frame_login,
                                 text="LOGIN",
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

        # Botão para voltar
        self.go_back_button = ttk.Button(frame_login,
                                         text="Voltar",
                                         command=self.controlador.voltar,
                                         bootstyle='primary',
                                         width=height_px)
        self.go_back_button.pack(pady=10)

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
        self.controlador.efetuar_login(email, senha)