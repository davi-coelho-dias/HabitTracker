import pyfiglet
import os
import login
from database import configs

configs.create_db()

banner = "HabitTracker"
banner_ascii_art = pyfiglet.figlet_format(banner)

def welcome_sign():
    print(banner_ascii_art)

def welcome_message():
    print("---------------------------------------")
    print("Welcome to your personal HabitTracker application!")
    print("Use arrow keys to choose and Enter to select it.")
    print("---------------------------------------")

def clear_terminal():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

clear_terminal()
welcome_sign()
welcome_message()

login.initial_prompt()