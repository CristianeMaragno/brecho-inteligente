import tkinter as tk
from limite.tela import Tela
from entidade.categoria import TipoRestauracao as tr


class MenuPeca(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.abrir_menu()

    def abrir_menu(self):
        self.label = tk.Label(self, text="Menu")
        self.label.pack()

        self.button1 = tk.Button(
            self, text="Registrar", command=self.controller.tela_registrar
        )
        self.button1.pack()

        self.button2 = tk.Button(
            self, text="Update", command=self.controller.tela_update
        )
        self.button2.pack()

        self.button2 = tk.Button(
            self, text="Apagar", command=self.controller.tela_apagar
        )
        self.button2.pack()

        self.button2 = tk.Button(
            self, text="Mostrar", command=self.controller.tela_mostrar
        )
        self.button2.pack()

class RegistrarPeca(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.registrar()

    def registrar(self):
        self.frame = tk.Frame(self.master, width=100, height=150, borderwidth=2, relief="solid")
        self.frame.pack(pady=50, padx=20)

        self.texto_titulo = tk.Label(self.frame, font=11, text="Cadastro de peça")
        self.texto_titulo.pack(pady=10, padx=10)

        # Entry de custo de aquisição
        self.label_custo = tk.Label(self.frame, font=8, text="Custo de aquisição:")
        self.label_custo.pack(pady=10, padx=10)

        self.custo_aquisicao = tk.Entry(self.frame, width=30, font=("Arial", 8))
        self.custo_aquisicao.pack(pady=10, padx=10)

        # Checkbox de restauração
        opcoes = tr.tipos.values()
        tipo_label = tk.Label(self.frame, font=14, text="Ajustes:")
        tipo_label.pack()

        self.checkbox_vars = {}

        # Frame para os checkboxes
        checkbox_frame = tk.Frame(self.frame)
        checkbox_frame.pack(padx=10, pady=10)

        # Criando checkboxes
        for opcao in opcoes:
            var = tk.BooleanVar()
            self.checkbox_vars[opcao] = var
            checkbox = tk.Checkbutton(checkbox_frame, text=opcao, variable=var)
            checkbox.pack(padx=10, pady=5)

        # Campo de detalhes
        self.label_desc = tk.Label(self.frame, font=8, text="Detalhes:")
        self.label_desc.pack(pady=10, padx=10)

        self.entry_descricao = tk.Entry(self.frame, width=30, font=("Arial", 8))
        self.entry_descricao.pack(pady=10, padx=10)

        # Botão para pegar os dados
        tk.Button(self.frame, text="Registrar", command=self.retornar, padx=5,
                  pady=5, width=50, height=1, font=10).pack(padx=10, pady=10)

    def retornar(self):

        ajustes = []
        if self.checkbox_vars:
            for tipo, var in self.checkbox_vars.items():
                if var.get():
                    ajustes.append(tipo)
        else:
            ajustes.append(tr.tipos["NENHUM"])

        dados = {
            "descrição": self.entry_descricao.get(),
            "tipos_restauração": ajustes,
            "imagem": "",
            "custo_aquisição": self.custo_aquisicao.get()
        }
        self.frame.pack_forget()
        self.controller.registrar(dados)
        self.controller.tela_menu()

class UpdatePeca(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.update()

    def update(self):
        self.label = tk.Label(self, text="Update")
        self.label.pack()

        self.button = tk.Button(
            self, text="Retornar ao Menu", command=self.controller.tela_menu
        )
        self.button.pack()

class MostrarPeca(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.mostrar()

    def mostrar(self):
        self.label = tk.Label(self, text="Mostrar")
        self.label.pack()

        self.button = tk.Button(
            self, text="Retornar ao Menu", command=self.controller.tela_menu
        )
        self.button.pack()

class ApagarPeca(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.apagar()

    def apagar(self):
        self.label = tk.Label(self, text="Apagar")
        self.label.pack()

        self.button = tk.Button(
            self, text="Retornar ao Menu", command=self.controller.tela_menu
        )
        self.button.pack()