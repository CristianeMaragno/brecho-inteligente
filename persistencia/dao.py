import sqlite3
from abc import ABC


class DAO(ABC):
    def __init__(self):
        self.db_name = "brecho.db"
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def disconnect(self):
        if self.conn:
            self.conn.close()

    def create_table(self, table_name, columns):
        column_definitions = ', '.join([f"{col_name} {col_type}" for col_name, col_type in columns.items()])
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions})"
        self.cursor.execute(query)
        self.conn.commit()

    def insert_data(self, table_name, data):
        placeholders = ', '.join(['?' for _ in range(len(data[0]))])
        query = f"INSERT INTO {table_name} VALUES ({placeholders})"
        self.cursor.executemany(query, data)
        self.conn.commit()

    def fetch_data(self, table_name):
        query = f"SELECT * FROM {table_name}"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def execute_query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()
