import tkinter as tk
from limite.tela_peca import MenuPeca, RegistrarPeca, ApagarPeca, UpdatePeca, MostrarPeca
from entidade.peca import Peca
from entidade.statusRestauracao import StatusRestauracao
from entidade.statusAVenda import StatusAVenda
import hashlib
import random
import string

class ControladorPeca:
    def __init__(self, root):
        self.root = root
        self.tela_atual = None

    # Métodos auxiliares
    def generate_short_hash(self, length=8):
        random.seed()
        seed = random.randint(0, 1000000)
        hash_object = hashlib.sha256(str(seed).encode())
        hex_hash = hash_object.hexdigest()
        return hex_hash[:length]

    # Métodos de navegação
    def tela_menu(self):
        if self.tela_atual:
            self.tela_atual.pack_forget()

        self.tela_atual = MenuPeca(self.root, self)
        self.tela_atual.pack()

    def tela_registrar(self):
        if self.tela_atual:
            self.tela_atual.pack_forget()

        self.tela_atual = RegistrarPeca(self.root, self)
        self.tela_atual.pack()

    def tela_update(self):
        if self.tela_atual:
            self.tela_atual.pack_forget()

        self.tela_atual = UpdatePeca(self.root, self)
        self.tela_atual.pack()

    def tela_mostrar(self):
        if self.tela_atual:
            self.tela_atual.pack_forget()

        self.tela_atual = MostrarPeca(self.root, self)
        self.tela_atual.pack()

    def tela_apagar(self):
        if self.tela_atual:
            self.tela_atual.pack_forget()

        self.tela_atual = ApagarPeca(self.root, self)
        self.tela_atual.pack()

    # Métodos de tratamento de dados
    def registrar(self, dados):
        if dados:
            id = self.generate_short_hash()

            status = StatusRestauracao(dados["tipos_restauração"])
            nova_peca = Peca(id, dados["descrição"], status, dados['imagem'])

            print("Peça criada com sucesso!")
            print(f"Informações:\nId: {nova_peca.id}\n"
                  f"Descrição: {nova_peca.descricao}\nImagem: {nova_peca.imagem}\n"
                  f"Status: {nova_peca.status.__str__()}\n"
                  f"Tipos restauração: {nova_peca.status.categorias}")
        else:
            print('Erro na criação da peça!')

    def update(self, peca: Peca):
        pass

    def mostrar(self, peca: Peca):
        pass

    def apagar(self, peca: Peca):
        pass


def main():
    root = tk.Tk()
    root.geometry("500x500")

    controller = ControladorPeca(root)
    controller.tela_menu()

    root.mainloop()

if __name__ == "__main__":

    main()