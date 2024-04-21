import tkinter as tk
from tkinter import ttk


class TelaCatalogo(tk.Frame):
    def __init__(self, master, controlador):
        super().__init__(master)
        self.controlador = controlador
        self.abrir_tela_catalogo()

    def abrir_tela_catalogo(self):
        titulo_label = tk.Label(self, text="[Futuro catálogo]", font=("Helvetica", 14, "bold"))
        titulo_label.pack(pady=10)

        self.login_button = tk.Button(self, text="Login", command=self.controlador.tela_login)
        self.login_button.pack(pady=10)

