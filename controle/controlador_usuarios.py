from limite.tela_usuario import TelaUsuario
from limite.tela_criar_usuario import TelaCriarUsuario
from limite.tela_login import TelaLogin
from entidade.usuario import Usuario
from persistencia.usuario_dao import UsuarioDAO


class ControladorUsuarios:

    def __init__(self, master, controlador):
        self.master = master
        self.controlador = controlador
        self.usuario = None
        self.usuario_logado = None

    def abre_tela_usuario(self):
        usuarios = self.pegar_todos()
        return TelaUsuario(self.master, self, usuarios)

    def abre_tela_criar_usuario(self):
        return TelaCriarUsuario(self.master, self, self.usuario)

    def abre_tela_login(self, erro=None):
        return TelaLogin(self.master, self.controlador, self, erro)

    def voltar(self):
        self.usuario = None
        self.controlador.tela_sistema()

    def criar_usuario(self, id, nome, email, senha, papel, editar):
        usuario = Usuario(id, nome, email, senha, papel)
        if (editar):
            UsuarioDAO().update(usuario)
        else:
            UsuarioDAO().add(usuario)

    def deletar_usuario(self, id):
        UsuarioDAO().remove(id)

    def editar_usuario(self, id):
        usuario = UsuarioDAO().pegar_por_id(id)
        if (usuario):
            self.usuario = usuario
            self.controlador.tela_criar_usuarios()

    def pegar_todos(self):
        usuarios = UsuarioDAO().pegar_todos()
        return usuarios

    def efetuar_login(self, email, senha):
        usuario = UsuarioDAO().fazer_login(email, senha)
        if usuario:
            self.usuario_logado = usuario
            self.controlador.tela_sistema()
        else:
            self.controlador.tela_login("Email ou senha incorretos!")

    def deslogar_usuario(self):
        self.usuario_logado = None
