import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap import Style
from limite.tela_padrao import TelaPadrao
from PIL import Image, ImageTk


class TelaCatalogo(TelaPadrao):
    def __init__(self, master, controlador, controladorUsuario, controladorPecas):
        self.controlador_pecas = controladorPecas
        self.pecas_a_venda = []
        super().__init__(master, controlador, controladorUsuario)

    def controlador(self):
        return self.__controlador

    def conteudo(self):
        self.frame()

        # Frame para conter os cards e a scrollbar
        self.content_frame = ttk.Frame(self.frame_principal, style="light", padding=10)
        self.content_frame.pack(padx=10, pady=10, expand=True)

        # Pegando as peças à venda
        pecas = self.controlador_pecas.pdao.get_all()
        for peca in pecas:
            if peca.status.__str__() == "À venda":
                self.pecas_a_venda.append(peca)

        if self.pecas_a_venda:
            # Adiciona um canvas para os cards
            self.canvas = tk.Canvas(
                self.content_frame,
                background=self.style.colors.primary,
                width=830,
                height=750,
            )
            self.canvas.pack(side="left", fill="both", expand=True)

            # Adiciona uma scrollbar vertical
            self.scrollbar = ttk.Scrollbar(
                self.content_frame, orient="vertical", command=self.canvas.yview
            )
            self.scrollbar.pack(side="right", fill="y")

            # Configura o canvas com a scrollbar
            self.canvas.configure(yscrollcommand=self.scrollbar.set)
            self.canvas.bind(
                "<Configure>",
                lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")),
            )

            # Frame para os cards
            self.cards_frame = ttk.Frame(self.canvas, style="light.TFrame", padding=10)
            self.canvas.create_window((0, 0), window=self.cards_frame, anchor="nw")

            row, col = 0, 0
            max_cols = 4  # Número máximo de colunas antes de pular para a próxima linha
            for peca in self.pecas_a_venda:
                self.criar_card(self.cards_frame, peca, row, col)
                col += 1
                if col >= max_cols:
                    col = 0
                    row += 1
        else:
            self.nao_ha_pecas()

    def criar_card(self, parent, peca, row, col):

        card_frame = ttk.Frame(
            parent, style="primary.TFrame", padding=10, width=200, height=300
        )
        card_frame.grid(row=row, column=col, padx=10, pady=10)

        # Adiciona imagem de exemplo
        imagem = ttk.Label(card_frame, text="[Imagem]", style="inverse.light.TLabel")
        imagem.pack(side="top", padx=5, pady=5, anchor="n")
        self.load_and_display_image(peca.imagem, imagem)

        # Adiciona frame para o texto
        text_frame = ttk.Frame(card_frame, style="primary.TFrame")
        text_frame.pack(side="top", fill="x", expand=True)

        # Adiciona o título, código e descrição
        titulo_label = ttk.Label(
            text_frame,
            text=peca.titulo,
            style="inverse-primary",
            font=("Helvetica", 12, "bold"),
        )
        titulo_label.pack(anchor="w")

        codigo_label = ttk.Label(
            text_frame,
            text=peca.id,
            style="inverse-primary",
            font=("Helvetica", 10, "bold"),
        )
        codigo_label.pack(anchor="w")

        descricao_label = ttk.Label(
            text_frame,
            text=peca.descricao,
            style="inverse-primary",
        )
        descricao_label.pack(anchor="w")

    def load_and_display_image(self, file_path, imagem_label):
        try:
            image = Image.open(file_path)
            image = image.resize((150, 150), Image.LANCZOS)
            image_tk = ImageTk.PhotoImage(image)
            imagem_label.config(image=image_tk)
            imagem_label.image = image_tk
        except Exception as e:
            messagebox.showinfo("Erro", f"Erro ao carregar imagem: {e}")

    def frame(self):
        self.frame_principal = ttk.Frame(
            self, width=900, height=608, padding=20, style="light"
        )

        self.frame_principal.grid(row=1, column=0, padx=20, pady=32, sticky="n")

        self.titulo = ttk.Label(
            self.frame_principal,
            text="Catálogo",
            style="inverse-light",
            font=("Helvetica", 14, "bold"),
        )
        self.titulo.pack(padx=10, pady=10)

    def nao_ha_pecas(self):
        label = ttk.Label(
            self.frame_principal,
            text="Não há peças para colocar à venda.",
            style="inverse-light",
            font=("Helvetica", 15, "bold"),
        )
        label.pack(padx=10, pady=10)
