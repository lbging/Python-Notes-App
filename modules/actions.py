from modules import user as model
import data.functions
import sqlite3

class Actions:

    def register(self):
        print("Register Form")

        name = input("What's your name?: ")
        lastname = input("What's your last name?: ")
        mail = input("What's your email?: ")
        password = input("Type in your password: ")

        user = model.user(name, lastname, mail, password)
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
        login = user.login()

        if mail == login[3]:
            print(f"Welcome {login[1]}!")
        self.nextFunctions(login)

        try:
            mail = input("Mail: ")
            password = input("Password: ")

            user = model.user('', '', mail, password)
            login = user.login()

            if mail == login[3]:
                print(f"Welcome {login[1]}!")
            self.nextFunctions(login)

        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"Wrong credentials.")

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
            doAction.create(user)
            self.nextFunctions(user)
        elif func.lower() == "show":
            doAction.show(user)
            self.nextFunctions(user)
        elif func.lower() == "delete":
            doAction.delete(user)
            self.nextFunctions(user)
        elif func.lower() == "exit":
            print(f"See you later. Nachito. I mean, {user[1]}.")
            exit()
            conn.close()

