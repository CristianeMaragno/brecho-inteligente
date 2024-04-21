from limite.tela_sistema import TelaSistema
from persistencia.usuario_dao import UsuarioDAO
from controle.controlador_usuarios import ControladorUsuarios

class ControladorSistema:

    def __init__(self, root):
        self.root = root
        self.__controlador_usuarios = ControladorUsuarios(self.root, self)
        self.tela_atual = None

    def criar_adm_padrao(self):
        # Supondo que 'usuarios' seja uma lista de objetos Usuario
        usuarios = UsuarioDAO().pegar_todos()

        # Iterar sobre cada usuário e exibir seus atributos
        for usuario in usuarios:
            print(f"ID: {usuario.identificador}")
            print(f"Nome: {usuario.nome}")
            print(f"Email: {usuario.email}")
            print(f"Senha: {usuario.senha}")
            print(f"Papel: {usuario.papel}")
            print()

        if UsuarioDAO().pegar_por_nome("Administrador Padrão"):
            print("adm padrão já existe.")
            None
        else:
            self.controlador_usuarios.criar_usuario(0, "Administrador Padrão", "adm0", "0", 1, False)
            print("adm padrão criado: \n email: adm0 \n senha: 0.")

    def tela_sistema(self):
        if self.tela_atual:
            self.tela_atual.pack_forget()

        self.tela_atual = TelaSistema(self.root, self)
        self.tela_atual.pack()

    def tela_usuarios(self):
        if self.tela_atual:
            self.tela_atual.pack_forget()

        self.tela_atual = self.__controlador_usuarios.abre_tela_usuario()
        self.tela_atual.pack()

    def tela_criar_usuarios(self):
        if self.tela_atual:
            self.tela_atual.pack_forget()

        self.tela_atual = self.__controlador_usuarios.abre_tela_criar_usuario()
        self.tela_atual.pack()

    def tela_login(self):
        if self.tela_atual:
            self.tela_atual.pack_forget()
        
        self.tela_atual = self.__controlador_usuarios.abre_tela_login()
        self.tela_atual.pack()

    @property
    def controlador_usuarios(self):
        return self.__controlador_usuarios

    def encerra_sistema(self):
        exit(0)