from database import users, days

def read(username, password):
    username = username.lower()
    password = password.lower()

    return_value = users.read(username, password)

    if return_value:
        return True
    else:
        return False
    
def write(username, password):
    username = username.lower()
    password = password.lower()

    return_value = users.write(username, password)

    if return_value:
        return True
    
def get_user_id(username):
    user_id = users.get_user_id(username)
    return user_id
    
def all_entries(username):
    records = days.read_all(username)
    clean_records = sorted(list(set([line[0] for line in records])))

    return clean_records

def get_habits_by_date(username, date):
    data = days.get_habits_by_date(username, date)

    return data

def create_entry(data_tuple, user_id):
    date = data_tuple[0]
    habits = data_tuple[1] # list of strings

    for habit in habits:
        users.save_tracking_habits(date, habit, user_id) 

def update_entry(data_tuple, user_id):
    date = data_tuple[0]

    users.delete_day_records(date, user_id)
    
    create_entry(data_tuple, user_id)

def delete_entry(date, user_id):
    users.delete_day_records(date, user_id)