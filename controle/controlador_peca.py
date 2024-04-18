import tkinter as tk
from limite.tela_peca import TelaPeca
from entidade.peca import Peca
from entidade.statusRestauracao import StatusRestauracao
from entidade.statusAVenda import StatusAVenda
import hashlib
import random
import string

class ControladorPeca:
    def __init__(self, root):
        self.tela = TelaPeca(root)

    def generate_short_hash(self, length=8):
        random.seed()
        seed = random.randint(0, 1000000)
        hash_object = hashlib.sha256(str(seed).encode())
        hex_hash = hash_object.hexdigest()
        return hex_hash[:length]

    def menu_peca(self):
        lista_opcoes = {1: self.criar_peca, 2: self.update_peca,
                        3: self.mostrar_peca, 4: self.deletar_peca}

        while True:
            opcao_escolhida = self.tela.menu()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def criar_peca(self):

        dados = self.tela.iniciar()

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

    def update_peca(self, peca: Peca):
        pass

    def mostrar_peca(self, peca: Peca):
        pass

    def deletar_peca(self, peca: Peca):
        pass


def main():
    root = tk.Tk()
    root.geometry("550x550")

    controlador = ControladorPeca(root)

    controlador.menu_peca()

    root.mainloop()

if __name__ == "__main__":

    main()