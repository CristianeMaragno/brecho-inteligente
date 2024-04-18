import tkinter as tk
from limite.tela import Tela
from entidade.categoria import TipoRestauracao as tr


class TelaPeca(Tela):
    def __init__(self, master):
        super().__init__(master)
        self.master.title("Controlador de peças")
        self.frame = None

        self.menu_opcao = None
        # Variáveis para facilitar o cadastro
        self.dados = None
        self.custo_aquisicao = None
        self.entry_descricao = None
        self.checkbox_vars = None

    def adicionar_dados(self):

        frame_pricipal = tk.Frame(self.master, width=200, height=250, borderwidth=2, relief="solid")
        frame_pricipal.pack()

        texto_titulo = tk.Label(frame_pricipal, font=14, text="Cadastro de peça")
        texto_titulo.pack(pady=10, padx=10)

        # Campos de custo
        self.custo_aquisicao = tk.Entry(frame_pricipal, width=50, font=("Arial", 14))
        self.custo_aquisicao.pack(pady=10, padx=10)

        # Checkbox de restauração
        opcoes = tr.tipos.values()
        tipo_label = tk.Label(frame_pricipal, font=14, text="Ajustes:")
        tipo_label.pack()
        self.checkbox_vars = super().gerar_checkbox(opcoes, frame_pricipal)

        # Campo de detalhes
        self.entry_descricao = tk.Entry(frame_pricipal, width=50, font=("Arial", 14))
        self.entry_descricao.pack(pady=10, padx=10)

        # Botão para pegar os dados
        tk.Button(frame_pricipal, text="Registrar", command=self.pegar_dados, padx=5,
                   pady=5, width=50, height=1, font=10).pack(padx=10, pady=10)

    def pegar_dados(self):
        ajustes = []
        for tipo, var in self.checkbox_vars.items():
            if var.get():
                ajustes.append(tipo)

        self.dados = {
            "descrição": self.entry_descricao.get(),
            "tipos_restauração": ajustes,
            "imagem": "",
            "valor_aquisição": self.custo_aquisicao.get()
        }

        self.master.quit()

    def iniciar(self):
        self.adicionar_dados()
        self.master.mainloop()
        return self.dados

    def menu(self):
        self.menu_opcoes()
        self.master.mainloop()
        return self.menu_opcao

    def definir_opcao(self, op):
        self.menu_opcao = op
        self.frame.pack_forget()
        self.master.quit()

    def menu_opcoes(self):

        self.frame = tk.Frame(self.master, width=200, height=250, borderwidth=2, relief="solid")
        self.frame.pack()
        tk.Button(self.frame, text="Registrar", command=lambda : self.definir_opcao(1)).pack()
        tk.Button(self.frame, text="Update", command=lambda: self.definir_opcao(2)).pack()
        tk.Button(self.frame, text="Deletar", command=lambda: self.definir_opcao(3)).pack()
        tk.Button(self.frame, text="Mostrar", command=lambda: self.definir_opcao(4)).pack()
        tk.Button(self.frame, text="Retornar", command=lambda: self.definir_opcao(0)).pack()






