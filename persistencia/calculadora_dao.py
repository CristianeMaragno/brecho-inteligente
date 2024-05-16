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

        if not self.check_data_exists('custos'):

            data = [
                ('Lavar', 0.0),
                ('Passar', 0.0),
                ('Reparo de Falhas', 0.0),
                ('Restauração de Detalhes', 0.0),
                ('Remoção de Manchas', 0.0),
                ('Tingimento', 0.0),
                ('Customizacao', 0.0),
                ('TaxaDeLucro', 0.0)
            ]

            super().insert_data('custos', data)

    def check_data_exists(self, table_name):
        query = f"SELECT COUNT(*) FROM {table_name}"
        self.cursor.execute(query)
        count = self.cursor.fetchone()[0]
        return count > 0

    # def add_custo(self, categoria, custo):
    #     if not self.get_custo(categoria):
    #         data = [(categoria, custo)]
    #         super().insert_data('custos', data)


    def get_custo(self, categoria):
         result = super().fetch_data('custos')
         for row in result:
             if row[0] == categoria:
                 return row[1]
         return None
    
    # def verifica_categoria(self, categoria):
    #     result = super().fetch_data('custos')
    #     print(result)
    #     for row in result:
    #         if row[0] == categoria:
    #             return True
    #     return False

    def update_custo(self, categoria, novo_custo):
        set_values = {'custo': novo_custo}
        condition = "categoria = '" + categoria + "'"
        super().update('custos', set_values, condition)


    # def delete_custo(self, categoria):
    #     super().delete('custos', 'categoria', categoria)

    def get_todas_categorias(self):
        result = super().fetch_data('custos')
        categorias = [row[0] for row in result]
        return categorias
