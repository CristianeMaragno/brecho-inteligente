from limite.tela_calculadora import TelaEditCalculadora
from persistencia.calculadora_dao import CalculadoraDAO


class ControladorCalculadora:
    def __init__(self, master, controlador):
        self.master = master
        self.controlador = controlador
        self.cdao = CalculadoraDAO()

    def abre_tela_calculadora(self):
        return TelaEditCalculadora(self.master, self.controlador, self, self.controlador.controlador_usuarios)
    
    def obter_todas_categorias(self):
        return self.cdao.get_todas_categorias()
    
    def atualizar_custo(categoria, custo):
        pass