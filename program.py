from modules import actions
from modules import user

print("""
Available actions:
    -Register
    -Login
""")

do = actions.Actions()
func = input("Welcome! What do you wish to do? ")

if func.lower() == "register":
    do.register()
elif func.lower() == "login":
    do.login()