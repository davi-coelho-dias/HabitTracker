import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "app.db")

def create_db():
    connection = sqlite3.connect(DB_PATH)
    cursor  = connection.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    # Table for holding user info
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    
    # Table for holding what was done in what day
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS days (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            habit TEXT NOT NULL,
            date DATE NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    """)

    # Table for holding what habit belongs to each user
    # cursor.execute("""
    #     CREATE TABLE IF NOT EXISTS habits (
    #         id INTEGER PRIMARY KEY AUTOINCREMENT,
    #         user_id INTEGER,
    #         habit TEXT NOT NULL,
    #         FOREIGN KEY (user_id) REFERENCES users (id)
    #     )
    # """)

    connection.commit()
    connection.close()