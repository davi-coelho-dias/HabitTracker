from database.configs import DB_PATH
import sqlite3

def read_all(username):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute(f"SELECT date FROM days JOIN users ON days.user_id = users.id WHERE users.username = '{username}'")
    all_entries = cursor.fetchall()

    connection.close()

    return all_entries

def get_habits_by_date(username, date):
    connection = sqlite3.connect()
    cursor = connection.cursor()

    cursor.execute(f"SELECT habits.habit FROM days JOIN habits ON days.habit_id = habits.id WHERE days.user_id = '{username}' AND days.date = '{date}'")
    results = cursor.fetchall()

    connection.close()
    
    return results