import tkinter as tk
from tkinter import ttk

class TelaUsuario(tk.Frame):
    def __init__(self, master, controlador, usuarios):
        super().__init__(master)
        self.controlador = controlador
        self.usuarios = usuarios
        self.abre_tela_usuario()

    def abre_tela_usuario(self):
        # Lista de usuarios
        self.user_listbox = tk.Listbox(self, width=50, height=10)
        self.user_listbox.pack(side=tk.LEFT, padx=5, pady=5)

        for usuario in self.usuarios:
            self.user_listbox.insert(tk.END, str(usuario.identificador) + " " + usuario.nome)

        # Scrollbar
        self.scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.user_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.user_listbox.config(yscrollcommand=self.scrollbar.set)

        # Delete Button
        self.delete_button = ttk.Button(self, text="Deletar Usuario", command=self.deletar_usuario)
        self.delete_button.pack(pady=5)

        # Edit Button
        self.edit_button = ttk.Button(self, text="Editar Usuario", command=self.editar_usuario)
        self.edit_button.pack(pady=5)

        # Voltar Button
        self.go_back_button = ttk.Button(self, text="Voltar", command=self.controlador.voltar)
        self.go_back_button.pack(pady=5)

    def deletar_usuario(self):
        selected_index = self.user_listbox.curselection()
        if selected_index:
            selected_user = self.user_listbox.get(selected_index[0])
            parts = selected_user.split(" ")
            id_part = parts[0].strip()
            id = int(id_part)
            self.controlador.deletar_usuario(id)
            self.user_listbox.delete(selected_index[0])

    def editar_usuario(self):
        selected_index = self.user_listbox.curselection()
        if selected_index:
            selected_user = self.user_listbox.get(selected_index[0])
            parts = selected_user.split(" ")
            id_part = parts[0].strip()
            id = int(id_part)
            self.controlador.editar_usuario(id)