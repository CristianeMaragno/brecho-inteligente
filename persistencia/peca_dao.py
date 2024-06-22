from persistencia.dao import DAO
from entidade.peca import Peca
from entidade.status_tipos.statusRestauracao import StatusRestauracao
from entidade.status_tipos.statusAVenda import StatusAVenda
from entidade.status_tipos.statusReserva import StatusReserva

class PecaDAO(DAO):
    def __init__(self, strdao, savdao, resdao):
        super().__init__()
        self.conn = None
        super().connect()
        super().create_table(
            "pecas",
            {
                "id": "TEXT PRIMARY KEY",
                "descricao": "TEXT",
                "status_id": "TEXT",
                "custo_aquisicao": "REAL",
                "titulo": "TEXT",
                "imagem": "TEXT",
                "preco": "REAL",
            },
        )
        self.strdao = strdao
        self.savdao = savdao
        self.resdao = resdao

    def add(self, peca: Peca):
        data = [
            (
                peca.id,
                peca.descricao,
                peca.status.id,
                peca.custo_aquisicao,
                peca.titulo,
                peca.imagem,
                peca.preco,
            )
        ]
        with self.conn:
            self.strdao.add(peca.status)
            super().insert_data("pecas", data)

    def remove(self, codigo: str):
        with self.conn:
            peca = self.get_by_id(codigo)
            if peca and peca.status:
                self.strdao.remove(peca.status.id)
                self.savdao.remove(peca.status.id)
            super().delete("pecas", "id", codigo)

    def get_all(self):
        rows = super().fetch_data("pecas")
        pecas = []
        for row in rows:
            status_rest = self.strdao.get_by_id(row[2])
            status_avenda = self.savdao.get_by_id(row[2])
            status_reserva = self.resdao.get_by_id(row[2])
            status = None
            if status_rest:
                status = status_rest
            elif status_avenda:
                status = status_avenda
            elif status_reserva:
                status = status_reserva
            pecas.append(Peca(*row[:2], status, *row[3:]))
        return pecas

    def get_by_id(self, codigo: str):
        result = self.execute(f"SELECT * FROM pecas WHERE id = '{codigo}'")
        if result:
            peca_data = result[0]
            status_rest = self.strdao.get_by_id(peca_data[2])
            status_avenda = self.savdao.get_by_id(peca_data[2])
            status_reserva = self.resdao.get_by_id(peca_data[2])
            status = None
            if status_rest:
                status = status_rest
            elif status_avenda:
                status = status_avenda
            elif status_reserva:
                status = status_reserva
            return Peca(*peca_data[:2], status, *peca_data[3:])
        return None

    def update(self, peca: Peca):
        with self.conn:
            old_peca = self.get_by_id(peca.id)
            if isinstance(peca.status, StatusRestauracao):
                self.strdao.add(peca.status)
                self.strdao.remove(old_peca.status.id)
            elif isinstance(peca.status, StatusAVenda):
                if self.strdao.get_by_id(old_peca.status.id):
                    self.strdao.remove(old_peca.status.id)
                if self.savdao.get_by_id(old_peca.status.id):
                    self.savdao.remove(old_peca.status.id)
                self.savdao.add(peca.status)
            elif isinstance(peca.status, StatusReserva):
                status_sav = self.savdao.get_by_id(old_peca.status.id)
                status_rev = self.resdao.get_by_id(old_peca.status.id)
                if status_sav:
                    self.savdao.remove(old_peca.status.id)
                if status_rev:
                    self.resdao.remove(old_peca.status.id)
                self.resdao.add(peca.status)

            query = (
                "UPDATE pecas SET descricao = ?, imagem = ?, status_id = ?, custo_aquisicao = ?, "
                "titulo = ?, preco = ? WHERE id = ?"
            )
            data = (
                peca.descricao,
                peca.imagem,
                peca.status.id,
                peca.custo_aquisicao,
                peca.titulo,
                peca.preco,
                peca.id,
            )
            self.execute(query, data)

    def execute(self, custom_query, params=()):
        return super().execute_query(custom_query, params)
