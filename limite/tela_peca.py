import tkinter as tk


class Tela:
    def __init__(self, master):
        self.master = master
        self.master.title("Cadastro")

    def gerar_label(self, texto):
        frame = tk.Frame(self.master)
        label = tk.Label(frame, text=texto)
        entry = tk.Entry(frame)
        frame.pack()
        label.pack(side=tk.LEFT)
        entry.pack(side=tk.LEFT)
        return entry

    def gerar_botao(self, texto, command=None):
        return tk.Button(self.master, text=texto, command=command)


class TelaPeca(Tela):
    def __init__(self, master):
        super().__init__(master)
        self.master.title("Cadastro de peça")

    def pegar_dados(self):
        entry_nome = super().gerar_label("Nome:")
        entry_email = super().gerar_label("Email:")
        botao_cadastrar = super().gerar_botao("Cadastrar", command=self.cadastrar)
        botao_cadastrar.pack()
        return entry_nome, entry_email

    def cadastrar(self):



def main():
    root = tk.Tk()
    root.geometry("400x200")

    tela = TelaPeca(root)

    infos = tela.pegar_dados()
    print(infos)

    root.mainloop()


if __name__ == "__main__":
    main()
