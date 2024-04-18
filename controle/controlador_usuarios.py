from limite.tela_usuario import TelaUsuario
from limite.tela_criar_usuario import TelaCriarUsuario
from entidade.usuario import Usuario
from persistencia.usuario_dao import UsuarioDAO
import tkinter as tk


class ControladorUsuarios:

    def __init__(self, master, controlador):
        self.master = master
        self.controlador = controlador
        self.users = ["User 1", "User 2", "User 3", "User 4"]
        #self.pegar_todos()

    def abre_tela_usuario(self):
        return TelaUsuario(self.master, self, self.users)

    def abre_tela_criar_usuario(self):
        return TelaCriarUsuario(self.master, self)

    def voltar(self):
        self.controlador.tela_sistema()

    def criar_usuario(self):
        usuario = Usuario(2, "Teste2", "teste@gmail.com", "teste", 1)
        UsuarioDAO().add(usuario)
        print("save")

    def deletar_usuario(self):
        print("delete")

    def pegar_todos(self):
        usuarios = UsuarioDAO().get_all()
        print(usuarios)

