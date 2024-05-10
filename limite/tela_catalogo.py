from limite.tela_padrao import TelaPadrao
import tkinter as tk


class TelaCatalogo(TelaPadrao):
    def __init__(self, master, controlador, controladorUsuario=None):
        super().__init__(master, controlador, controladorUsuario)

    def controlador(self):
        return self.__controlador

    def conteudo(self):
        self.frame_principal = tk.Frame(self)
        self.frame_principal.pack(fill=tk.BOTH, expand=True)

        titulo_label = tk.Label(self.frame_principal,
                                text="[Futuro catálogo]",
                                font=("Helvetica", 14, "bold"))
        titulo_label.pack(pady=10)
