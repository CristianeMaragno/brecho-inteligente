from persistencia.dao import DAO
from entidade.status_tipos.statusAVenda import StatusAVenda
import json


class AVendaDAO(DAO):
    def __init__(self):
        super().__init__()
        super().connect()
        super().create_table('status_avenda',
                             {'vendido': 'INTEGER', 'id': 'TEXT PRIMARY KEY'})

    def add(self, st: StatusAVenda):
        if not self.exists(st.id):
            if st.vendido:
                vendido = 1
            else:
                vendido = 0
            data = [(vendido, st.id)]
            super().insert_data('status_avenda', data)
        else:
            print(f"O id '{st.id}' já existe na tabela status_avenda. A inserção foi ignorada.")

    def remove(self, codigo: str):
        super().delete('status_avenda', 'id', codigo)

    def get_by_id(self, codigo: str):
        query = f"SELECT * FROM status_avenda WHERE id = '{codigo}'"
        result = self.execute(query)
        if result:
            vendido = json.loads(result[0][0])
            if vendido:
                vendido = True
            else:
                vendido = False
            return StatusAVenda(vendido, result[0][1])
        else:
            return None

    def update(self, st: StatusAVenda):
        if st.vendido:
            vendido = 1
        else:
            vendido = 0
        query = f"UPDATE status_avenda SET vendido = '{vendido}' WHERE id = '{st.id}'"
        self.execute(query)

    def execute(self, custom_query):
        return super().execute_query(custom_query)

    def exists(self, status_id: str) -> bool:
        query = f"SELECT COUNT(*) FROM status_avenda WHERE id = '{status_id}'"
        result = super().execute_query(query)
        return result[0][0] > 0
