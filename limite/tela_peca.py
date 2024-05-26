import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from limite.tela_padrao import TelaPadrao
from persistencia.categorias_dao import CategoriasDAO as ctdao
from persistencia.categorias_dao import CategoriasDAO as ctdao
from entidade.status_tipos.statusRestauracao import StatusRestauracao
from entidade.categoria import Categorias as ct


class MenuPeca(TelaPadrao):
    def __init__(self, master, controlador, controladorUsuario, controladorPeca):
        self.controladorPeca = controladorPeca
        super().__init__(master, controlador, controladorUsuario)

    def conteudo(self):

        self.frame()

        self.button1 = ttk.Button(
            self.frame_principal,
            text="Registrar",
            command=self.controladorPeca.tela_registrar,
            bootstyle="secondary",
            width=30,
        )
        self.button1.pack(padx=10, pady=10)

        self.button2 = ttk.Button(
            self.frame_principal,
            text="Update",
            command=self.controladorPeca.tela_update,
            bootstyle="secondary",
            width=30,
        )
        self.button2.pack(padx=10, pady=10)

        self.button3 = ttk.Button(
            self.frame_principal,
            text="Apagar",
            command=self.controladorPeca.tela_apagar,
            bootstyle="secondary",
            width=30,
        )
        self.button3.pack(padx=10, pady=10)

        self.button4 = ttk.Button(
            self.frame_principal,
            text="Mostrar",
            command=self.controladorPeca.tela_mostrar,
            bootstyle="secondary",
            width=30,
        )
        self.button4.pack(padx=10, pady=10)

        self.button5 = ttk.Button(
            self.frame_principal,
            text="Retornar",
            command=self.controladorPeca.voltar,
            bootstyle="secondary",
            width=30,
        )
        self.button5.pack(padx=10, pady=10)

        self.button6 = ttk.Button(
            self.frame_principal,
            text="Restauração para a venda",
            command=self.controladorPeca.tela_rest_p_venda,
            bootstyle="secondary",
            width=30,
        )
        self.button6.pack(padx=10, pady=10)

    def frame(self):
        self.frame_principal = ttk.Frame(self,
                                    width=770,
                                    height=608,
                                    padding=20,
                                    style='light')

        self.frame_principal.pack(fill="none",
                             expand=False,
                             pady=32)

        titulo_label = ttk.Label(self.frame_principal,
                                text="MENU PEÇAS",
                                style="inverse-light",
                                font=("Helvetica", 14, "bold"))
        titulo_label.pack(pady=10, padx=10)


