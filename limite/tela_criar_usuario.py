import tkinter as tk
from tkinter import ttk

class TelaCriarUsuario(tk.Frame):
    def __init__(self, master, controlador, usuario):
        super().__init__(master)
        self.editar = False if usuario is None else True
        self.controlador = controlador
        self.usuario = usuario
        self.abre_tela_criar_usuario()

    def abre_tela_criar_usuario(self):
        # Nome
        self.name_label = tk.Label(self, text="Nome:")
        self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.name_entry = tk.Entry(self)
        if(self.editar):
            self.name_entry.insert(0, self.usuario.nome)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        # Email Label and Entry
        self.email_label = tk.Label(self, text="Email:")
        self.email_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.email_entry = tk.Entry(self)
        if (self.editar):
            self.email_entry.insert(0, self.usuario.email)
        self.email_entry.grid(row=1, column=1, padx=10, pady=5)

        # Password Label and Entry
        self.password_label = tk.Label(self, text="Senha:")
        self.password_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.password_entry = tk.Entry(self, show="*")
        if (self.editar):
            self.password_entry.insert(0, self.usuario.senha)
        self.password_entry.grid(row=2, column=1, padx=10, pady=5)

        # Role Label and Dropdown
        self.role_label = tk.Label(self, text="Papel:")
        self.role_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        self.role_var = tk.StringVar()
        self.role_combobox = ttk.Combobox(self, textvariable="Selecione o papel", state="readonly")
        self.role_combobox['values'] = ("Administrador", "Funcionário")
        self.role_combobox.current(0)
        if (self.editar):
            papel = 'Administrador' if self.usuario.papel == 1 else 'Funcionário'
            self.role_combobox.set(papel)
        self.role_combobox.grid(row=3, column=1, padx=10, pady=5)

        # Button to create user
        texto = "Editar" if self.editar else "Criar"
        self.create_button = tk.Button(self, text=texto, command=self.create_user)
        self.create_button.grid(row=4, columnspan=2, padx=10, pady=10)

        # Voltar Button
        self.go_back_button = tk.Button(self, text="Voltar", command=self.controlador.voltar)
        self.go_back_button.grid(row=5, columnspan=2, padx=10, pady=10)

    def create_user(self):
        id = self.usuario.identificador if self.editar else 0
        nome = self.name_entry.get()
        email = self.email_entry.get()
        senha = self.password_entry.get()
        papel = self.role_var.get()
        papel_int = 0

        if(papel == 'Administrador'):
            papel_int = 1
        else:
            papel_int = 2

        self.controlador.criar_usuario(id, nome, email, senha, papel_int, self.editar)
        self.controlador.voltar()