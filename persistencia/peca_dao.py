from persistencia.dao import DAO
from entidade.peca import Peca


class UsuarioDAO(DAO):
    def __init__(self):
        super().__init__()
        super().connect()
        super().create_table('pecas',
                             {'id': 'TEXT PRIMARY KEY', 'descricao': 'TEXT',
                            'status': 'TEXT', 'titulo': 'TEXT', 'preco': 'REAL'})
    def add(self, peca: Peca):
        data = [
            ('e66a8a97', 'Precisa-se de botão preto.', 'Em restauração', '', 20.0),
            ('09520032', 'Tamanho P', 'À Venda', '',15.5)
        ]
        super().insert_data('users', data)

    def remove(self, codigo: int):
        return 0

    def get_all(self):
        return super().fetch_data('users')

    def update(self, codigo, usuario: Usuario):
        return 0

    def execute(self, custom_query):
        super().execute_query(custom_query)