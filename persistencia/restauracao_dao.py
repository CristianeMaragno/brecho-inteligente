from persistencia.dao import DAO
from entidade.status_tipos.statusRestauracao import StatusRestauracao
import json


class RestauracaoDAO(DAO):
    def __init__(self):
        super().__init__()
        super().connect()
        super().create_table('status_restauracao',
                             {'categorias': 'TEXT', 'id': 'TEXT PRIMARY KEY'})

    def add(self, st: StatusRestauracao):
        if not self.exists(st.id):
            categorias_str = json.dumps(st.categorias)
            data = [(categorias_str, st.id)]
            super().insert_data('status_restauracao', data)
        else:
            print(f"O id '{st.id}' já existe na tabela status_restauracao. A inserção foi ignorada.")

    def remove(self, codigo: str):
        super().delete('status_restauracao', 'id', codigo)
        # query = f"DELETE FROM status_restauracao WHERE id = '{codigo}'"
        # super().execute_query(query)

    def get_all(self):
        rows = super().fetch_data('status_restauracao')
        status = []
        for row in rows:
            categorias = json.loads(row[1])
            st = StatusRestauracao(categorias, row[0])
            status.append(st)
        return status

    def get_by_id(self, codigo: str):
        query = f"SELECT * FROM status_restauracao WHERE id = '{codigo}'"
        result = self.execute(query)
        if result:
            categorias = json.loads(result[0][0])
            return StatusRestauracao(categorias, result[0][1])
        else:
            return None

    def update(self, codigo: str, st: StatusRestauracao):
        categorias_str = json.dumps(st.categorias)
        query = f"UPDATE status_restauracao SET categorias = '{categorias_str}' WHERE id = '{codigo}'"
        self.execute(query)

    def execute(self, custom_query):
        return super().execute_query(custom_query)

    def exists(self, status_id: str) -> bool:
        query = f"SELECT COUNT(*) FROM status_restauracao WHERE id = '{status_id}'"
        result = super().execute_query(query)
        return result[0][0] > 0
