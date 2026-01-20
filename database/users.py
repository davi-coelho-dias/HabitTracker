from database.configs import DB_PATH
import sqlite3

def read(username, password):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE NOT NULL, password TEXT NOT NULL)")
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
    user_db = cursor.fetchone()

    connection.close()

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
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE NOT NULL, password TEXT NOT NULL)")
    cursor.execute(f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')")

    connection.commit()
    connection.close()

    return True 

def get_user_id(username):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute(f"SELECT id FROM users WHERE username = '{username}'")
    result = cursor.fetchone()

    connection.close()

    if result:
        user_id = result[0]
    else:
        user_id = None

    return user_id

def save_tracking_habits(date, habit_name, user_id):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute(f"SELECT id FROM habits WHERE habit = '{habit_name}' AND user_id = '{user_id}'")
    result = cursor.fetchone()

    if result:
        habit_id = result[0]
    else:
        cursor.execute(f"INSERT INTO habits (user_id, habit) VALUES ('{user_id}', '{habit_name}')")
        connection.commit()
        habit_id = cursor.lastrowid

    cursor.execute(f"""
        INSERT INTO days (user_id, habit_id, date)
        VALUES ('{user_id}', '{habit_id}', '{date}')
    """)

    connection.commit()
    connection.close()

def delete_day_records(date, user_id):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute(f"DELETE FROM days WHERE date = '{date}' AND user_id = '{user_id}'")

    connection.commit()
    connection.close()