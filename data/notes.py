import modules.sql as sql
import datetime

connect = sql.connectDb()
database = connect[0]
cursor = connect[1]


class Notes:

    def __init__(self, user_id, title, content):
        self.user_id = user_id
        self.title = title
        self.content = content

    def save(self):
        sql = "INSERT INTO notes VALUES (null, ?, ?, ?, ?)"
        note = (self.user_id, self.title, self.content, datetime.datetime.now())

        cursor.execute(sql, note)
        database.commit()

        return (cursor.rowcount, self)

    def list(self):
        sql = f"SELECT * FROM notes WHERE user_id = {self.user_id}"

        cursor.execute(sql)
        result = cursor.fetchall()

        return result

    def delete(self):
        sql = f"DELETE FROM notes WHERE user_id = ? AND title = ?"

        note = (self.user_id, self.title)

        cursor.execute(sql, note)
        database.commit()

        return (cursor.rowcount, self)
