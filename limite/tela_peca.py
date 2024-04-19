import tkinter as tk
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
        self.frame = tk.Frame(self, borderwidth=2, relief="solid")
        self.frame.pack(pady=10, padx=20)

        self.texto_titulo = tk.Label(self.frame, text="Cadastro de peça")
        self.texto_titulo.pack(pady=10, padx=10)

        # Entry de custo de aquisição
        self.label_custo = tk.Label(self.frame, text="Custo de aquisição:")
        self.label_custo.pack(pady=10, padx=10)

        self.custo_aquisicao = tk.Entry(self.frame)
        self.custo_aquisicao.pack(pady=10, padx=10)

        opcoes = tr.tipos.values()
        tipo_label = tk.Label(self.frame, text="Ajustes:")
        tipo_label.pack()

        self.checkbox_vars = {}

        # Frame para os checkboxes
        checkbox_frame = tk.Frame(self.frame)
        checkbox_frame.pack(padx=10, pady=10)

        # Criando listbox
        self.listbox = tk.Listbox(checkbox_frame, selectmode=tk.MULTIPLE, width=20, height=len(opcoes))
        for opcao in opcoes:
            self.listbox.insert(tk.END, opcao)
        self.listbox.pack(padx=10, pady=10)

        # Campo de detalhes
        self.label_desc = tk.Label(self.frame, text="Detalhes:")
        self.label_desc.pack(pady=10, padx=10)

        self.entry_descricao = tk.Entry(self.frame)
        self.entry_descricao.pack(pady=10, padx=10)

        # Botão para pegar os dados
        tk.Button(self.frame, text="Registrar", command=self.retornar).pack(padx=10, pady=10)

    def retornar(self):

        selecionados = self.listbox.curselection()
        ajustes = [self.listbox.get(idx) for idx in selecionados]
        if not ajustes:
            ajustes.append(tr.tipos["NENHUM"])

        dados = {
            "descrição": self.entry_descricao.get(),
            "tipos_restauração": ajustes,
            "imagem": "",
            "custo_aquisição": self.custo_aquisicao.get()
        }
        self.controller.registrar(dados)
        self.controller.tela_menu()

class UpdatePeca(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.frame = tk.Frame(self)
        self.mensagem_erro = None
        self.get_id()

    def get_id(self):
        if not self.mensagem_erro:
            self.frame.pack()

            self.label = tk.Label(self.frame, text="Update")
            self.label.pack()

            label_peca_id = tk.Label(self.frame, text= "Insira o id da peça para fazer update:")
            label_peca_id.pack()

            self.entry_peca_id = tk.Entry(self.frame)
            self.entry_peca_id.pack(padx=10, pady=10)

            self.button = tk.Button(
                self.frame, text="Checar ID", command=self.checar_id
            )
            self.button.pack()

            self.button = tk.Button(
                self.frame, text="Retornar", command=self.controller.tela_menu
            )
            self.button.pack()

    def checar_id(self):
        resposta = self.controller.get_peca(self.entry_peca_id.get())
        if resposta:
            self.id_peca = resposta.id
            self.frame.pack_forget()
            self.update()
        else:
            self.mensagem_erro = tk.Label(self.frame, text="Insira um id válido.")
            self.mensagem_erro.pack()
            self.get_id()

    def update(self):
        self.frame = tk.Frame(self, borderwidth=2, relief="solid")
        self.frame.pack(pady=10, padx=20)

        self.texto_titulo = tk.Label(self.frame, text="Update de peça")
        self.texto_titulo.pack(pady=10, padx=10)

        # Entry de custo de aquisição
        self.label_custo = tk.Label(self.frame, text="Custo de aquisição:")
        self.label_custo.pack(pady=10, padx=10)

        self.custo_aquisicao = tk.Entry(self.frame)
        self.custo_aquisicao.pack(pady=10, padx=10)

        # Checkbox de restauração
        opcoes = tr.tipos.values()
        tipo_label = tk.Label(self.frame, text="Ajustes:")
        tipo_label.pack()

        # Frame para os checkboxes
        checkbox_frame = tk.Frame(self.frame)
        checkbox_frame.pack(padx=10, pady=10)

        # Campo de detalhes
        self.label_desc = tk.Label(self.frame, text="Detalhes:")
        self.label_desc.pack(pady=10, padx=10)

        self.entry_descricao = tk.Entry(self.frame, font=("Arial", 8))
        self.entry_descricao.pack(pady=10, padx=10)

        # Criando listbox
        self.listbox = tk.Listbox(checkbox_frame, selectmode=tk.MULTIPLE, width=20, height=len(opcoes))
        for opcao in opcoes:
            self.listbox.insert(tk.END, opcao)
        self.listbox.pack(padx=10, pady=10)

        # Botão para pegar os dados
        tk.Button(self.frame, text="Update", command=self.retornar).pack(padx=10, pady=10)


    def retornar(self):
        selecionados = self.listbox.curselection()
        ajustes = [self.listbox.get(idx) for idx in selecionados]
        if not ajustes:
            ajustes.append(tr.tipos["NENHUM"])

        dados = {
            "id": self.id_peca,
            "descrição": self.entry_descricao.get(),
            "tipos_restauração": ajustes,
            "imagem": "",
            "custo_aquisição": self.custo_aquisicao.get()
        }
        self.controller.update(dados)
        self.controller.tela_menu()

class MostrarPeca(tk.Frame):
    def __init__(self, master, controller, lista_pecas=None):
        super().__init__(master)
        self.controller = controller
        self.frame = tk.Frame(self)
        self.pecas = lista_pecas or []
        self.mostrar()

    def mostrar(self):
        self.frame.pack()

        self.label = tk.Label(self.frame, text="Itens:")
        self.label.pack()

        self.listbox = tk.Listbox(self.frame, width=50)
        for peca in self.pecas:
            self.listbox.insert(tk.END, f'ID: {peca.id}  Descrição: {peca.descricao}'
                                        f'  Status: {peca.status.__str__()}')
        self.listbox.pack()

        self.button = tk.Button(
            self, text="Retornar ao Menu", command=self.controller.tela_menu
        )
        self.button.pack()


class ApagarPeca(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.mensagem_erro = None
        self.frame = tk.Frame(self)
        self.controller = controller
        self.get_id()

    def get_id(self):
        if not self.mensagem_erro:
            self.frame.pack()

            self.label = tk.Label(self.frame, text="Apagar")
            self.label.pack()

            label_peca_id = tk.Label(self.frame, text= "Insira o id da peça a ser apagada:")
            label_peca_id.pack()

            self.entry_peca_id = tk.Entry(self.frame)
            self.entry_peca_id.pack(padx=10, pady=10)

            self.button = tk.Button(
                self.frame, text="Apagar", command=self.checar_id
            )
            self.button.pack()

            self.button = tk.Button(
                self.frame, text="Retornar", command=self.controller.tela_menu
            )
            self.button.pack()

    def checar_id(self):
        resposta = self.controller.get_peca(self.entry_peca_id.get())
        if resposta:
            self.id_peca = resposta.id
            self.frame.pack_forget()
            self.retornar()
        else:
            self.mensagem_erro = tk.Label(self.frame, text="Insira um id válido.")
            self.mensagem_erro.pack()
            self.get_id()

    def retornar(self):
        self.controller.apagar(self.id_peca)
        self.controller.tela_menu()