class RegistrarPeca(TelaPadrao):
    def __init__(self, master, controlador, controladorUsuario, controladorPeca, categorias):
        self.controladorPeca = controladorPeca
        self.categorias = categorias
        super().__init__(master, controlador, controladorUsuario)


    def conteudo(self):

        self.frame()

        # Entry de custo de aquisição
        self.label_custo = ttk.Label(self.frame_principal, text="Custo de aquisição:", style="inverse-light",)
        self.label_custo.pack(pady=10, padx=10)

        self.custo_aquisicao = ttk.Entry(self.frame_principal, width=30)
        self.custo_aquisicao.pack(pady=10, padx=10)

        opcoes = []
        for categoria in self.categorias:
            opcoes.append(categoria.nome)

        tipo_label = ttk.Label(self.frame_principal, text="Ajustes:", style="inverse-light",)
        tipo_label.pack()

        self.checkbox_vars = {}

        # Frame para os checkboxes
        checkbox_frame = ttk.Frame(self.frame_principal)
        checkbox_frame.pack(padx=10, pady=10)

        # Criando listbox
        self.listbox = tk.Listbox(checkbox_frame,
                                  selectmode=tk.MULTIPLE,
                                  width=30, height=len(opcoes))
        for opcao in opcoes:
            self.listbox.insert(tk.END, opcao)
        self.listbox.pack(padx=10, pady=10)

        # Campo de detalhes
        self.label_desc = ttk.Label(self.frame_principal, text="Detalhes:", style="inverse-light",)
        self.label_desc.pack(pady=10, padx=10)

        self.entry_descricao = ttk.Entry(self.frame_principal, width=30)
        self.entry_descricao.pack(pady=10, padx=10)

        # Botão para pegar os dados
        ttk.Button(
            self.frame_principal,
            text="Registrar",
            command=self.input_tests,
            bootstyle="success",
            width=30,
        ).pack(padx=10, pady=10)
        ttk.Button(
            self.frame_principal,
            text="Retornar",
            command=self.controladorPeca.tela_menu,
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
        self.controladorPeca.registrar(dados)
        self.controladorPeca.tela_menu()

    def frame(self):
        self.frame_principal = ttk.Frame(self,
                                    width=770,
                                    height=608,
                                    padding=20,
                                    style='light')

        self.frame_principal.pack(fill="none",
                             expand=False,
                             pady=32)

        titulo_label = ttk.Label(self.frame_principal,
                                text="REGISTRAR PEÇA",
                                style="inverse-light",
                                font=("Helvetica", 14, "bold"))
        titulo_label.pack(pady=10, padx=10)


class UpdatePeca(TelaPadrao):
    def __init__(self, master, controlador, controladorUsuario, controladorPeca, categorias):
        self.controladorPeca = controladorPeca
        self.categorias = categorias
        self.frame_principal = None
        super().__init__(master, controlador, controladorUsuario)


    def conteudo(self):
        if not self.frame_principal:
            self.frame()

            label_peca_id = ttk.Label(
                self.frame_principal, text="Insira o id da peça para fazer update:",
                style="inverse-light"
            )
            label_peca_id.pack()

            self.entry_peca_id = tk.Entry(self.frame_principal, width=30)
            self.entry_peca_id.pack(padx=10, pady=10)

            ttk.Button(
                self.frame_principal,
                text="Checar ID",
                command=self.checar_id,
                bootstyle="success",
                width=30,
            ).pack(padx=10, pady=10)
            ttk.Button(
                self.frame_principal,
                text="Retornar",
                command=self.controladorPeca.tela_menu,
                bootstyle="warning",
                width=30,
            ).pack(padx=10, pady=10)

    def checar_id(self):
        resposta = self.controladorPeca.get_peca(self.entry_peca_id.get())
        if resposta:
            self.peca = resposta
            self.frame_principal.pack_forget()
            self.update()
        else:
            messagebox.showinfo("Erro", "Por favor informe um id válido.")
            self.conteudo()

    def update(self):
        self.frame()

        # Entry de custo de aquisição
        self.label_custo = ttk.Label(self.frame_principal, text="Custo de aquisição:", style="inverse-light")
        self.label_custo.pack(pady=10, padx=10)

        self.custo_aquisicao = ttk.Entry(self.frame_principal, width=30)
        self.custo_aquisicao.pack(pady=10, padx=10)

        # Checkbox de restauração
        opcoes = []
        for categoria in self.categorias:
            opcoes.append(categoria.nome)
        tipo_label = ttk.Label(self.frame_principal, text="Ajustes:", style="inverse-light")
        tipo_label.pack()

        # Frame para os checkboxes
        checkbox_frame = ttk.Frame(self.frame_principal)
        checkbox_frame.pack(padx=10, pady=10)

        # Campo de detalhes
        self.label_desc = ttk.Label(self.frame_principal, text="Detalhes:", style="inverse-light")
        self.label_desc.pack(pady=10, padx=10)

        self.entry_descricao = ttk.Entry(self.frame_principal, width=30)
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
            self.frame_principal,
            text="Update",
            command=self.input_tests,
            bootstyle="success",
            width=30,
        ).pack(padx=10, pady=10)
        ttk.Button(
            self.frame_principal,
            text="Retornar",
            command=self.controladorPeca.tela_menu,
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
        ajustes = self.listbox.curselection()

        if not ajustes:
            ajustes = []
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
            'preco': 0
        }

        self.controladorPeca.update(dados_update)
        self.controladorPeca.tela_menu()
    def frame(self):
        self.frame_principal = ttk.Frame(self,
                                    width=770,
                                    height=608,
                                    padding=20,
                                    style='light')

        self.frame_principal.pack(fill="none",
                             expand=False,
                             pady=32)

        titulo_label = ttk.Label(self.frame_principal,
                                text="UPDATE PEÇA",
                                style="inverse-light",
                                font=("Helvetica", 14, "bold"))
        titulo_label.pack(pady=10, padx=10)


