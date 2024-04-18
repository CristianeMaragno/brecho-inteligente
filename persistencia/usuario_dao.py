from persistencia.dao import DAO
from entidade.usuario import Usuario


class UsuarioDAO(DAO):
    def __init__(self):
        super().__init__()
        super().connect()
        super().create_table('users', {'id': 'INTEGER PRIMARY KEY', 'nome': 'TEXT', 'email': 'TEXT', 'senha': 'TEXT', 'papel': 'INTEGER'})
    def add(self, usuario: Usuario):
        data = [
            (usuario.identificador, usuario.nome, usuario.email, usuario.senha, usuario.papel),
        ]

        super().insert_data('users', data)

    def remove(self, codigo: int):
        return 0

    def get_all(self):
        rows = super().fetch_data('users')
        response = []
        for row in rows:
            usuario = Usuario(row[0], row[1], row[2], row[3], row[4])
            response.append(usuario)

        return response

    def get_by_id(self, codigo):
        query = "SELECT * FROM users WHERE id = %s" % (codigo)
        usuario = self.execute(query)
        if usuario:
            return Usuario(usuario[0], usuario[1], usuario[2], usuario[3], usuario[4])
        else:
            return None

    def update(self, codigo, usuario: Usuario):
        return 0

    def execute(self, custom_query):
        return super().execute_query_one_value(custom_query)