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

        # Deletar Button
        self.delete_button = ttk.Button(self, text="Deletar Usuário", command=self.deletar_usuario)
        self.delete_button.pack(pady=5)

        # Editar Button
        self.edit_button = ttk.Button(self, text="Editar Usuário", command=self.editar_usuario)
        self.edit_button.pack(pady=5)

        # Voltar Button
        self.go_back_button = ttk.Button(self, text="Voltar", command=self.controlador.voltar)
        self.go_back_button.pack(pady=5)

    def deletar_usuario(self):
        index = self.user_listbox.curselection()
        if index:
            usuario_selecionado = self.user_listbox.get(index[0])
            partes = usuario_selecionado.split(" ")
            id_parte = partes[0].strip()
            id = int(id_parte)
            self.controlador.deletar_usuario(id)
            self.user_listbox.delete(index[0])

    def editar_usuario(self):
        index = self.user_listbox.curselection()
        if index:
            usuario_selecionado = self.user_listbox.get(index[0])
            partes = usuario_selecionado.split(" ")
            id_parte = partes[0].strip()
            id = int(id_parte)
            self.controlador.editar_usuario(id)
