import questionary as qst
from API import api
import menu

def initial_prompt():
    global user_id

    while True:
        answer = qst.select(
            ">>>",
            choices=[
                "Login",
                "Register",
                "Quit"
            ]
        ).ask()

        if answer == "Login":
            login(user_id)
            break                                           # remove
        elif answer == "Register":
            user_id = register()
        else:
            quit()

# LOGIN SYSTEM:

def login(user_id):
    username = qst.text("Username:").ask()
    password = qst.text("Password:").ask() # I know

    api_call = api.read(username, password)

    if api_call == True:
        print("Successfully logged in. Welcome again!")
        menu.main_menu(username, user_id)

def register():
    username = qst.text("Username:").ask()
    password = qst.text("Password:").ask()

    api_call = api.write(username, password)

    if api_call == True:
        user_id = api.get_user_id(username)
        print("Registration complete. Welcome!")
        return user_id
    else:
        print("Something wrong happened. Try again.")