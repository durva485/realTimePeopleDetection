import sqlite3
from datetime import datetime

conn = None
cursor = None

def initialize_database():
    global conn, cursor
    conn = sqlite3.connect("people_count.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            timestamp TEXT,
            count INTEGER
        )
    ''')
    conn.commit()

def log_count(count):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO logs (timestamp, count) VALUES (?, ?)", (timestamp, count))
    conn.commit()

def close_connection():
    if conn:
        conn.close()
