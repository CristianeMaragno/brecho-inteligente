from limite.tela_padrao import TelaPadrao
import ttkbootstrap as ttk
import tkinter as tk

from tkinter import VERTICAL, Scrollbar


class TelaEditCalculadora(TelaPadrao):
    def __init__(self, master, controlador, controladorCalculadora, controladorUsuario):
        self.__controlador_calculadora = controladorCalculadora
        super().__init__(master, controlador, controladorUsuario)

    def conteudo(self):
        frame_container = ttk.Frame(self, padding=10, style="light")
        frame_container.grid(row=1, column=0)

        self.label = ttk.Label(
            frame_container,
            text="CALCULADORA",
            style="inverse-light",
            font=("Helvetica", 12, "bold"),
        )
        self.label.grid(row=0, column=0, pady=10)

        canvas = tk.Canvas(frame_container)
        canvas.grid(row=1, column=0)

        scrollbar = Scrollbar(frame_container, orient=VERTICAL, command=canvas.yview)
        scrollbar.grid(row=1, column=1, sticky="ns")
        canvas.config(yscrollcommand=scrollbar.set)

        frame = ttk.Frame(canvas, padding=(80, 20), style="light")
        canvas.create_window((0, 0), window=frame, anchor="center")

        categorias = [
            "Lavar",
            "Passar",
            "Reparar danos",
            "Restaurar detalhes",
            "Remover manchas",
            "Tingir",
            "Customizar",
            "Taxa de Lucro",
        ]

        self.campos_custo = {}

        for i, categoria in enumerate(categorias):
            custo_atual = float(self.__controlador_calculadora.pegar_custo(categoria))

            if custo_atual is None:
                continue
            
            frame_categoria = ttk.Frame(frame, style="light")
            frame_categoria.grid(row=i + 1, column=0, sticky="ew", padx=10, pady=5)

            label_categoria = ttk.Label(
                frame_categoria, text=categoria, style="inverse-light"
            )
            label_categoria.pack(padx=10, pady=5, side="left")

            campo_custo = ttk.Entry(frame_categoria, width=10)
            campo_custo.insert(0, custo_atual)
            campo_custo.pack(padx=10, pady=5, side="right")
            self.campos_custo[categoria] = campo_custo

        canvas.update_idletasks()  # Atualiza o tamanho do canvas
        canvas.config(scrollregion=canvas.bbox("all"))

        self.mensagem_erro_label = ttk.Label(
            frame_container, style="light.inverse.TLabel", foreground="red"
        )
        self.mensagem_erro_label.grid(row=2, column=0, pady=10)

        botao_salvar = ttk.Button(
            frame_container, text="Salvar", command=self.salvar_custos
        )
        botao_salvar.grid(row=3, column=0, pady=10)

        botao_voltar = ttk.Button(
            frame_container, text="Voltar", command=self.voltar
        )
        botao_voltar.grid(row=4, column=0, pady=10)

    def salvar_custos(self):
        self.mensagens_erro = []

        for categoria, campo_custo in self.campos_custo.items():
            valor = campo_custo.get()

            if valor == "":
                continue

            try:
                valor_float = float(valor)
            except ValueError:
                self.adicionar_mensagem_erro(categoria, "Valor inserido não é um número válido.")
                continue

            if valor_float < 0:
                self.adicionar_mensagem_erro(categoria, "Valor inserido não pode ser negativo.")

            else:  # Salvar o custo apenas se o valor for um número válido
                self.__controlador_calculadora.atualizar_custo(categoria, float(valor))

        if self.mensagens_erro:
            mensagem_erro_str = "\n".join(self.mensagens_erro)
            self.exibir_mensagem_erro("Salvo, exceto:\n" + mensagem_erro_str)
        else:
            self.exibir_mensagem_erro("Salvo")

    def exibir_mensagem_erro(self, mensagem):
        if mensagem == "Salvo":
            self.mensagem_erro_label.config(text=mensagem, foreground="green")
        else:
            self.mensagem_erro_label.config(text=mensagem, foreground="red")
    
    def adicionar_mensagem_erro(self, categoria, mensagem):
        self.mensagens_erro.append(
                    f"{categoria}: {mensagem}")

    def voltar(self):
        self.controlador.tela_menu()