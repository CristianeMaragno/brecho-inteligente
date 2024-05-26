import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from persistencia.categorias_dao import CategoriasDAO as ctdao
from persistencia.categorias_dao import CategoriasDAO as ctdao
from entidade.categoria import Categorias as ct


class MenuPeca(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.conteudo()

    def conteudo(self):

        frame = ttk.Labelframe(self, text="Menu peças")
        frame.grid(row=1, column=0, padx=10, pady=32)

        self.button1 = ttk.Button(
            frame,
            text="Registrar",
            command=self.controller.tela_registrar,
            bootstyle="secondary",
            width=30,
        )
        self.button1.pack(padx=10, pady=10)

        self.button2 = ttk.Button(
            frame,
            text="Update",
            command=self.controller.tela_update,
            bootstyle="secondary",
            width=30,
        )
        self.button2.pack(padx=10, pady=10)

        self.button3 = ttk.Button(
            frame,
            text="Apagar",
            command=self.controller.tela_apagar,
            bootstyle="secondary",
            width=30,
        )
        self.button3.pack(padx=10, pady=10)

        self.button4 = ttk.Button(
            frame,
            text="Mostrar",
            command=self.controller.tela_mostrar,
            bootstyle="secondary",
            width=30,
        )
        self.button4.pack(padx=10, pady=10)

        self.button5 = ttk.Button(
            frame,
            text="Retornar",
            command=self.controller.voltar,
            bootstyle="secondary",
            width=30,
        )
        self.button5.pack(padx=10, pady=10)

        self.button6 = ttk.Button(
            frame,
            text="Restauração para a venda",
            command=self.controller.tela_rest_p_venda,
            bootstyle="secondary",
            width=30,
        )
        self.button6.pack(padx=10, pady=10)


class RegistrarPeca(tk.Frame):
    def __init__(self, master, controller, categorias):
        super().__init__(master)
        self.categorias = categorias
        self.controller = controller
        self.frame = None
        self.registrar()

    def registrar(self):
        self.frame = ttk.Labelframe(self,
                                    text="Cadastro de peça",
                                    bootstyle="info")
        self.frame.grid(row=1, column=0, padx=10, pady=32)

        # Entry de custo de aquisição
        self.label_custo = ttk.Label(self.frame, text="Custo de aquisição:")
        self.label_custo.pack(pady=10, padx=10)

        self.custo_aquisicao = ttk.Entry(self.frame, width=30)
        self.custo_aquisicao.pack(pady=10, padx=10)

        opcoes = []
        for categoria in self.categorias:
            opcoes.append(categoria.nome)

        tipo_label = ttk.Label(self.frame, text="Ajustes:")
        tipo_label.pack()

        self.checkbox_vars = {}

        # Frame para os checkboxes
        checkbox_frame = ttk.Frame(self.frame)
        checkbox_frame.pack(padx=10, pady=10)

        # Criando listbox
        self.listbox = tk.Listbox(checkbox_frame,
                                  selectmode=tk.MULTIPLE,
                                  width=30, height=len(opcoes))
        for opcao in opcoes:
            self.listbox.insert(tk.END, opcao)
        self.listbox.pack(padx=10, pady=10)

        # Campo de detalhes
        self.label_desc = ttk.Label(self.frame, text="Detalhes:")
        self.label_desc.pack(pady=10, padx=10)

        self.entry_descricao = ttk.Entry(self.frame, width=30)
        self.entry_descricao.pack(pady=10, padx=10)

        # Botão para pegar os dados
        ttk.Button(
            self.frame,
            text="Registrar",
            command=self.input_tests,
            bootstyle="success",
            width=30,
        ).pack(padx=10, pady=10)
        ttk.Button(
            self.frame,
            text="Retornar",
            command=self.controller.tela_menu,
            bootstyle="warning",
            width=30,
        ).pack(padx=10, pady=10)

    def input_tests(self):
        try:
            custo_aquisicao = float(self.custo_aquisicao.get())
            if custo_aquisicao:
                self.retornar()
        except ValueError:
            messagebox.showinfo(
                "Erro",
                "Por favor informe um valorválido de custo de aquisição."
            )

    def retornar(self):
        ajustes = []
        ajustes = self.listbox.curselection()

        if not ajustes:
            ajustes.append(0)

        dados = {
            "descrição": self.entry_descricao.get(),
            "tipos_restauração": ajustes,
            "imagem": "",
            "custo_aquisição": self.custo_aquisicao.get(),
        }
        self.controller.registrar(dados)
        self.controller.tela_menu()


class UpdatePeca(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.frame = None
        self.mensagem_erro = None
        self.get_id()

    def get_id(self):
        if not self.frame:
            self.frame = ttk.Labelframe(self, text="Update", bootstyle="info")
            self.frame.pack(padx=10, pady=10)

            label_peca_id = tk.Label(
                self.frame, text="Insira o id da peça para fazer update:"
            )
            label_peca_id.pack()

            self.entry_peca_id = tk.Entry(self.frame, width=30)
            self.entry_peca_id.pack(padx=10, pady=10)

            ttk.Button(
                self.frame,
                text="Checar ID",
                command=self.checar_id,
                bootstyle="success",
                width=30,
            ).pack(padx=10, pady=10)
            ttk.Button(
                self.frame,
                text="Retornar",
                command=self.controller.tela_menu,
                bootstyle="warning",
                width=30,
            ).pack(padx=10, pady=10)

    def checar_id(self):
        resposta = self.controller.get_peca(self.entry_peca_id.get())
        if resposta:
            self.peca = resposta
            self.frame.pack_forget()
            self.update()
        else:
            messagebox.showinfo("Erro", "Por favor informe um id válido.")
            self.get_id()

    def update(self):
        self.frame = ttk.Labelframe(self, text="Update de peça")
        self.frame.grid(row=1, column=0, padx=10, pady=32)

        # Entry de custo de aquisição
        self.label_custo = tk.Label(self.frame, text="Custo de aquisição:")
        self.label_custo.pack(pady=10, padx=10)

        self.custo_aquisicao = tk.Entry(self.frame, width=30)
        self.custo_aquisicao.pack(pady=10, padx=10)

        # Checkbox de restauração
        opcoes = ct.tipos.values()
        tipo_label = tk.Label(self.frame, text="Ajustes:")
        tipo_label.pack()

        # Frame para os checkboxes
        checkbox_frame = tk.Frame(self.frame)
        checkbox_frame.pack(padx=10, pady=10)

        # Campo de detalhes
        self.label_desc = tk.Label(self.frame, text="Detalhes:")
        self.label_desc.pack(pady=10, padx=10)

        self.entry_descricao = tk.Entry(self.frame, width=30)
        self.entry_descricao.pack(pady=10, padx=10)

        # Criando listbox
        self.listbox = tk.Listbox(checkbox_frame,
                                  selectmode=tk.MULTIPLE,
                                  width=30, height=len(opcoes))
        for opcao in opcoes:
            self.listbox.insert(tk.END, opcao)
        self.listbox.pack(padx=10, pady=10)

        # Botão para pegar os dados
        ttk.Button(
            self.frame,
            text="Update",
            command=self.input_tests,
            bootstyle="success",
            width=30,
        ).pack(padx=10, pady=10)
        ttk.Button(
            self.frame,
            text="Retornar",
            command=self.controller.tela_menu,
            bootstyle="warning",
            width=30,
        ).pack(padx=10, pady=10)

    def input_tests(self):
        try:
            custo_aquisicao = float(self.custo_aquisicao.get())
            if custo_aquisicao:
                self.retornar()
        except ValueError:
            messagebox.showinfo(
                "Erro",
                "Por favor informe um valor válido de custo de aquisição."
            )

    def retornar(self):
        ajustes = []
        ajustes = self.listbox.curselection()

        if not ajustes:
            ajustes.append(0)

        self.peca.descricao = self.entry_descricao.get()
        self.peca.custo_aquisicao = self.custo_aquisicao.get()

        dados_update = {
            'id': self.peca.id,
            'custo_aquisicao': self.peca.custo_aquisicao,
            'descricao': self.peca.descricao,
            'status': 'em_restauracao',
            'ajustes': ajustes,
            'imagem': '',
            'titulo': '',
        }

        self.controller.update(dados_update)
        self.controller.tela_menu()


class MostrarPeca(tk.Frame):
    def __init__(self, master, controller, lista_pecas=None):
        super().__init__(master)
        self.controller = controller
        self.frame = None
        self.pecas = lista_pecas or []
        self.mostrar()

    def mostrar(self):
        self.frame = ttk.Labelframe(self, text="Peças disponíveis:")
        self.frame.grid(row=1, column=0, padx=10, pady=32)

        tree = ttk.Treeview(
            self.frame,
            columns=("Custo de aquisição", "Descrição", "Status",
                     "Restaurações"),
            bootstyle="success",
        )

        tree.heading("#0", text="ID")
        tree.heading("Custo de aquisição", text="Custo de aquisição")
        tree.heading("Descrição", text="Descrição")
        tree.heading("Status", text="Status")
        tree.heading("Restaurações", text="Restaurações")

        for peca in self.pecas:
            categorias_lista = []
            for ct in peca.status.categorias:
                categorias_lista.append(ct.nome)
            categorias = ", ".join(categorias_lista)
            tree.insert(
                "",
                "end",
                text=peca.id,
                values=(
                    peca.custo_aquisicao,
                    peca.descricao,
                    peca.status.__str__(),
                    categorias,
                ),
            )
        tree.pack(padx=10, pady=10)

        ttk.Button(
            self.frame,
            text="Retornar",
            command=self.controller.tela_menu,
            bootstyle="warning",
            width=30,
        ).pack(padx=10, pady=10)


class ApagarPeca(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.mensagem_erro = None
        self.frame = None
        self.controller = controller
        self.get_id()

    def get_id(self):
        if not self.frame:
            self.frame = ttk.Labelframe(self,
                                        text="Apagar",
                                        bootstyle="danger")
            self.frame.grid(row=1, column=0, padx=10, pady=32)

            label_peca_id = tk.Label(
                self.frame, text="Insira o id da peça a ser apagada:"
            )
            label_peca_id.pack(padx=10, pady=10)

            self.entry_peca_id = tk.Entry(self.frame, width=30)
            self.entry_peca_id.pack(padx=10, pady=10)

            ttk.Button(
                self.frame,
                text="Apagar",
                command=self.checar_id,
                bootstyle="danger",
                width=30,
            ).pack(padx=10, pady=10)

            ttk.Button(
                self.frame,
                text="Retornar",
                command=self.controller.tela_menu,
                bootstyle="warning",
                width=30,
            ).pack(padx=10, pady=10)

    def checar_id(self):
        resposta = self.controller.get_peca(self.entry_peca_id.get())
        if resposta:
            self.id_peca = resposta.id
            self.frame.pack_forget()
            self.retornar()
        else:
            messagebox.showinfo("Erro", "Por favor informe um id válido.")
            self.get_id()

    def retornar(self):
        self.controller.apagar(self.id_peca)
        self.controller.tela_menu()
