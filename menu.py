import os
import questionary as qst
from API import api
import edition_menu
from datetime import date

# Main menu functionalities: 

def clear_terminal():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def main_menu(username, user_id):
    clear_terminal()
    while True:
        answer = qst.select(
            ">>>",
            choices=[
                "Show all daily records",
                "Edit(Create, Update, Delete)"
            ]
        ).ask()

        if answer == "Show all daily records":
            show_all(username)
        elif answer == "Edit(Create, Update, Delete":
            edit_menu(username)

def show_all(username):
    all_entries = api.all_entries(username) # a list of all dates within the database

    selected_date = qst.select(
        ">>>",
        choices=[
            line for line in all_entries
        ]
    ).ask()

    if selected_date:
        details = api.get_habits_by_date(username, selected_date)

        for habit_name, status in details:
            icon = "✅ Done" if status == 1 else "❌ Not done"
            print(f"{habit_name}: {icon}")

def edit_menu(username, user_id):
    while True:
        option = qst.select(
            ">>>",
            choices=[
                "Create entry",
                "Update entry",
                "Delete entry"
            ]
        ).ask()

        if option == "Create Entry":
            entry_date = qst.select(
                "Is the date of this entry today?",
                choices=[
                    "Yes",
                    "No"
                ]
            ).ask()

            if entry_date == "Yes":
                entry_date = date.today().isoformat()
            else:
                entry_date = qst.text("Please provide the date(Example of date: 2026-01-24):").ask() # Treat this
            create_entry(entry_date, user_id)
        
        elif option == "Update Entry":
            update_date = qst.text("From which date would you like to update(Example of date: 2026-01-24):").ask()
            update_entry(update_date)
        
        elif option == "Delete Entry":
            delete_date = qst.text("Which date would you like to delete from database(Example of date: 2026-01-24)").ask()
            delete_entry(delete_date)

def create_entry(date, user_id):
    data = qst.text("Provide the habits you practiced on this date(Use a list of comma separated values with no space. Ex: Exercised,Read,Worked,Coded)").ask()
    data = data.split(",")

    data_tuple = (date, data)

    api.create_entry(data_tuple, user_id)