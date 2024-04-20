import sqlite3
from abc import ABC


class DAO(ABC):
    def __init__(self):
        self.db_name = "brecho.db"

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print("Error connecting to the database:", e)

    def disconnect(self):
        if hasattr(self, 'conn') and self.conn:
            self.conn.close()

    def create_table(self, table_name, columns):
        try:
            with self.conn:
                column_definitions = ', '.join([f"{col_name} {col_type}" for col_name, col_type in columns.items()])
                query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions})"
                self.cursor.execute(query)
        except sqlite3.Error as e:
            print("Error creating table:", e)

    def insert_data(self, table_name, data):
        try:
            with self.conn:
                placeholders = ', '.join(['?' for _ in range(len(data[0]))])
                query = f"INSERT INTO {table_name} VALUES ({placeholders})"
                self.cursor.executemany(query, data)
        except sqlite3.Error as e:
            print("Error inserting data:", e)

    def fetch_data(self, table_name):
        try:
            with self.conn:
                query = f"SELECT * FROM {table_name}"
                self.cursor.execute(query)
                return self.cursor.fetchall()
        except sqlite3.Error as e:
            print("Error fetching data:", e)

    def execute_query(self, query):
        try:
            with self.conn:
                self.cursor.execute(query)
                return self.cursor.fetchall()
        except sqlite3.Error as e:
            print("Error executing query:", e)
