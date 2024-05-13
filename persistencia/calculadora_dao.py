from persistencia.dao import DAO

class CalculadoraDAO(DAO):
    def __init__(self):
        super().__init__()
        super().connect()
        self.create_table()

    def create_table(self):
        query = '''CREATE TABLE IF NOT EXISTS custos (
                    categoria TEXT PRIMARY KEY,
                    custo REAL
                )'''
        super().create_table(query)

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
            if not self.get_custo(categoria):
                self.add_custo(categoria, custo)


    def add_custo(self, categoria, custo):
        query = "INSERT INTO custos (categoria, custo) VALUES (?, ?)"
        data = (categoria, custo)
        super().insert_data(query, data)

    def get_custo(self, categoria):
        query = "SELECT custo FROM custos WHERE categoria = ?"
        data = (categoria,)
        result = super().fetch_data(query, data)
        if result:
            return result[0][0]
        else:
            return None

    def update_custo(self, categoria, novo_custo):
        query = "UPDATE custos SET custo = ? WHERE categoria = ?"
        data = (novo_custo, categoria)
        super().execute_query(query, data)

    def delete_custo(self, categoria):
        query = "DELETE FROM custos WHERE categoria = ?"
        data = (categoria,)
        super().execute_query(query, data)
