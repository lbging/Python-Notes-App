import sqlite3

# SQL connection module


def connectDb():
    database = sqlite3.connect("Python1.db")
    cursor = database.cursor()

    return [database, cursor]


def create_tables():
    database, cursor = connectDb()

    create_users_table = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        lastname TEXT NOT NULL,
        mail TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        date_registered TEXT NOT NULL
    );
    '''

    create_notes_table = '''
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        date_created TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users (id)
    );
    '''

    cursor.execute(create_users_table)
    cursor.execute(create_notes_table)
    database.commit()
