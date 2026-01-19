from database import users

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