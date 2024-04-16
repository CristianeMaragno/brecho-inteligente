import tkinter as tk
from limite.tela import Tela
from entidade.categoria import tipoRestauracao as tr


class TelaPeca(Tela):
    def __init__(self, master):
        super().__init__(master)
        self.master.title("Cadastro de peças")

    def pegar_dados(self):
        # Campos de texto
        entry_nome = super().gerar_input("Título:")
        # Botão de escolher imagem
        imagem = super().gerar_botao(texto="Escolher imagem",
                                     command=super().abrir_imagem)
        # Imprimir a imagem
        if imagem:
            super().exibir_imagem(imagem)

        # Para selecionar o Status
        status_frame = tk.Frame(self.master)
        status_frame.pack()
        status_label = tk.Label(status_frame, text="Status")
        status_label.pack(side=tk.LEFT)
        opcoes = ["Em restauração", "À venda"]
        status = super().gerar_radiobutton(opcoes, status_frame)

        # Criando um dicionário com os resultados
        dados = {"titulo": entry_nome.get(),
                 "imagem": imagem,
                 "status": status.get()}

        # Botão para concluir
        super().gerar_botao(texto="Continuar",
                            command=lambda: self.tratar_dados(dados))

    def tratar_dados(self, dados):
        # Renderizando atributos de acordo com o tipo de Status
        if dados["status"] == "Em restauração":
            # Selecionando o tipo de restauração
            tipo_frame = tk.Frame(self.master)
            tipo_frame.pack()
            tipo_label = tk.Label(status_frame, text="Selecione as restaurações\n necessárias:")
            tipo_label.pack(side=tk.LEFT)
            # Os tipos foram importados
            opcoes = tr.tipos
            tipos_selecionados = super().gerar_checkbox(opcoes, tipo_frame)
        if dados["status"] == "À venda":
            preco_entry = super().gerar_input("Preço:")

    def iniciar(self):
        super().gerar_texto_packed("Cadastro de peça")
        self.pegar_dados()


def main():
    root = tk.Tk()
    root.geometry("400x500")

    tela = TelaPeca(root)

    tela.iniciar()

    root.mainloop()


if __name__ == "__main__":
    main()
