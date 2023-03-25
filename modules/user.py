from modules import sql
import sqlite3
import datetime
import hashlib


# Database connection function
def connectDb():
    database = sqlite3.connect("Python1.db")
    cursor = database.cursor()

    return [database, cursor]


connect = connectDb()
database = connect[0]
cursor = connect[1]


class user:

    def __init__(self, name, lastname, mail, password):
        self.name = name
        self.lastname = lastname
        self.mail = mail
        self.password = password

    def register(self):
        date = datetime.datetime.now()

        # Password cypher
        encryption = hashlib.sha256()
        encryption.update(self.password.encode('utf8'))

        sql = "INSERT INTO users VALUES(null, ?, ?, ?, ?, ?)"
        user = (self.name, self.lastname, self.mail, encryption.hexdigest(), date)

        try:
            cursor.execute(sql, user)
            database.commit()
            result = [cursor.rowcount, self]
        except Exception as e:
            print(f"Error: {e}")
            result = [0, self]

        return result

    def login(self, cursor, connection):

        # User exists?
        sql = "SELECT * from users WHERE mail = ? AND password = ?"

        encryption = hashlib.sha256()
        encryption.update(self.password.encode('utf-8'))

        # Query data
        user = (self.mail, encryption.hexdigest())

        cursor.execute(sql, user)
        result = cursor.fetchone()

        return result
