import sqlite3
import datetime

class DatabaseManager:
    def __init__(self, db_name="access_log.db"):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.create_table()

    def create_table(self):
        query = '''CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            timestamp TEXT
        )'''
        self.conn.execute(query)
        self.conn.commit()

    def add_log(self, name):
        ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.conn.execute("INSERT INTO logs (name, timestamp) VALUES (?, ?)", (name, ts))
        self.conn.commit()
