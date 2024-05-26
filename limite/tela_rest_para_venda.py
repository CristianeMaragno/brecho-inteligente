from limite.tela_padrao import TelaPadrao
import ttkbootstrap as ttk
from tkinter import messagebox
import tkinter as tk
import re
from tkinter import filedialog
from PIL import Image, ImageTk


class TelaRestauracaoParaVenda1(TelaPadrao):
    def __init__(self, master, controlador, controladorUsuario, controladorPeca):
        self.controladorPeca = controladorPeca
        self.peca_selecionada = None
        super().__init__(master, controlador, controladorUsuario)

    def conteudo(self):
        self.frame()

        self.frame_secundario = ttk.Frame(self.frame_principal, style='light')
        self.frame_secundario.pack()
        # Criação dos frames
        self.criar_frame_direito()
        # Frame esquerdo
        if self.peca_selecionada:
            self.criar_frame_esquerdo()

    def criar_frame_direito(self):
        # Navegação das peças por ID
        pecas = self.controladorPeca.pdao.get_all()
        ids_das_pecas = []
        if pecas:
            for peca in pecas:
                ids_das_pecas.append(peca.id)

        # Definindo o frame direito
        self.frame_direito = ttk.Frame(
            self.frame_secundario,
            width=770,
            height=608,
            padding=20,
            style='light'
        )
        self.frame_direito.grid(row=1, column=1, sticky="n")

        self.frame_peca_info = ttk.Frame(self.frame_direito,
                                         style="light")
        self.frame_peca_info.pack()

        label_id = ttk.Label(self.frame_peca_info,
                             text='ID',
                             style="inverse-light",
                             font=("Helvetica", 12))
        label_id.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.combobox = ttk.Combobox(self.frame_peca_info,
                                     bootstyle="primary",
                                     values=ids_das_pecas,
                                     font=("Helvetica", 10))
        self.combobox.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        self.combobox.bind("<<ComboboxSelected>>", self.apresentar_infos)

        if not self.peca_selecionada:
            self.peca_selecionada = self.controladorPeca.pdao.get_by_id(ids_das_pecas[0])
            print(self.peca_selecionada)

        label_custo_aquisicao = ttk.Label(self.frame_peca_info,
                                          text='Custo aquisição',
                                          style="inverse-light",
                                          font=("Helvetica", 10))
        label_custo_aquisicao.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        custo_aquisicao = f'R${self.peca_selecionada.custo_aquisicao}'
        label_valor_custo_aquisicao = ttk.Label(self.frame_peca_info,
                                                text=custo_aquisicao,
                                                style="inverse-light",
                                                font=("Helvetica", 10))
        label_valor_custo_aquisicao.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        label_descricao = ttk.Label(self.frame_peca_info,
                                    text='Descrição',
                                    style="inverse-light",
                                    font=("Helvetica", 10))
        label_descricao.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.descricao_peca = ttk.Entry(self.frame_peca_info,
                                        bootstyle='primary')
        self.descricao_peca.insert(0, self.peca_selecionada.descricao)
        self.descricao_peca.bind("<FocusIn>", self.clear_descricao_placeholder)
        self.descricao_peca.bind("<FocusOut>", self.restore_descricao_placeholder)
        self.descricao_peca.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        # Botão enviar para a venda
        self.botao_enviar_venda = ttk.Button(self.frame_direito,
                                             text="Voltar",
                                             width=30,
                                             command=self.controladorPeca.
                                             tela_menu)
        self.botao_enviar_venda.pack(padx=10, pady=10)

        # Botão de voltar
        self.botao_voltar = ttk.Button(self.frame_direito,
                                       text="Enviar para venda",
                                       width=30,
                                       command=self.prosseguir)
        self.botao_voltar.pack(padx=10, pady=5)

    def apresentar_infos(self, event):
        self.peca_selecionada = self.controladorPeca.pdao.get_by_id(self.combobox.get())
        self.criar_frame_direito()
        self.criar_frame_esquerdo()

    def criar_frame_esquerdo(self):
        self.frame_esquerdo = ttk.Frame(
            self.frame_secundario,
            width=770,
            height=608,
            padding=20,
            style='light'
        )
        self.frame_esquerdo.grid(row=1, column=0, sticky="n")

        self.combobox.set(self.peca_selecionada.id)

        frame_tabela = ttk.Frame(self.frame_esquerdo)
        frame_tabela.pack(expand=False)

        # Definindo a estrutura da tabela

        # 1. Headers
        label_coluna_1 = ttk.Label(frame_tabela, text='AJUSTES', font=("Helvetica", 9, "bold"))
        label_coluna_2 = ttk.Label(frame_tabela, text='CUSTO PADRÃO', font=("Helvetica", 9, "bold"))
        label_coluna_3 = ttk.Label(frame_tabela, text='CUSTO MODIFICADO', font=("Helvetica", 9, "bold"))
        label_coluna_4 = ttk.Label(frame_tabela, text='FEITO', font=("Helvetica", 9, "bold"))

        label_coluna_1.grid(row=0, column=0, padx=10, pady=10)
        label_coluna_2.grid(row=0, column=1, padx=10, pady=10)
        label_coluna_3.grid(row=0, column=2, padx=10, pady=10)
        label_coluna_4.grid(row=0, column=3, padx=10, pady=10)

        # 2. Conteúdo
        categorias = self.peca_selecionada.status.categorias
        self.custo_entrys = []

        i = 1
        for categoria in categorias:
            label_categoria = ttk.Label(frame_tabela, text=categoria.nome)
            label_categoria.grid(row=i, column=0, padx=10, pady=10)

            label_custo_padrao = ttk.Label(frame_tabela, text=categoria.custo_padrao)
            label_custo_padrao.grid(row=i, column=1, padx=10, pady=10)

            entry_custo_padrao = ttk.Entry(frame_tabela, bootstyle="info")
            entry_custo_padrao.grid(row=i, column=2, padx=10, pady=10)

            default_var = tk.BooleanVar()
            default_var.set(True)
            feito_checkbox = ttk.Checkbutton(frame_tabela, style="secondary", variable=default_var)
            feito_checkbox.grid(row=i, column=3, padx=10, pady=10)

            self.custo_entrys.append([entry_custo_padrao, categoria, default_var])

            i+=1

        # 3. Botão calcular total
        self.botao_calcular = ttk.Button(self.frame_esquerdo,
                                       text="Calcular total",
                                       width=30,
                                       command=self.calcular_total)
        self.botao_calcular.pack(padx=10, pady=10, expand=False)

        # Total
        texto = f'TOTAL: R$ 0.0'
        self.total_label = ttk.Label(self.frame_esquerdo,
                                     text=texto,
                                     style="inverse-light",
                                     font=("Helvetica", 11, "bold"))
        self.total_label.pack(padx=10, pady=10, expand=False)

    def calcular_total(self):
        self.valor_total = 0
        for entry, categoria, feito in self.custo_entrys:
            try:
                if len(entry.get()) == 0:
                    self.valor_total += 0
                else:
                    valor = float(entry.get())
                    if valor and feito.get():
                        self.valor_total += valor
            except ValueError:
                messagebox.showinfo(
                    "Erro",
                    "Por favor informe um valor válido de custo."
                )
        self.apresentar_total(self.valor_total)

    def apresentar_total(self, valor_total):
        self.total_label.destroy()
        texto = f'TOTAL: R${valor_total}'
        self.total_label = ttk.Label(self.frame_esquerdo,
                          text=texto,
                          style="inverse-light",
                          font=("Helvetica", 11, "bold"))
        self.total_label.pack(padx=10, pady=10, expand=False)

    def prosseguir(self):

        if self.descricao_peca.get():
            print("Nova descrição: ", self.descricao_peca.get())

        self.calcular_total()
        # Update dos valores adquiridos
        custo_total = self.valor_total
        self.peca_selecionada.status.custo_total = custo_total
        self.peca_selecionada.descricao = self.descricao_peca.get()

        self.controladorPeca.tela_rest_p_venda(self.peca_selecionada)

    def clear_descricao_placeholder(self, event):
        if self.descricao_peca.get() == "Email":
            self.descricao_peca.delete(0, tk.END)

    def restore_descricao_placeholder(self, event):
        if not self.descricao_peca.get():
            self.descricao_peca.insert(0, "Email")

    def frame(self):
        self.frame_principal = ttk.Frame(self,
                                width=770,
                                height=608,
                                padding=20,
                                style='light')

        self.frame_principal.grid(row=1, column=0, padx=10, pady=32)

        self.titulo = ttk.Label(self.frame_principal,
                                 text="Disponibilização de peça em restauração para a venda",
                                 style="inverse-light",
                                 font=("Helvetica", 14, "bold"))
        self.titulo.pack(padx=10, pady=10)

