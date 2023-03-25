from modules import user as model
import data.functions
import sqlite3

class Actions:

    def __init__(self):
        self.connection = sqlite3.connect('Python1.db')
        self.cursor = self.connection.cursor()

    def register(self):
        print("Register Form")

        user = model.user('','','','')

        user.name = input("What's your name?: ")
        user.lastname = input("What's your last name?: ")
        user.mail = input("What's your email?: ")
        user.password = input("Type in your password: ")

        register = user.register()

        if register[0]>=1:
            print(f"Great {register[1].name}, you are now a registered user!")
        else:
            print("You haven't registered correctly.")

    def login(self):
        print("Login Form")
        mail = input("Mail: ")
        password = input("Password: ")

        user = model.user('', '', mail, password)
        login = user.login(self.cursor, self.connection)

        if mail == login[3]:
            print(f"Welcome {login[1]}!")
            self.nextFunctions(login)
        else:
            print("Wrong credentials.")

    def nextFunctions(self, user):

        print("""
            Available functions:
        -Create a new note (create)
        -Display saved notes (show)
        -Delete a saved note (delete)
        -Exit the program (exit)
        """)

        func = input("What do you wish to do?: ")

        # Call methods and class so I can create the object
        doAction = data.functions.Functions()

        if func.lower() == "create":
            doAction.create(user, self.cursor, self.connection)
            self.nextFunctions(user)
        elif func.lower() == "show":
            doAction.show(user, self.cursor)
            self.nextFunctions(user)
        elif func.lower() == "delete":
            doAction.delete(user, self.cursor, self.connection)
            self.nextFunctions(user)
        elif func.lower() == "exit":
            print(f"See you later. Nachito. I mean, {user[1]}.")
            exit()
