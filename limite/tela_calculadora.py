from limite.tela_padrao import TelaPadrao
import ttkbootstrap as ttk
import tkinter as tk

from tkinter import VERTICAL

class TelaEditCalculadora(TelaPadrao):
    def __init__(self, master, controlador, controladorCalculadora, controladorUsuario):
        self.__controlador_calculadora = controladorCalculadora
        super().__init__(master, controlador, controladorUsuario)

    def conteudo(self):
        frame_container = ttk.Frame(self)
        frame_container.pack(fill="both", expand=True)

        canvas = tk.Canvas(frame_container)
        canvas.pack(side= "left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(frame_container, orient=VERTICAL, command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        canvas.configure(yscrollcommand=scrollbar.set)

        content_frame = ttk.Frame(canvas)

        canvas.create_window((0, 0), window=content_frame, anchor="nw")

        content_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        frame = ttk.Frame(content_frame, width=770, height=608, padding=20, style='light')
        frame.pack(fill="none", expand=False, pady=32)

        self.label = ttk.Label(frame, text="CALCULADORA", style="inverse-light", font=("Helvetica", 12, "bold"))
        self.label.pack(pady=32)

        categorias = ['Lavar', 'Passar', 'Reparo de Falhas', 'Restauração de Detalhes', 'Remoção de Manchas',
                      'Tingimento', 'Customizacao', 'TaxaDeLucro']

        self.campos_custo = {}

        for categoria in categorias:
            frame_categoria = ttk.Frame(frame, style='light')
            frame_categoria.pack(fill="x", padx=10, pady=5)

            label_categoria = ttk.Label(frame_categoria, text=categoria, style="inverse-light")
            label_categoria.pack(side="left", padx=10, pady=5)

            custo_atual = float(self.__controlador_calculadora.pegar_custo(categoria))

            campo_custo = ttk.Entry(frame_categoria, width=10)
            campo_custo.insert(0, custo_atual)
            campo_custo.pack(side="right")
            self.campos_custo[categoria] = campo_custo

        self.mensagem_erro_label = ttk.Label(frame, style="light.inverse.TLabel", foreground="red")
        self.mensagem_erro_label.pack()

        botao_salvar = ttk.Button(frame, text="Salvar", command=self.salvar_custos)
        botao_salvar.pack(pady=10)

    def salvar_custos(self):
        mensagens_erro = []

        for categoria, campo_custo in self.campos_custo.items():
            valor = campo_custo.get()

            if valor == "":
                continue

            try:
                valor_float = float(valor)
            except ValueError:
                mensagens_erro.append(f"{categoria}: Valor inserido não é um número válido.")
                continue

            if valor_float < 0:
                mensagens_erro.append(f"{categoria}: Valor inserido não pode ser negativo.")
                continue

            else:  # Salvar o custo apenas se o valor for um número válido
                self.__controlador_calculadora.atualizar_custo(categoria, float(valor))

        if mensagens_erro:
            mensagem_erro_str = "\n".join(mensagens_erro)
            self.exibir_mensagem_erro('salvo, exceto:\n' + mensagem_erro_str)
        else:
            self.exibir_mensagem_erro('Salvo')

    def exibir_mensagem_erro(self, mensagem):
        if mensagem == 'Salvo':
            self.mensagem_erro_label.config(text=mensagem, foreground="green")
        else:
            self.mensagem_erro_label.config(text=mensagem)
