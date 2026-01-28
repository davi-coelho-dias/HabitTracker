import questionary as qst
from API import api
import menu

def initial_prompt():
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
            login()
        elif answer == "Register":
            register()
        else:
            quit()

# LOGIN SYSTEM:

def login():
    username = qst.text("Username:").ask()
    password = qst.text("Password:").ask() # I know

    api_call = api.read(username, password)

    if api_call == True:
        print("Successfully logged in. Welcome again!")
        user_id = api.get_user_id(username)
        menu.main_menu(username, user_id) # just passed the user_id correctly to main_menu

def register():
    username = qst.text("Username:").ask()
    password = qst.text("Password:").ask()

    api_call = api.write(username, password)

    if api_call == True:
        print("Registration complete. Welcome!")
    else:
        print("Something wrong happened. Try again.")