from modules import actions
from modules import user
from modules import sql


def main_menu():
    print("""
    Available actions:
        -Register
        -Login
        -Exit
    """)

    return input("Welcome! What do you wish to do? ").lower()


sql.create_tables()
do = actions.Actions()

while True:
    func = main_menu()

    if func == "register":
        do.register()
    elif func == "login":
        do.login()
    elif func == "exit":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")
