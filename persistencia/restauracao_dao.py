from persistencia.dao import DAO
from entidade.status_tipos.statusRestauracao import StatusRestauracao
import json


class RestauracaoDAO(DAO):
    def __init__(self, ctdao):
        super().__init__()
        self.conn = None
        super().connect()
        super().create_table('status_restauracao',
                             {'categorias': 'TEXT', 'id': 'TEXT PRIMARY KEY'})
        self.ctdao = ctdao

    def add(self, st: StatusRestauracao):
        if not self.exists(st.id):
            categorias_lista = []
            for categoria in st.categorias:
                categorias_lista.append(categoria.id)
            categorias_json = json.dumps(categorias_lista)
            data = [(categorias_json, st.id)]
            super().insert_data('status_restauracao', data)
        else:
            print(f"O id '{st.id}' já existe na tabela status_restauracao. A inserção foi ignorada.")

    def remove(self, codigo: str):
        super().delete('status_restauracao', 'id', codigo)


    def get_all(self):
        rows = super().fetch_data('status_restauracao')
        status = []
        for row in rows:
            categorias_lista = json.loads(row[1])
            categorias = []
            for categoria_id in categorias_lista:
                categoria = self.ctdao.get_by_id(categoria_id)
                categorias.append(categoria)
            st = StatusRestauracao(categorias, row[0])
            status.append(st)
        return status

    def get_by_id(self, codigo: str):
        query = f"SELECT * FROM status_restauracao WHERE id = '{codigo}'"
        result = self.execute(query)
        if result:
            categorias_lista = json.loads(result[0][0])
            categorias = []
            for categoria_id in categorias_lista:
                categoria = self.ctdao.get_by_id(categoria_id)
                categorias.append(categoria)
            return StatusRestauracao(categorias, result[0][1])
        else:
            return None

    def update(self, st: StatusRestauracao):
        with self.conn:
            categorias_lista = []
            for categoria in st.categorias:
                categorias_lista.append(categoria.id)
            categorias_json = json.dumps(categorias_lista)
            query = f"UPDATE status_restauracao SET categorias = '{categorias_json}' WHERE id = '{st.id}'"
            self.execute(query)

    def execute(self, custom_query):
        with self.conn:
            return super().execute_query(custom_query)

    def exists(self, status_id: str) -> bool:
        query = f"SELECT COUNT(*) FROM status_restauracao WHERE id = '{status_id}'"
        result = super().execute_query(query)
        return result[0][0] > 0
