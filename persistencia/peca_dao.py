from persistencia.dao import DAO
from entidade.peca import Peca

class PecaDAO(DAO):
    def __init__(self, strdao):
        super().__init__()
        self.conn = None
        super().connect()
        super().create_table('pecas', {'id': 'TEXT PRIMARY KEY', 'descricao': 'TEXT', 'status_id': 'TEXT',
                                        'custo_aquisicao': 'REAL', 'titulo': 'TEXT', 'imagem': 'TEXT', 'preco': 'REAL', })
        self.strdao = strdao

    def add(self, peca: Peca):
        data = [(peca.id, peca.descricao, peca.status.id, peca.custo_aquisicao, peca.titulo, peca.imagem, peca.preco)]
        with self.conn:
            self.strdao.add(peca.status)
            super().insert_data('pecas', data)

    def remove(self, codigo: str):
        with self.conn:
            peca = self.get_by_id(codigo)
            if peca and peca.status:
                self.strdao.remove(peca.status.id)
            super().delete('pecas', 'id', codigo)

    def get_all(self):
        rows = super().fetch_data('pecas')
        pecas = []
        for row in rows:
            status = self.strdao.get_by_id(row[2])
            pecas.append(Peca(row[0], row[1], status, row[3], row[4], row[5], row[6]))
        return pecas

    def get_by_id(self, codigo: str):
        result = self.execute(f"SELECT * FROM pecas WHERE id = '{codigo}'")
        if result:
            peca_data = result[0]
            status = self.strdao.get_by_id(peca_data[2])
            return Peca(*peca_data[:2], status, *peca_data[3:])
        return None

    def update(self, codigo: str, peca: Peca):
        with self.conn:
            old_peca = self.get_by_id(codigo)
            if old_peca and old_peca.status:
                self.strdao.remove(old_peca.id)
            self.strdao.add(peca.status)
            query = (f"UPDATE pecas SET descricao = '{peca.descricao}', imagem = '{peca.imagem}', " 
                     f"status_id = '{peca.status.id}', custo_aquisicao = {peca.custo_aquisicao}, " 
                     f"titulo = '{peca.titulo}', preco = '{peca.preco}' " 
                     f"WHERE id = '{codigo}'")
            self.execute(query)

    def execute(self, custom_query):
        return super().execute_query(custom_query)
