from persistencia.dao import DAO
from entidade.status_tipos.statusReserva import StatusReserva
import json

class ReservaDAO(DAO):
    def __init__(self):
        super().__init__()
        super().connect()
        super().create_table('status_reserva',
                             {'id': 'TEXT PRIMARY KEY', 'nome': 'TEXT', 'telefone': 'TEXT', 'data': 'TEXT'})

    def add(self, st: StatusReserva):
        if not self.exists(st.id):
            data = [(st.id, st.nome, st.telefone, st.data)]
            super().insert_data('status_reserva', data)
        else:
            print(
                f"O id '{st.id}' já existe na tabela status_reserva. A inserção foi ignorada."
            )

    def remove(self, codigo: str):
        super().delete("status_reserva", "id", codigo)

    def get_by_id(self, codigo: str):
        query = f"SELECT * FROM status_reserva WHERE id = '{codigo}'"
        result = self.execute(query)
        if result:
            return StatusReserva(result[0][1], result[0][2], result[0][3], result[0][0])
        else:
            return None

    def update(self, st: StatusReserva):
        query = f"UPDATE status_reserva SET nome = '{st.nome}', telefone = '{st.telefone}', data = '{st.data}'  WHERE id = '{st.id}'"
        self.execute(query)

    def execute(self, custom_query):
        return super().execute_query(custom_query)

    def exists(self, status_id: str) -> bool:
        query = f"SELECT COUNT(*) FROM status_reserva WHERE id = '{status_id}'"
        result = super().execute_query(query)
        return result[0][0] > 0
