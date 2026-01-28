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

    # checking to see if there already is an entry inside the database with that user_id, that habit name and that date
    cursor.execute(f"SELECT id FROM days WHERE user_id = '{user_id}' AND habit = '{habit_name}' AND date = '{date}'")
    db_check = cursor.fetchone()

    # if there isn't:
    if db_check is None:
        # add it
        cursor.execute(f"INSERT INTO days (user_id, habit, date) VALUES ('{user_id}', '{habit_name}', '{date}')")
        connection.commit()
    # if there is:
    else:
        return
    
    connection.close()

def delete_day_records(date, user_id):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute(f"DELETE FROM days WHERE date = '{date}' AND user_id = '{user_id}'")

    connection.commit()
    connection.close()