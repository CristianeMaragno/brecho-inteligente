from limite.tela_peca import (
    MenuPeca,
    RegistrarPeca,
    ApagarPeca,
    UpdatePeca,
    MostrarPeca,
)
from limite.tela_rest_para_venda import (
    TelaRestauracaoParaVenda1,
    TelaRestauracaoParaVenda2,
)
from limite.tela_busca import TelaBusca
from entidade.status_tipos.statusAVenda import StatusAVenda
from entidade.peca import Peca
from entidade.categoria import Categoria
from entidade.status_tipos.statusRestauracao import StatusRestauracao
from persistencia.peca_dao import PecaDAO as pdao
from persistencia.categorias_dao import CategoriasDAO as ctdao
from persistencia.restauracao_dao import RestauracaoDAO as strdao
from persistencia.avenda_dao import AVendaDAO as savdao
import tkinter as tk


import hashlib
import random


class ControladorPeca:
    def __init__(self, root, controlador, controladorUsuarios):
        self.ctdao = ctdao()
        self.savdao = savdao()
        self.strdao = strdao(self.ctdao)
        self.pdao = pdao(self.strdao, self.savdao)
        self.root = root
        self.controlador = controlador
        self.controlador_usuarios = controladorUsuarios
        self.tela_atual = None

        self.criar_categorias()

    # Métodos auxiliares
    @staticmethod
    def generate_short_hash(length=8):
        random.seed()
        seed = random.randint(0, 1000000)
        hash_object = hashlib.sha256(str(seed).encode())
        hex_hash = hash_object.hexdigest()
        return hex_hash[:length]

    def criar_categorias(self):
        criar = self.ctdao.get_by_id("0")
        if criar:
            return

        categorias = [
            Categoria("0", "Lavar", 0.0),
            Categoria("1", "Passar", 0.0),
            Categoria("2", "Reparar danos", 0.0),
            Categoria("3", "Restaurar detalhes", 0.0),
            Categoria("4", "Remover manchas", 0.0),
            Categoria("5", "Tingir", 0.0),
            Categoria("6", "Customizar", 0.0),
            Categoria("7", "Nenhum ajuste", 0.0),
        ]

        for ct in categorias:
            self.ctdao.add(ct)

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

        self.tela_atual = MenuPeca(
            self.root, self.controlador, self.controlador_usuarios, self
        )
        self.tela_atual.pack(fill=tk.BOTH, expand=True)

    def tela_registrar(self):
        if self.tela_atual:
            self.tela_atual.pack_forget()

        self.tela_atual = RegistrarPeca(
            self.root,
            self.controlador,
            self.controlador_usuarios,
            self,
            self.ctdao.get_all(),
        )
        self.tela_atual.pack(fill=tk.BOTH, expand=True)

    def tela_update(self):
        if self.tela_atual:
            self.tela_atual.pack_forget()

        self.tela_atual = UpdatePeca(
            self.root,
            self.controlador,
            self.controlador_usuarios,
            self,
            self.ctdao.get_all(),
        )
        self.tela_atual.pack(fill=tk.BOTH, expand=True)

    def tela_mostrar(self):
        if self.tela_atual:
            self.tela_atual.pack_forget()

        self.tela_atual = MostrarPeca(
            self.root,
            self.controlador,
            self.controlador_usuarios,
            self,
            self.pdao.get_all(),
        )
        self.tela_atual.pack(fill=tk.BOTH, expand=True)

    def tela_busca(self):
        if self.tela_atual:
            self.tela_atual.pack_forget()

        self.tela_atual = TelaBusca(
            self.root,
            self.controlador,
            self.controlador_usuarios,
            self,
            self.pdao.get_all())
        self.tela_atual.pack(fill=tk.BOTH, expand=True)

    def tela_apagar(self):
        if self.tela_atual:
            self.tela_atual.pack_forget()

        self.tela_atual = ApagarPeca(
            self.root, self.controlador, self.controlador_usuarios, self
        )
        self.tela_atual.pack(fill=tk.BOTH, expand=True)

    def tela_rest_p_venda(self, dados=None):
        if self.tela_atual:
            self.tela_atual.pack_forget()

        if dados:
            self.tela_atual = TelaRestauracaoParaVenda2(
                self.root,
                self.controlador,
                self.controlador_usuarios,
                self,
                dados,
            )
            self.tela_atual.pack(fill=tk.BOTH, expand=True)
        else:
            self.tela_atual = TelaRestauracaoParaVenda1(
                self.root,
                self.controlador,
                self.controlador_usuarios,
                self,
            )
            self.tela_atual.pack(fill=tk.BOTH, expand=True)

    # Métodos de tratamento de dados
    def registrar(self, dados):
        if dados:
            id = self.generate_short_hash()

            categorias = []
            for ct_id in dados["tipos_restauração"]:
                categoria = self.ctdao.get_by_id(str(ct_id))
                categorias.append(categoria)
            status = StatusRestauracao(categorias)
            nova_peca = Peca(
                id,
                dados["descrição"],
                status,
                float(dados["custo_aquisição"]),
                dados["imagem"],
            )

            print("Peça criada com sucesso!")
            print(f"Id: {nova_peca.id}")

            self.pdao.add(peca=nova_peca)
        else:
            print("Erro na criação da peça!")

    def update(self, dados):
        status = None
        if dados["status"] == "em_restauracao":
            categorias = []
            if dados["ajustes"]:
                for ct_id in dados["ajustes"]:
                    categoria = self.ctdao.get_by_id(str(ct_id))
                    categorias.append(categoria)
                status = StatusRestauracao(categorias)
        else:
            status = StatusAVenda()

        update_peca = Peca(
            dados["id"],
            dados["descricao"],
            status,
            dados["custo_aquisicao"],
            dados["titulo"],
            dados["imagem"],
            dados["preco"],
        )

        self.pdao.update(update_peca)

    def mostrar(self, lista_dao):
        pass

    def apagar(self, codigo):
        if codigo:
            self.pdao.remove(codigo)
            print("Peça apagada com sucesso!")

    def voltar(self):
        if self.tela_atual:
            self.tela_atual.pack_forget()
        self.controlador.tela_menu()
