from persistencia.dao import DAO
from entidade.usuario import Usuario


class UsuarioDAO(DAO):
    def __init__(self):
        super().__init__()
        super().connect()
        super().create_table('users', {'id': 'INTEGER PRIMARY KEY', 'email': 'TEXT', 'senha': 'TEXT', 'papel': 'INTEGER'})
    def add(self, usuario: Usuario):
        data = [
            (1, 'john_doe', 'john@example.com'),
            (2, 'jane_smith', 'jane@example.com')
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