class TelaRestauracaoParaVenda2(TelaPadrao):
    def __init__(self, master, controlador, controladorUsuario, controladorPeca, peca):
        self.controladorPeca = controladorPeca
        self.peca = peca
        super().__init__(master, controlador, controladorUsuario)

    def conteudo(self):

        print(self.peca.id)
        print(self.peca.custo_aquisicao)
        print(self.peca.status.categorias)
        print(self.peca.descricao)
        self.frame()

        self.frame_secundario = ttk.Frame(self.frame_principal)
        self.frame_secundario.pack()

        # 1. Entrys e labels

        # Título
        self.entry_titulo = ttk.Entry(self.frame_secundario, width=50)
        self.entry_titulo.insert(0, 'Título')
        self.entry_titulo.bind("<FocusIn>", self.clear_titulo_placeholder)
        self.entry_titulo.bind("<FocusOut>", self.restore_titulo_placeholder)
        self.entry_titulo.grid(row=0, column=0, padx=10, pady=10)

        # Preço final

        self.entry_preco = ttk.Entry(self.frame_secundario, width=50)
        self.entry_preco.insert(0, 'Preço final')
        self.entry_preco.bind("<FocusIn>", self.clear_preco_placeholder)
        self.entry_preco.bind("<FocusOut>", self.restore_preco_placeholder)
        self.entry_preco.grid(row=4, column=0, padx=10, pady=10)

        # Imagem

        botao_imagem = ttk.Button(self.frame_secundario,
                            text="Select Image",
                            command=self.open_file_dialog,
                            width=50)
        botao_imagem.grid(row=1, column=0, padx=10, pady=10)

        self.image_label = ttk.Label(self.frame_secundario)
        self.image_label.grid(row=2, column=0, padx=10, pady=10)
        self.path_imagem = None

        # 2. Tabela

        tabela_frame = ttk.Frame(self.frame_secundario)
        tabela_frame.grid(row=3, column=0, padx=10, pady=10)

        linha_um = ttk.Label(tabela_frame, text='CUSTO AQUISIÇÃO', font=("Helvetica", 12))
        linha_um.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        linha_dois = ttk.Label(tabela_frame, text='CUSTO DE AJUSTES', font=("Helvetica", 12))
        linha_dois.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        linha_tres = ttk.Label(tabela_frame, text='TAXA LUCRO', font=("Helvetica", 12))
        linha_tres.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        linha_quatro = ttk.Label(tabela_frame, text='PREÇO SUGERIDO', font=("Helvetica", 12))
        linha_quatro.grid(row=3, column=0, padx=5, pady=5, sticky="w")

        custo_aquisicao = self.peca.custo_aquisicao
        valor_um = ttk.Label(tabela_frame, text=custo_aquisicao, font=("Helvetica", 12, "bold"))
        valor_um.grid(row=0, column=1, padx=5, pady=5, sticky="e")

        custo_ajustes = self.peca.status.custo_total
        valor_dois = ttk.Label(tabela_frame, text=custo_ajustes, font=("Helvetica", 12, "bold"))
        valor_dois.grid(row=1, column=1, padx=5, pady=5, sticky="e")

        taxa_lucro = 0 # Modificar para o valor da calculadora
        valor_tres = ttk.Label(tabela_frame, text=taxa_lucro, font=("Helvetica", 12, "bold"))
        valor_tres.grid(row=2, column=1, padx=5, pady=5, sticky="e")

        valor_sugerido = custo_aquisicao + custo_ajustes + taxa_lucro
        valor_quatro = ttk.Label(tabela_frame, text=valor_sugerido, font=("Helvetica", 12, "bold"))
        valor_quatro.grid(row=3, column=1, padx=5, pady=5, sticky="e")

        # 3. Botões
        self.botao_calcular = ttk.Button(self.frame_principal,
                                         text="Colocar à venda",
                                         width=50,
                                         command=self.checar_valores)
        self.botao_calcular.pack(padx=10, pady=10, expand=False)

        self.botao_enviar_venda = ttk.Button(self.frame_principal,
                                             text="Voltar",
                                             width=50,
                                             command=self.controladorPeca.
                                             tela_rest_p_venda)
        self.botao_enviar_venda.pack(padx=10, pady=10)

    def checar_valores(self):
        try:
            titulo = self.entry_titulo.get()
            preco = self.entry_preco.get()
            if float(preco) and titulo:
                self.prosseguir()
        except ValueError:
            messagebox.showinfo(
                "Erro",
                "Por favor informe um título e um preço válido."
            )

    def prosseguir(self):
        self.peca.titulo = self.entry_titulo.get()
        self.peca.preco = self.entry_preco.get()
        if self.path_imagem:
            self.peca.imagem = self.path_imagem

        dados_update = {
            'id': self.peca.id,
            'custo_aquisicao': self.peca.custo_aquisicao,
            'descricao': self.peca.descricao,
            'status': 'a_venda',
            'imagem': self.peca.imagem,
            'titulo': self.peca.titulo,
        }

        # Update DAO
        self.controladorPeca.update(dados_update)

    def clear_titulo_placeholder(self, event):
        if self.entry_titulo.get() == "Título":
            self.entry_titulo.delete(0, tk.END)

    def restore_titulo_placeholder(self, event):
        if not self.entry_titulo.get():
            self.entry_titulo.insert(0, "Título")

    def clear_preco_placeholder(self, event):
        if self.entry_preco.get() == "Preço final":
            self.entry_preco.delete(0, tk.END)

    def restore_preco_placeholder(self, event):
        if not self.entry_preco.get():
            self.entry_preco.insert(0, "Preço final")

    def open_file_dialog(self):
        # Open a file dialog to select an image
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif")]
        )
        if file_path:
            self.path_imagem = file_path
            self.load_and_display_image(file_path)

    def load_and_display_image(self, file_path):
        try:
            image = Image.open(file_path)
            image = image.resize((300, 300), Image.ANTIALIAS)
            image_tk = ImageTk.PhotoImage(image)
            self.image_label.config(image=image_tk)
            self.image_label.image = image_tk
        except Exception as e:
            print(f"Error loading image: {e}")

    def frame(self):
        self.frame_principal = ttk.Frame(self,
                                width=770,
                                height=608,
                                padding=20,
                                style='light')

        self.frame_principal.grid(row=1, column=0, padx=10, pady=32)

        self.titulo = ttk.Label(self.frame_principal,
                                 text=self.peca.id,
                                 style="inverse-light",
                                 font=("Helvetica", 14, "bold"))
        self.titulo.pack(padx=10, pady=10)
