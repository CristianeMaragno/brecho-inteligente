import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from limite.tela_padrao import TelaPadrao
from entidade.status_tipos.statusRestauracao import StatusRestauracao
from entidade.status_tipos.statusAVenda import StatusAVenda
from entidade.status_tipos.statusReserva import StatusReserva
from PIL import Image, ImageTk


class TelaBusca(TelaPadrao):
    def __init__(self, master, controlador, controladorUsuario,
                 controladorPeca, lista_pecas=None):
        self.pecas = lista_pecas or []
        self.controladorPeca = controladorPeca
        super().__init__(master, controlador, controladorUsuario)
        self.filtradas = self.pecas
        self.restauracao_menu = None

    def conteudo(self):
        self.frame()

        # Menu suspenso para escolha de busca
        self.search_var = tk.StringVar(value="ID")
        search_options = ["ID", "Restaurações"]
        self.search_menu = ttk.OptionMenu(self.frame_principal,
                                          self.search_var, search_options[0],
                                          *search_options,
                                          command=self.alterar_campo_busca)
        self.search_menu.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        # Campo de entrada para busca por ID
        self.search_entry = ttk.Entry(self.frame_principal)
        self.search_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        self.search_button = ttk.Button(self.frame_principal, text="Buscar",
                                        command=self.buscar_peca,
                                        style="success")
        self.search_button.grid(row=1, column=2, padx=10, pady=5, sticky="ew")

        # Botão "Mostrar Todas as Peças"
        self.reset_button = ttk.Button(self.frame_principal,
                                       text="Mostrar Todas as Peças",
                                       command=self.mostrar_todas_pecas)
        self.reset_button.grid(row=1, column=3, padx=10, pady=5, sticky="ew")

        self.tree = ttk.Treeview(
            self.frame_principal,
            columns=("status", "titulo", "descrição", "preço", "restaurações"),
            bootstyle="success",
        )

        self.tree.heading("#0", text="ID")
        self.tree.heading("status", text="status")
        self.tree.heading("titulo", text="titulo")
        self.tree.heading("descrição", text="descrição")
        self.tree.heading("preço", text="preço")
        self.tree.heading("restaurações", text="restaurações")

        self.atualizar_treeview(self.pecas)

        self.tree.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

        # Botão retornar
        ttk.Button(
            self.frame_principal,
            text="Retornar",
            command=self.controladorPeca.tela_menu,
            bootstyle="warning",
            width=30,
        ).grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky="w")

        # Botão de Informações
        self.info_button = ttk.Button(self.frame_principal, text="Informações", command=self.mostrar_informacoes)
        self.info_button.grid(row=3, column=3, padx=10, pady=10, sticky="e")

    def frame(self):
        self.frame_principal = ttk.Frame(
            self, width=770, height=608, padding=20, style="light"
        )

        self.frame_principal.grid(row=1, column=0, padx=10, pady=32)

        titulo_label = ttk.Label(
            self.frame_principal,
            text="MOSTRAR PEÇA",
            style="inverse-light",
            font=("Helvetica", 14, "bold"),
        )
        titulo_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="w")

    def alterar_campo_busca(self, criterio):
        # Remove o campo de entrada atual e o menu suspenso, se houver
        if self.search_entry:
            self.search_entry.grid_forget()
            self.search_entry = None
        if self.restauracao_menu:
            self.restauracao_menu.grid_forget()
            self.restauracao_menu = None

        if criterio == "ID":
            # Campo de entrada para busca por ID
            self.search_entry = ttk.Entry(self.frame_principal)
            self.search_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
        elif criterio == "Restaurações":
            # Menu suspenso para busca por restaurações
            restauracao_options = ["Nenhum ajuste", "Lavar", "Passar",
                                   "Reparar danos", "Restaurar detalhes",
                                   "Remover manchas", "Tingir", "Customizar"]
            self.restauracao_var = tk.StringVar(value=restauracao_options[0])
            self.restauracao_menu = ttk.OptionMenu(self.frame_principal,
                                                   self.restauracao_var,
                                                   restauracao_options[0],
                                                   *restauracao_options)
            self.restauracao_menu.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

    def buscar_peca(self):
        criterio = self.search_var.get()

        if criterio == "ID":
            busca = self.search_entry.get().strip()
            if not busca:
                messagebox.showerror("Erro", "Por favor, insira um valor para busca.")
                return
            resultados = [peca for peca in self.pecas if str(peca.id) == busca]
            self.atualizar_treeview(resultados)
        elif criterio == "Restaurações":
            busca = self.restauracao_var.get()
            resultados = [
                peca for peca in self.pecas
                if isinstance(peca.status, StatusRestauracao)
                and any(busca.lower() in ajuste.nome.lower() for ajuste in peca.status.categorias)
            ]
            self.atualizar_treeview(resultados, restauracao=True)
        else:
            messagebox.showinfo("Busca", "Tipo de Busca informado inválido.")
            self.atualizar_treeview([])

    def mostrar_todas_pecas(self):
        self.atualizar_treeview(self.pecas)

    def atualizar_treeview(self, pecas, restauracao=False):
        for item in self.tree.get_children():
            self.tree.delete(item)

        self.tree.pecas_map = {}

        if restauracao:
            self.tree["columns"] = ("status", "titulo", "descrição", "preço", "restaurações")
            self.tree.heading("#0", text="ID")
            self.tree.heading("status", text="status")
            self.tree.heading("titulo", text="titulo")
            self.tree.heading("descrição", text="descrição")
            self.tree.heading("preço", text="preço")
            self.tree.heading("restaurações", text="restaurações")
            for peca in pecas:
                titulo = peca.titulo if peca.titulo else "--"
                restauracoes = ", ".join([ajuste.nome for ajuste in peca.status.categorias]) if peca.status.categorias else "--"
                descricao = peca.descricao if peca.descricao else "--"
                preco = peca.preco if peca.preco else "--"
                tree_item_id = self.tree.insert(
                    "",
                    "end",
                    text=peca.id,
                    values=(peca.status.__str__(), titulo, descricao, preco, restauracoes),
                )
                self.tree.pecas_map[tree_item_id] = peca
        else:
            self.tree["columns"] = ("status", "titulo", "descrição", "preço", "restaurações")
            self.tree.heading("#0", text="ID")
            self.tree.heading("status", text="status")
            self.tree.heading("titulo", text="titulo")
            self.tree.heading("descrição", text="descrição")
            self.tree.heading("preço", text="preço")
            self.tree.heading("restaurações", text="restaurações")
            for peca in pecas:
                if isinstance(peca.status, StatusRestauracao):
                    categorias = ", ".join([ct.nome for ct in peca.status.categorias]) if peca.status.categorias else "--"
                else:
                    categorias = "--"
                titulo = peca.titulo if peca.titulo else "--"
                descricao = peca.descricao if peca.descricao else "--"
                preco = peca.preco if peca.preco else "--"
                tree_item_id = self.tree.insert(
                    "",
                    "end",
                    text=peca.id,
                    values=(
                        peca.status.__str__(),
                        titulo,
                        descricao,
                        preco,
                        categorias,
                    ),
                )
                self.tree.pecas_map[tree_item_id] = peca

    def mostrar_informacoes(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showinfo("Informação", "Por favor, selecione uma peça na lista.")
            return

        peca = self.tree.pecas_map[selected_item[0]]

        # Criando o Toplevel para as informações
        info_popup = tk.Toplevel(self)
        info_popup.title("Informações da Peça")

        popup_width = 800
        popup_height = 400

        screen_width = info_popup.winfo_screenwidth()
        screen_height = info_popup.winfo_screenheight()

        x = int((screen_width / 2) - (popup_width / 2))
        y = int((screen_height / 2) - (popup_height / 2))

        # Centralizar o popup
        info_popup.geometry(f"{popup_width}x{popup_height}+{x}+{y}")

        imagem = ttk.Label(info_popup, text="[Imagem]", style="inverse.light.TLabel")
        imagem.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        self.load_and_display_image(peca.imagem, imagem)

        if isinstance(peca.status, StatusRestauracao):
            info_text = (
                f"ID: {peca.id}\n"
                f"Status: {peca.status.__str__()}\n"
                f"Título: {peca.titulo}\n"
                f"Descrição: {peca.descricao}\n"
                f"Preço: {peca.preco}\n"
                f"Restaurações: {', '.join([ajuste.nome for ajuste in peca.status.categorias]) if peca.status.categorias else '--'}"
            )

        elif isinstance(peca.status, StatusAVenda):

            info_text = (
                f"ID: {peca.id}\n"
                f"Status: {peca.status.__str__()}\n"
                f"Título: {peca.titulo}\n"
                f"Descrição: {peca.descricao}\n"
                f"Preço: {peca.preco}\n"
            )
            if peca.status.vendido:
                info_text += (
                    "Vendido: Sim\n"
                    f"Desconto: {peca.status.desconto}\n"
                    f"Forma de Pagamento: {peca.status.forma_pagamento}\n"
                )
            else:
                info_text += (
                    "Vendido: Não\n"
                )
        elif isinstance(peca.status, StatusReserva):

            info_text = (
                f"ID: {peca.id}\n"
                f"Status: {peca.status.__str__()}\n"
                f"Título: {peca.titulo}\n"
                f"Descrição: {peca.descricao}\n"
                f"Preço: {peca.preco}\n"
                f"Data Limite: {peca.status.data}\n"
                f"Nome do cliente: {peca.status.nome}\n"
                f"Telefone do cliente: {peca.status.telefone}\n"
            )

        info_label = ttk.Label(info_popup, text=info_text, padding=10)
        info_label.grid(row=1, column=0, sticky="nsew")

        info_popup.grid_rowconfigure(1, weight=1)
        info_popup.grid_columnconfigure(0, weight=1)

    def load_and_display_image(self, file_path, imagem_label):
        try:
            image = Image.open(file_path)
            image = image.resize((150, 150), Image.LANCZOS)
            image_tk = ImageTk.PhotoImage(image)
            imagem_label.config(image=image_tk)
            imagem_label.image = image_tk
        except Exception as e:
            messagebox.showinfo("Erro", f"Erro ao carregar imagem: {e}")
