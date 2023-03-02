from modules import sql
import datetime
import hashlib

# Database connection function
connect = sql.connectDb()
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

        sql = "INSERT INTO users VALUES(null, %s, %s, %s, %s, %s)"
        user = (self.name, self.lastname, self.mail, encryption.hexdigest(), date)

        try:
            cursor.execute(sql, user)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]
        
        return result
    
    def login(self):

        # User exists?
        sql = "SELECT * from users WHERE mail = %s AND password = %s"

        encryption = hashlib.sha256()
        encryption.update(self.password.encode('utf-8'))

        # Query data
        user = (self.mail, encryption.hexdigest())

        cursor.execute(sql, user)
        result = cursor.fetchone()

        return result
    


