import sqlite3

class TableAgent:
    def __init__(self, db_path="academic.db"):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def execute(self, sql, params=()):
        try:
            self.cursor.execute(sql, params)
            return self.cursor.fetchall()
        except Exception as e:
            return f"Error: {e}"
