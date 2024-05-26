from persistencia.dao import DAO
from entidade.categoria import Categorias
from persistencia.categorias_dao import CategoriasDAO


class CalculadoraDAO(DAO):
    def __init__(self):
        super().__init__()
        super().connect()
        self.create_table()
        self.categorias_dao = CategoriasDAO()  # Inicializa o CategoriasDAO

    def create_table(self):
        columns = {
            'categoria': 'TEXT PRIMARY KEY',
            'custo': 'REAL'
        }
        super().create_table('custos', columns)

        if not self.check_data_exists('custos'):
            data = [
                ('Lavar', 0.0),
                ('Passar', 0.0),
                ('Reparar danos', 0.0),
                ('Restaurar detalhes', 0.0),
                ('Remover manchas', 0.0),
                ('Tingir', 0.0),
                ('Customizar', 0.0),
                ('Taxa de Lucro', 0.0)
            ]
            super().insert_data('custos', data)

    def check_data_exists(self, table_name):
        query = f"SELECT COUNT(*) FROM {table_name}"
        self.cursor.execute(query)
        count = self.cursor.fetchone()[0]
        return count > 0

    def get_custo(self, categoria):
        result = super().fetch_data('custos')
        for row in result:
            if row[0] == categoria:
                return row[1]
        return None

    def update_custo(self, categoria, novo_custo):
        set_values = {'custo': novo_custo}
        condition = "categoria = '" + categoria + "'"
        super().update('custos', set_values, condition)
        self.update_custo_categoria(categoria, novo_custo)  # Atualiza o custo padrão no CategoriasDAO

    def update_custo_categoria(self, categoria, novo_custo):
        categorias = self.categorias_dao.get_all()
        for ct in categorias:
            if ct.nome == categoria:
                ct.custo_padrao = novo_custo
                self.categorias_dao.update(ct.id, ct)

    def get_todas_categorias(self):
        result = super().fetch_data('custos')
        categorias = [row[0] for row in result]
        return categorias
