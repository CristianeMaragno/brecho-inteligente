from limite.tela_padrao import TelaPadrao
from entidade.status_tipos.statusRestauracao import StatusRestauracao
import ttkbootstrap as ttk
from tkinter import messagebox
import tkinter as tk
import re
from tkinter import filedialog
from PIL import Image, ImageTk


class TelaRestauracaoParaVenda1(TelaPadrao):
    def __init__(
        self,
        master,
        controlador,
        controladorUsuario,
        controladorPeca,
    ):
        self.controladorPeca = controladorPeca
        self.peca_selecionada = None
        super().__init__(master, controlador, controladorUsuario)

    def conteudo(self):

        # Cria o frame principal
        self.frame()

        # Checa se há peças
        ha_pecas = self.checar_se_ha_pecas()

        # Se sim, cria o frame secundário e os frames direito e esquerdo (implementar com alt)
        if ha_pecas:
            self.frame_secundario = ttk.Frame(self.frame_principal, style="light")
            self.frame_secundario.pack()

            self.criar_frame_esquerdo()
            self.criar_frame_direito()

        # Se não, passa para a tela de que não há peças
        else:
            self.nao_ha_pecas()

    def checar_se_ha_pecas(self):
        # Pega todas as peças
        pecas = self.controladorPeca.pdao.get_all()

        # Coloca todos os IDs das peças em restaução dentro
        if pecas:
            self.ids_das_pecas = []
            for peca in pecas:
                if isinstance(peca.status, StatusRestauracao):
                    self.ids_das_pecas.append(peca.id)

            # Arruma uma lista com os IDs das peças
            if self.ids_das_pecas:
                self.peca_selecionada = self.controladorPeca.pdao.get_by_id(
                    self.ids_das_pecas[0]
                )

        # Retorna a primeira peça em restauração (se houver)
        return self.peca_selecionada

    def nao_ha_pecas(self):

        # Cria o label de que não há peças
        label = ttk.Label(
            self.frame_principal,
            text="Não há peças para colocar à venda.",
            style="inverse-light",
            font=("Helvetica", 12, "bold"),
        )
        label.pack(padx=10, pady=10)

        # Botão de voltar
        self.botao_voltar = ttk.Button(
            self.frame_principal,
            text="Voltar",
            width=30,
            command=self.controladorPeca.tela_menu,
        )
        self.botao_voltar.pack(padx=10, pady=5)

    def criar_frame_direito(self):

        # Definindo o frame direito
        self.frame_direito = ttk.Frame(
            self.frame_secundario, width=770, height=608, padding=20, style="light"
        )
        self.frame_direito.grid(row=1, column=1, sticky="n")

        self.frame_peca_info = ttk.Frame(self.frame_direito, style="light")
        self.frame_peca_info.pack()

        label_id = ttk.Label(
            self.frame_peca_info,
            text="ID",
            style="inverse-light",
            font=("Helvetica", 12),
        )
        label_id.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.combobox = ttk.Combobox(
            self.frame_peca_info,
            bootstyle="primary",
            values=self.ids_das_pecas,
            font=("Helvetica", 10),
        )
        self.combobox.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        self.combobox.bind("<<ComboboxSelected>>", self.apresentar_infos)
        self.combobox.set(self.peca_selecionada.id)

        label_custo_aquisicao = ttk.Label(
            self.frame_peca_info,
            text="Custo aquisição",
            style="inverse-light",
            font=("Helvetica", 10),
        )
        label_custo_aquisicao.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        custo_aquisicao = f"R${self.peca_selecionada.custo_aquisicao}"
        label_valor_custo_aquisicao = ttk.Label(
            self.frame_peca_info,
            text=custo_aquisicao,
            style="inverse-light",
            font=("Helvetica", 10),
        )
        label_valor_custo_aquisicao.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        label_descricao = ttk.Label(
            self.frame_peca_info,
            text="Descrição",
            style="inverse-light",
            font=("Helvetica", 10),
        )
        label_descricao.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.descricao_peca = ttk.Entry(self.frame_peca_info, bootstyle="primary")
        self.descricao_peca.insert(0, self.peca_selecionada.descricao)
        self.descricao_peca.bind("<FocusIn>", self.clear_descricao_placeholder)
        self.descricao_peca.bind("<FocusOut>", self.restore_descricao_placeholder)
        self.descricao_peca.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        # Botão de voltar ao menu
        self.botao_voltar = ttk.Button(
            self.frame_direito,
            text="Voltar",
            width=30,
            command=self.controladorPeca.tela_menu,
        )
        self.botao_voltar.pack(padx=10, pady=10)

        # Botão de enviar para a venda
        self.botao_enviar_venda = ttk.Button(
            self.frame_direito,
            text="Enviar para venda",
            width=30,
            command=self.prosseguir,
        )
        self.botao_enviar_venda.pack(padx=10, pady=5)

    def apresentar_infos(self, event):
        # Método chamado sempre que o ID é mudado no combobox do frame direito
        peca_selecionada_id = self.combobox.get()
        self.peca_selecionada = self.controladorPeca.pdao.get_by_id(peca_selecionada_id)
        self.criar_frame_direito()
        self.criar_frame_esquerdo()

    def criar_frame_esquerdo(self):
        # Definindo o frame esquerdo
        self.frame_esquerdo = ttk.Frame(
            self.frame_secundario, width=770, height=608, padding=20, style="light"
        )
        self.frame_esquerdo.grid(row=1, column=0, sticky="n")

        frame_tabela = ttk.Frame(self.frame_esquerdo)
        frame_tabela.pack(expand=False)

        # Definindo a estrutura da tabela

        # Headers
        label_coluna_1 = ttk.Label(
            frame_tabela, text="AJUSTES", font=("Helvetica", 9, "bold")
        )
        label_coluna_2 = ttk.Label(
            frame_tabela, text="CUSTO PADRÃO", font=("Helvetica", 9, "bold")
        )
        label_coluna_3 = ttk.Label(
            frame_tabela, text="CUSTO MODIFICADO", font=("Helvetica", 9, "bold")
        )
        label_coluna_4 = ttk.Label(
            frame_tabela, text="FEITO", font=("Helvetica", 9, "bold")
        )

        label_coluna_1.grid(row=0, column=0, padx=10, pady=10)
        label_coluna_2.grid(row=0, column=1, padx=10, pady=10)
        label_coluna_3.grid(row=0, column=2, padx=10, pady=10)
        label_coluna_4.grid(row=0, column=3, padx=10, pady=10)

        # Conteúdo
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
            feito_checkbox = ttk.Checkbutton(
                frame_tabela, style="secondary", variable=default_var
            )
            feito_checkbox.grid(row=i, column=3, padx=10, pady=10)

            self.custo_entrys.append([entry_custo_padrao, categoria, default_var])

            i += 1

        # Botão calcular total
        self.botao_calcular = ttk.Button(
            self.frame_esquerdo,
            text="Calcular total",
            width=30,
            command=self.apresentar_total,
        )
        self.botao_calcular.pack(padx=10, pady=10, expand=False)

        # Total
        texto = f"TOTAL: R$ 0.0"
        self.total_label = ttk.Label(
            self.frame_esquerdo,
            text=texto,
            style="inverse-light",
            font=("Helvetica", 11, "bold"),
        )
        self.total_label.pack(padx=10, pady=10, expand=False)

    def calcular_total(self):
        self.valor_total = 0
        passou_validacao = True

        # Validação dos valores de custo apresentados
        for entry, categoria, feito in self.custo_entrys:
            try:
                custo = entry.get()
                if len(custo) == 0:
                    self.valor_total += categoria.custo_padrao
                if len(custo) > 0:
                    valor = float(entry.get())
                    if valor and feito.get():
                        self.valor_total += valor
            except ValueError:
                passou_validacao = False

        return passou_validacao

    def apresentar_total(self):
        passou_validacao = self.calcular_total()
        # Só apresenta o novo total na tela se ele passou a validação (alt)
        if passou_validacao:
            self.total_label.destroy()
            texto = f"TOTAL: R${self.valor_total}"
            self.total_label = ttk.Label(
                self.frame_esquerdo,
                text=texto,
                style="inverse-light",
                font=("Helvetica", 11, "bold"),
            )
            self.total_label.pack(padx=10, pady=10, expand=False)
        else:
            self.apresentar_msg_erro("Por favor informe valores válidos de custo.")

    def prosseguir(self):

        passou_validacao = self.calcular_total()

        # Update dos valores adquiridos (alt)
        if passou_validacao:
            custo_total = self.valor_total
            self.peca_selecionada.status.custo_total = custo_total
            self.peca_selecionada.descricao = self.descricao_peca.get()
            self.controladorPeca.tela_rest_p_venda(self.peca_selecionada)
        else:
            self.apresentar_msg_erro("Por favor informe valores válidos de custo.")

    # Métodos auxiliares para apara e remover a descrição
    def clear_descricao_placeholder(self, event):
        self.descricao_peca.delete(0, tk.END)

    def restore_descricao_placeholder(self, event):
        if not self.descricao_peca.get():
            self.descricao_peca.insert(0, self.peca_selecionada.descricao)

    # Método que apresenta uma mensagem de erro
    def apresentar_msg_erro(self, msg):
        messagebox.showinfo("Erro", msg)

    def frame(self):
        # Forma o frame principal
        self.frame_principal = ttk.Frame(
            self, width=770, height=608, padding=20, style="light"
        )

        self.frame_principal.grid(row=1, column=0, padx=10, pady=32)

        self.titulo = ttk.Label(
            self.frame_principal,
            text="Disponibilização de peça em restauração para a venda",
            style="inverse-light",
            font=("Helvetica", 14, "bold"),
        )
        self.titulo.pack(padx=10, pady=10)


