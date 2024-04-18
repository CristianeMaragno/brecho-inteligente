from persistencia.dao import DAO
from entidade.peca import Peca


class PecaDAO(DAO):
    def __init__(self):
        super().__init__()
        super().connect()
        super().create_table('pecas',
                             {'id': 'TEXT PRIMARY KEY', 'descricao': 'TEXT', 'status_id': 'TEXT',
                              'custo_aquisicao': 'REAL', 'titulo': 'TEXT', 'imagem': 'TEXT', 'preco': 'REAL', })
    def add(self, peca: Peca):
        data = [(peca.id, peca.descricao, peca.status.id, peca.custo_aquisicao, peca.titulo, peca.imagem, peca.preco)]
        super().insert_data('pecas', data)

    def remove(self, codigo: str):
        query = f"DELETE FROM pecas WHERE id = '{codigo}'"
        super().execute_query(query)

    def get_all(self):
        rows = super().fetch_data('pecas')

        pecas = []

        for row in rows:
            peca = Peca(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            pecas.append(peca)

        return pecas

    def get_by_id(self, codigo: str):
        query = f"SELECT * FROM pecas WHERE id = '{codigo}'"
        result = super().execute_query(query)
        if result:
            return Peca(*result[0])
        else:
            return None

    def update(self, codigo: str, peca: Peca):
        query = f"UPDATE pecas SET descricao = '{peca.descricao}', imagem = '{peca.imagem}', " \
                f"status_id = '{peca.status.id}', titulo = '{peca.titulo}', preco = {peca.preco} " \
                f"WHERE id = '{codigo}'"
        super().execute_query(query)

    def execute(self, custom_query):
        return super().execute_query(custom_query)