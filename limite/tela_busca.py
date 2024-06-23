import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from limite.tela_padrao import TelaPadrao
from entidade.status_tipos.statusRestauracao import StatusRestauracao

class TelaBusca(TelaPadrao):
    def __init__(self, master, controlador, controladorUsuario, controladorPeca, lista_pecas=None):
        self.pecas = lista_pecas or []
        self.controladorPeca = controladorPeca
        super().__init__(master, controlador, controladorUsuario)
        self.filtradas = self.pecas
        self.restauracao_menu = None

    def conteudo(self):
        self.frame()
        
        # Adiciona o menu suspenso para escolha de busca
        self.search_var = tk.StringVar(value="ID")
        search_options = ["ID", "Restaurações"]
        self.search_menu = ttk.OptionMenu(self.frame_principal, self.search_var, search_options[0], *search_options, command=self.alterar_campo_busca)
        self.search_menu.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        
        # Campo de entrada inicial para busca por ID
        self.search_entry = ttk.Entry(self.frame_principal)
        
        # Adiciona o campo de entrada para busca por ID (inicialmente oculto)
        self.search_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
        
        self.search_button = ttk.Button(self.frame_principal, text="Buscar", command=self.buscar_peca, style="success")
        self.search_button.grid(row=1, column=2, padx=10, pady=5, sticky="ew")

        
        # Adiciona o botão "Mostrar Todas as Peças"
        self.reset_button = ttk.Button(self.frame_principal, text="Mostrar Todas as Peças", command=self.mostrar_todas_pecas)
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

        # Adiciona o botão para retornar à visualização padrão
        ttk.Button(
            self.frame_principal,
            text="Retornar",
            command=self.controladorPeca.tela_menu,
            bootstyle="warning",
            width=30,
        ).grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky="w")

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
            # Adiciona o campo de entrada para busca por ID
            self.search_entry = ttk.Entry(self.frame_principal)
            self.search_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
        elif criterio == "Restaurações":
            # Adiciona o menu suspenso para busca por restaurações
            restauracao_options = ["Nenhum ajuste", "Lavar", "Passar", "Reparar danos", "Restaurar detalhes", "Remover manchas", "Tingir", "Customizar"]
            self.restauracao_var = tk.StringVar(value=restauracao_options[0])
            self.restauracao_menu = ttk.OptionMenu(self.frame_principal, self.restauracao_var, restauracao_options[0], *restauracao_options)
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
            messagebox.showinfo("Busca", "Nenhuma peça encontrada para o critério de busca informado.")
            self.atualizar_treeview([])

    def mostrar_todas_pecas(self):
        self.atualizar_treeview(self.pecas)

    def atualizar_treeview(self, pecas, restauracao=False):
        for item in self.tree.get_children():
            self.tree.delete(item)

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

                # Quebra de texto simulada para o título
                if len(titulo) > 30:  # Limite arbitrário para quebra de texto
                    linhas = []
                    while len(titulo) > 30:
                        linhas.append(titulo[:30])
                        titulo = titulo[30:]
                    linhas.append(titulo)
                    titulo = "\n".join(linhas)

                self.tree.insert(
                    "",
                    "end",
                    text=peca.id,
                    values=(peca.status.__str__(), titulo, descricao, preco, restauracoes),
                )
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

                # Quebra de texto simulada para o título
                if len(titulo) > 30:  # Limite arbitrário para quebra de texto
                    linhas = []
                    while len(titulo) > 30:
                        linhas.append(titulo[:30])
                        titulo = titulo[30:]
                    linhas.append(titulo)
                    titulo = "\n".join(linhas)

                self.tree.insert(
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