class TelaRestauracaoParaVenda2(TelaPadrao):
    def __init__(
        self,
        master,
        controlador,
        controladorUsuario,
        controladorPeca,
        peca,
    ):
        self.controladorPeca = controladorPeca
        self.peca = peca
        super().__init__(master, controlador, controladorUsuario)

    def conteudo(self):
        self.frame()

        self.frame_secundario = ttk.Frame(self.frame_principal)
        self.frame_secundario.pack()

        # 1. Entrys e labels

        # Título
        self.entry_titulo = ttk.Entry(self.frame_secundario, width=50)
        self.entry_titulo.insert(0, "Título")
        self.entry_titulo.bind("<FocusIn>", self.clear_titulo_placeholder)
        self.entry_titulo.bind("<FocusOut>", self.restore_titulo_placeholder)
        self.entry_titulo.grid(row=0, column=0, padx=10, pady=10)

        # Preço final

        self.entry_preco = ttk.Entry(self.frame_secundario, width=50)
        self.entry_preco.insert(0, "Preço final")
        self.entry_preco.bind("<FocusIn>", self.clear_preco_placeholder)
        self.entry_preco.bind("<FocusOut>", self.restore_preco_placeholder)
        self.entry_preco.grid(row=4, column=0, padx=10, pady=10)

        # Imagem

        botao_imagem = ttk.Button(
            self.frame_secundario,
            text="Selecionar imagem",
            command=self.open_file_dialog,
            width=50,
        )
        botao_imagem.grid(row=1, column=0, padx=10, pady=10)

        self.image_label = ttk.Label(self.frame_secundario)
        self.image_label.grid(row=2, column=0, padx=10, pady=10)
        self.path_imagem = None

        # 2. Tabela

        tabela_frame = ttk.Frame(self.frame_secundario)
        tabela_frame.grid(row=3, column=0, padx=10, pady=10)

        linha_um = ttk.Label(
            tabela_frame, text="CUSTO AQUISIÇÃO", font=("Helvetica", 12)
        )
        linha_um.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        linha_dois = ttk.Label(
            tabela_frame, text="CUSTO DE AJUSTES", font=("Helvetica", 12)
        )
        linha_dois.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        linha_tres = ttk.Label(tabela_frame, text="TAXA LUCRO", font=("Helvetica", 12))
        linha_tres.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        linha_quatro = ttk.Label(
            tabela_frame, text="PREÇO SUGERIDO", font=("Helvetica", 12)
        )
        linha_quatro.grid(row=3, column=0, padx=5, pady=5, sticky="w")

        custo_aquisicao = self.peca.custo_aquisicao
        valor_um = ttk.Label(
            tabela_frame, text=custo_aquisicao, font=("Helvetica", 12, "bold")
        )
        valor_um.grid(row=0, column=1, padx=5, pady=5, sticky="e")

        custo_ajustes = self.peca.status.custo_total
        valor_dois = ttk.Label(
            tabela_frame, text=custo_ajustes, font=("Helvetica", 12, "bold")
        )
        valor_dois.grid(row=1, column=1, padx=5, pady=5, sticky="e")

        taxa_lucro = self.controlador.controlador_calculadora.pegar_custo(
            "Taxa de Lucro"
        )
        valor_tres = ttk.Label(
            tabela_frame, text=taxa_lucro, font=("Helvetica", 12, "bold")
        )
        valor_tres.grid(row=2, column=1, padx=5, pady=5, sticky="e")

        valor_sugerido = custo_aquisicao + custo_ajustes + taxa_lucro
        valor_quatro = ttk.Label(
            tabela_frame, text=valor_sugerido, font=("Helvetica", 12, "bold")
        )
        valor_quatro.grid(row=3, column=1, padx=5, pady=5, sticky="e")

        # 3. Botões
        self.botao_calcular = ttk.Button(
            self.frame_principal,
            text="Colocar à venda",
            width=50,
            command=self.checar_valores,
        )
        self.botao_calcular.pack(padx=10, pady=10, expand=False)

        self.botao_enviar_venda = ttk.Button(
            self.frame_principal,
            text="Voltar",
            width=50,
            command=self.controladorPeca.tela_rest_p_venda,
        )
        self.botao_enviar_venda.pack(padx=10, pady=10)

    def checar_valores(self):
        try:
            titulo = self.entry_titulo.get()
            preco = self.entry_preco.get()
            if float(preco) and titulo:
                self.prosseguir()
        except ValueError:
            self.apresentar_msg_erro("Por favor informe um título e um preço válido.")

    def prosseguir(self):

        self.peca.titulo = self.entry_titulo.get()
        self.peca.preco = self.entry_preco.get()
        if self.path_imagem:
            self.peca.imagem = self.path_imagem

        dados_update = {
            "id": self.peca.id,
            "custo_aquisicao": self.peca.custo_aquisicao,
            "descricao": self.peca.descricao,
            "status": "a_venda",
            "imagem": self.peca.imagem,
            "titulo": self.peca.titulo,
            "preco": self.peca.preco,
        }

        # Update DAO,*
        self.controladorPeca.update(dados_update)
        self.controladorPeca.tela_menu()

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

    def apresentar_msg_erro(self, msg):
        messagebox.showinfo("Erro", msg)

    def load_and_display_image(self, file_path):
        try:
            image = Image.open(file_path)
            image = image.resize((150, 150), Image.ANTIALIAS)
            image_tk = ImageTk.PhotoImage(image)
            self.image_label.config(image=image_tk)
            self.image_label.image = image_tk
        except Exception as e:
            messagebox.showinfo("Erro", f"Erro ao carregar imagem: {e}")

    def frame(self):
        self.frame_principal = ttk.Frame(
            self, width=770, height=608, padding=20, style="light"
        )

        self.frame_principal.grid(row=1, column=0, padx=10, pady=32)

        self.titulo = ttk.Label(
            self.frame_principal,
            text=self.peca.id,
            style="inverse-light",
            font=("Helvetica", 14, "bold"),
        )
        self.titulo.pack(padx=10, pady=10)
