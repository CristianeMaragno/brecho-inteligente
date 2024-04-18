import tkinter as tk
from tkinter import ttk

class TelaCriarUsuario(tk.Frame):
    def __init__(self, master, controlador):
        super().__init__(master)
        self.controlador = controlador
        self.abre_tela_criar_usuario()

    def abre_tela_criar_usuario(self):
        # Email Label and Entry
        self.email_label = tk.Label(self, text="Email:")
        self.email_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.email_entry = tk.Entry(self)
        self.email_entry.grid(row=0, column=1, padx=10, pady=5)

        # Password Label and Entry
        self.password_label = tk.Label(self, text="Senha:")
        self.password_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        # Role Label and Dropdown
        self.role_label = tk.Label(self, text="Papel:")
        self.role_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.role_var = tk.StringVar()
        self.role_combobox = ttk.Combobox(self, textvariable="Selecione o papel", state="readonly")
        self.role_combobox['values'] = ("Administrador", "Funcionário")
        self.role_combobox.current(0)
        self.role_combobox.grid(row=2, column=1, padx=10, pady=5)

        # Button to create user
        self.create_button = tk.Button(self, text="Criar", command=self.create_user)
        self.create_button.grid(row=3, columnspan=2, padx=10, pady=10)

        # Voltar Button
        self.go_back_button = tk.Button(self, text="Voltar", command=self.controlador.voltar)
        self.go_back_button.grid(row=4, columnspan=2, padx=10, pady=10)

    def create_user(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        role = self.role_var.get()

        print("Email:", email)
        print("Password:", password)
        print("Role:", role)
