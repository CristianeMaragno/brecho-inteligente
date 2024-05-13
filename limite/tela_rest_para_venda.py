from limite.tela_padrao import TelaPadrao
import ttkbootstrap as ttk
from tkinter import messagebox
import tkinter as tk
import re


class TelaRestauracaoParaVenda(TelaPadrao):
    def __init__(self, master, controlador, controladorUsuario, controladorPeca):
        self.controladorPeca = controladorPeca
        self.peca_selecionada = None
        super().__init__(master, controlador, controladorUsuario)

    def conteudo(self):
        self.frame()

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
            self.frame_principal,
            width=770,
            height=608,
            padding=20,
            style='light'
        )
        self.frame_direito.grid(row=1, column=1, padx=10, pady=10)

        frame_peca_info = ttk.Frame(self.frame_direito)
        frame_peca_info.pack(padx=10, pady=5)

        label_id = ttk.Label(frame_peca_info,
                             text='ID')
        label_id.grid(row=0, column=0, padx=10, pady=10)
        self.combobox = ttk.Combobox(frame_peca_info,
                                     bootstyle="primary",
                                     values=ids_das_pecas)
        self.combobox.grid(row=0, column=1, padx=10, pady=10)

        label_custo_aquisicao = ttk.Label(frame_peca_info, text='Custo aquisição')
        label_custo_aquisicao.grid(row=1, column=0, padx=10, pady=10)

        self.peca_selecionada = self.controladorPeca.pdao.get_by_id(ids_das_pecas[0])
        custo_aquisicao = f'R${self.peca_selecionada.custo_aquisicao}'
        label_valor_custo_aquisicao = ttk.Label(frame_peca_info, text=custo_aquisicao)
        label_valor_custo_aquisicao.grid(row=1, column=1, padx=10, pady=10)

        # Botão enviar para a venda
        self.botao_enviar_venda = ttk.Button(self.frame_direito,
                                             text="Voltar",
                                             width=30,
                                             command=self.controladorPeca.
                                             tela_menu)
        self.botao_enviar_venda.pack(padx=10, pady=5)

        # Botão de voltar
        self.botao_voltar = ttk.Button(self.frame_direito,
                                       text="Enviar para venda",
                                       width=30,
                                       command=self.controladorPeca.
                                       tela_menu)
        self.botao_voltar.pack(padx=10, pady=5)

    def criar_frame_esquerdo(self):
        self.frame_esquerdo = ttk.Frame(
            self.frame_principal,
            width=770,
            height=608,
            padding=20,
            style='light'
        )
        self.frame_esquerdo.grid(row=1, column=0, padx=10, pady=10)

        frame_tabela = ttk.Frame(self.frame_esquerdo)
        frame_tabela.pack(expand=False)

        # Definindo a estrutura da tabela

        # 1. Headers
        label_coluna_1 = ttk.Label(frame_tabela, text='AJUSTES', font=("Helvetica", 9, "bold"))
        label_coluna_2 = ttk.Label(frame_tabela, text='CUSTO PADRÃO', font=("Helvetica", 9, "bold"))
        label_coluna_3 = ttk.Label(frame_tabela, text='CUSTO MODIFICADO', font=("Helvetica", 9, "bold"))

        label_coluna_1.grid(row=0, column=0, padx=10, pady=10)
        label_coluna_2.grid(row=0, column=1, padx=10, pady=10)
        label_coluna_3.grid(row=0, column=2, padx=10, pady=10)

        # 2. Conteúdo
        categorias = self.peca_selecionada.status.categorias
        self.custo_entrys = []

        i = 1
        for categoria in categorias:
            label_categoria = ttk.Label(frame_tabela, text=categoria)
            label_categoria.grid(row=i, column=0, padx=10, pady=10)

            label_custo_padrao = ttk.Label(frame_tabela, text='0.0')
            label_custo_padrao.grid(row=i, column=1, padx=10, pady=10)

            entry_custo_padrao = ttk.Entry(frame_tabela, bootstyle="info")
            entry_custo_padrao.grid(row=i, column=2, padx=10, pady=10)
            self.custo_entrys.append([entry_custo_padrao, categoria])

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
        valor_total = 0
        for entry, categoria in self.custo_entrys:
            try:
                if len(entry.get()) == 0:
                    valor_total += 0
                else:
                    valor = float(entry.get())
                    if valor:
                        valor_total += valor
            except ValueError:
                messagebox.showinfo(
                    "Erro",
                    "Por favor informe um valor válido de custo."
                )
        self.apresentar_total(valor_total)

    def apresentar_total(self, valor_total):
        self.total_label.destroy()
        texto = f'TOTAL: R${valor_total}'
        self.total_label = ttk.Label(self.frame_esquerdo,
                          text=texto,
                          style="inverse-light",
                          font=("Helvetica", 11, "bold"))
        self.total_label.pack(padx=10, pady=10, expand=False)

    def frame(self):
        self.frame_principal = ttk.Frame(self,
                                width=770,
                                height=608,
                                padding=20,
                                style='light')

        self.frame_principal.pack(fill="none",
                         expand=False,
                         pady=32)

        self.titulo = ttk.Label(self.frame_principal,
                                 text="Restauração para venda",
                                 style="inverse-light",
                                 font=("Helvetica", 14, "bold"))
        self.titulo.grid(row=0, column=0, padx=10, pady=10)