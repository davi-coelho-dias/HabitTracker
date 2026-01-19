from database.configs import DB_PATH, create_db
import sqlite3

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

create_db()

def read(username, password):
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE NOT NULL, password TEXT NOT NULL)")
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
    user_db = cursor.fetchone()

    if user_db:
        password_db = user_db[2] # user_db is a tuple (id, username, password)

        if password_db == password:
            return True
        else:
            print("Wrong password.")
            return False
    else:
        print("Credentials not found.")
        return False

def write(username, password):
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE NOT NULL, password TEXT NOT NULL)")

    cursor.execute(f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')")
    return True 