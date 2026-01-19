import os

# Build main menu: user select options like show all logs, create habits, delete, update, and so on...

def clear_terminal():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def main_menu():
    clear_terminal()
    print("Hello world main menu")