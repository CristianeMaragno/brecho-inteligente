from persistencia.dao import DAO

class CalculadoraDAO(DAO):
    def __init__(self):
        super().__init__()
        super().connect()
        self.create_table()

    def create_table(self):
        columns = {
            'categoria': 'TEXT PRIMARY KEY',
            'custo': 'REAL'
        }
        super().create_table('custos', columns)

        # Inserir as categorias com custo padrão
        categorias_padrao = [
            ('lavar', 0.0),
            ('passar', 0.0),
            ('reparoDeFalhas', 0.0),
            ('restauracaoDeDetalhes', 0.0),
            ('remocaoDeManchas', 0.0),
            ('tingimento', 0.0),
            ('customizacao', 0.0),
            ('taxaDeLucro', 0.0)
        ]
        for categoria, custo in categorias_padrao:
            if not self.verifica_categoria(categoria):
                self.add_custo(categoria, custo)

    def add_custo(self, categoria, custo):
        if not self.get_custo(categoria):
            data = [(categoria, custo)]
            super().insert_data('custos', data)


    def get_custo(self, categoria):
        result = super().fetch_data('custos')
        for row in result:
            if row[0] == categoria:
                return row[1]
        return None
    
    def verifica_categoria(self, categoria):
        result = super().fetch_data('custos')
        for row in result:
            if row[0] == categoria:
                return True
        return False

    def update_custo(self, categoria, novo_custo):
        set_values = {'custo': novo_custo}
        condition = "categoria = ?"
        super().update('custos', set_values, condition, (categoria,))

    def delete_custo(self, categoria):
        super().delete('custos', 'categoria', categoria)

    def get_todas_categorias(self):
        result = super().fetch_data('custos')
        categorias = [row[0] for row in result]
        return categorias
