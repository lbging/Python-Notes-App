import mysql
import mysql.connector
import sqlite3

# SQL connection module

def connectDb():
    database = mysql.connector.connect(
        host = "localhost",
        port = 3306,
        database = "Python1",
        user = "root",
        passwd = "HalfLife3"
    )

    cursor = database.cursor(buffered=True)

    return [database, cursor]

