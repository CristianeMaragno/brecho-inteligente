from persistencia.dao import DAO
from entidade.categoria import Categoria


class CategoriasDAO(DAO):
    def __init__(self):
        super().__init__()
        super().connect()
        super().create_table('categorias',
                             {'id': 'TEXT PRIMARY KEY', 'nome': 'TEXT', 'custo_padrao': 'INTEGER', 'feito': 'INTEGER'})

    def add(self, ct: Categoria):
        if not self.exists(ct.id):
            data = [(ct.id, ct.nome, ct.custo_padrao, ct.feito)]
            super().insert_data('categorias', data)
        else:
            print(f"O id '{ct.id}' já existe na tabela status_restauracao. A inserção foi ignorada.")

    def remove(self, codigo: str):
        super().delete('categorias', 'id', codigo)

    def get_all(self):
        rows = super().fetch_data('categorias')
        categorias = []
        for row in rows:
            ct = Categoria(row[0], row[1], row[2], row[3])
            categorias.append(ct)
        return categorias

    def get_by_id(self, codigo: str):
        query = f"SELECT * FROM categorias WHERE id = '{codigo}'"
        categoria = super().execute_query_one_value(query)
        if categoria:
            return Categoria(categoria[0], categoria[1], categoria[2], categoria[3])
        else:
            return None

    def update(self, codigo, ct: Categoria):
        data = {
            "nome": ct.nome,
            "custo_padrao": ct.custo_padrao,
            "feito": ct.feito,
        }
        condition = "id = " + str(codigo)
        super().update('categorias', data, condition)

    def execute(self, custom_query):
        return super().execute_query(custom_query)

    def exists(self, codigo: str) -> bool:
        query = f"SELECT COUNT(*) FROM categorias WHERE id = '{codigo}'"
        result = super().execute_query(query)
        return result[0][0] > 0
