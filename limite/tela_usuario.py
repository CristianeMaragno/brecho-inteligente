import tkinter as tk
from tkinter import ttk

class TelaUsuario(tk.Frame):
    def __init__(self, master, controlador, users):
        super().__init__(master)
        self.controlador = controlador
        self.users = users
        self.abre_tela_usuario()

    def abre_tela_usuario(self):
        # User List
        self.user_listbox = tk.Listbox(self, width=50, height=10)
        self.user_listbox.pack(side=tk.LEFT, padx=5, pady=5)

        # Fill user list
        for user in self.users:
            self.user_listbox.insert(tk.END, user)

        # Scrollbar for user list
        self.scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.user_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.user_listbox.config(yscrollcommand=self.scrollbar.set)

        # Delete Button
        self.delete_button = ttk.Button(self, text="Delete User", command=self.controlador.deletar_usuario)
        self.delete_button.pack(pady=5)

        # Voltar Button
        self.go_back_button = ttk.Button(self, text="Voltar", command=self.controlador.voltar)
        self.go_back_button.pack(pady=5)

    def delete_user(self):
        selected_index = self.user_listbox.curselection()
        print(selected_index)