class MostrarPeca(TelaPadrao):
    def __init__(self, master, controlador, controladorUsuario, controladorPeca, lista_pecas=None):
        self.pecas = lista_pecas or []
        self.controladorPeca = controladorPeca
        super().__init__(master, controlador, controladorUsuario)

    def conteudo(self):
        self.frame()

        tree = ttk.Treeview(
            self.frame_principal,
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
            if isinstance(peca.status, StatusRestauracao):
                categorias_lista = []
                for ct in peca.status.categorias:
                    categorias_lista.append(ct.nome)
                categorias = ", ".join(categorias_lista)
            else:
                categorias = '--'
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
            self.frame_principal,
            text="Retornar",
            command=self.controladorPeca.tela_menu,
            bootstyle="warning",
            width=30,
        ).pack(padx=10, pady=10)

    def frame(self):
        self.frame_principal = ttk.Frame(self,
                                         width=770,
                                         height=608,
                                         padding=20,
                                         style='light')

        self.frame_principal.pack(fill="none",
                                  expand=False,
                                  pady=32)

        titulo_label = ttk.Label(self.frame_principal,
                                 text="MOSTRAR PEÇA",
                                 style="inverse-light",
                                 font=("Helvetica", 14, "bold"))
        titulo_label.pack(pady=10, padx=10)


class ApagarPeca(TelaPadrao):
    def __init__(self, master, controlador, controladorUsuario, controladorPeca):
        self.controladorPeca = controladorPeca
        self.frame_principal = None
        super().__init__(master, controlador, controladorUsuario)


    def conteudo(self):
        if not self.frame_principal:
            self.frame()

            label_peca_id = tk.Label(
                self.frame_principal, text="Insira o id da peça a ser apagada:"
            )
            label_peca_id.pack(padx=10, pady=10)

            self.entry_peca_id = tk.Entry(self.frame_principal, width=30)
            self.entry_peca_id.pack(padx=10, pady=10)

            ttk.Button(
                self.frame_principal,
                text="Apagar",
                command=self.checar_id,
                bootstyle="danger",
                width=30,
            ).pack(padx=10, pady=10)

            ttk.Button(
                self.frame_principal,
                text="Retornar",
                command=self.controladorPeca.tela_menu,
                bootstyle="warning",
                width=30,
            ).pack(padx=10, pady=10)

    def checar_id(self):
        resposta = self.controladorPeca.get_peca(self.entry_peca_id.get())
        if resposta:
            self.id_peca = resposta.id
            self.frame_principal.pack_forget()
            self.retornar()
        else:
            messagebox.showinfo("Erro", "Por favor informe um id válido.")
            self.conteudo()

    def retornar(self):
        self.controladorPeca.apagar(self.id_peca)
        self.controladorPeca.tela_menu()

    def frame(self):
        self.frame_principal = ttk.Frame(self,
                                         width=770,
                                         height=608,
                                         padding=20,
                                         style='light')

        self.frame_principal.pack(fill="none",
                                  expand=False,
                                  pady=32)

        titulo_label = ttk.Label(self.frame_principal,
                                 text="APAGAR PEÇA",
                                 style="inverse-light",
                                 font=("Helvetica", 14, "bold"))
        titulo_label.pack(pady=10, padx=10)
