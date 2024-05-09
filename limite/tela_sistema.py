import tkinter as tk
from limite.tela_catalogo import TelaCatalogo


class TelaSistema(tk.Frame):
    def __init__(self, master, controlador):
        super().__init__(master)
        self.controlador = controlador
        self.abre_tela_principal()

    def abre_tela_principal(self):

        if self.controlador.controlador_usuarios.usuario_logado:
            nome = self.controlador.controlador_usuarios.usuario_logado.nome
            titulo_label = tk.Label(self, text=nome, font=("Helvetica", 14, "bold"))
            titulo_label.pack(pady=10)

            papel = self.controlador.controlador_usuarios.usuario_logado.papel
            if papel == 1:  # Administrador
                self.redirecionar_administrador()
            elif papel == 2:  # Funcionário
                self.redirecionar_funcionario()
            else:
                self.controlador.controlador_usuarios.usuario_logado = None
                self.controlador.tela_usuario_deslogado()  # Qualquer outro papel
        else:
            self.controlador.tela_catalogo(self) #usuário não logado

    def redirecionar_administrador(self):
        # Button to open User Creation Screen
        self.add_user_button = tk.Button(
            self,
            text="Cadastrar usuários",
            command=self.controlador.tela_criar_usuarios,
        )
        self.add_user_button.pack(pady=10)

        # Button to open View User Screen
        self.view_users_button = tk.Button(
            self, text="Listar usuários", command=self.controlador.tela_usuarios
        )
        self.view_users_button.pack(pady=10)

        self.view_users_button = tk.Button(
            self, text="Menu peças", command=self.controlador.tela_menu_pecas
        )
        self.view_users_button.pack(pady=10)

        # Button to logout
        self.logout = tk.Button(self, text="Logout", command=self.controlador.deslogar)
        self.logout.pack(pady=10)

    def redirecionar_funcionario(self):
        self.view_users_button = tk.Button(
            self, text="Menu peças", command=self.controlador.tela_menu_pecas
        )
        self.view_users_button.pack(pady=10)
        self.logout = tk.Button(self, text="Logout", command=self.controlador.deslogar)
        self.logout.pack(pady=10)