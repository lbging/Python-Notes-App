from data import notes as model


class Functions:

    def create(self, user, cursor, connection):
        print(f"Let's create a new note, {user[1]}!")

        title = input("What's the title?: ")
        content = input("Write your note: ")

        note = model.Notes(user[0], title, content)
        save = note.save()

        if save[0] >= 0:
            print(f"Note saved: {note.title}.")
        else:
            print(f"Note couldn't be saved.")

    def show(self, user, cursor):
        print(f"{user[1]}, these are your notes: ")

        note = model.Notes(user[0], "", "")
        notes = note.list()

        for note in notes:
            print("----------------------------------------------------------------------------")
            print(f"Title: {note[2]}")
            print(f"Content: {note[3]}")
            print(f"Date created: {note[4]}")
        print("----------------------------------------------------------------------------")

    def delete(self, user, cursor, connection):
        print(f"Note deletion module.")

        title = input("What's the title of the note you want to erase?")
        note = model.Notes(user[0], title, '')
        delete = note.delete()

        if delete[0] >= 1:
            print(f"{note.title} has been succesfully deleted!")
        else:
            print(f"Note couldn't be deleted.")


