import tkinter as tk
from limite.tela_peca import MenuPeca, RegistrarPeca, ApagarPeca, UpdatePeca, MostrarPeca
from entidade.peca import Peca
from entidade.status_tipos.statusRestauracao import StatusRestauracao
from persistencia.peca_dao import PecaDAO as pdao

import hashlib
import random


class ControladorPeca:
    def __init__(self, root):
        self.pdao = pdao()
        self.root = root
        self.tela_atual = None

    # Métodos auxiliares
    def generate_short_hash(self, length=8):
        random.seed()
        seed = random.randint(0, 1000000)
        hash_object = hashlib.sha256(str(seed).encode())
        hex_hash = hash_object.hexdigest()
        return hex_hash[:length]

    def get_peca(self, codigo: str):

        if codigo:
            resultado = self.pdao.get_by_id(codigo)
            if resultado:
                return resultado
            else:
                return None
        else:
            return None

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

        self.tela_atual = MostrarPeca(self.root, self, self.pdao.get_all())
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
            nova_peca = Peca(id, dados["descrição"], status, float(dados['custo_aquisição']), dados['imagem'])

            print("Peça criada com sucesso!")
            print(f"Id: {nova_peca.id}")

            self.pdao.add(peca=nova_peca)
        else:
            print('Erro na criação da peça!')

    def update(self, dados):
        status = StatusRestauracao(dados["tipos_restauração"])
        update_peca = Peca(dados['id'], dados["descrição"], status, float(dados['custo_aquisição']), dados['imagem'])

        self.pdao.update(update_peca.id, update_peca)
        print('Update feito com sucesso!')

    def mostrar(self, lista_dao):
       pass

    def apagar(self, codigo):
        if codigo:
            self.pdao.remove(codigo)
            print('Peça apagada com sucesso!')