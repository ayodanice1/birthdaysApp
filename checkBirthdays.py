import sqlite3
from datetime import date


class BirthdayApp(object):

    def __init__(self):
        self._con = sqlite3.connect('birthdays.db')
        self._conn = self._con.cursor()
        self._createTables()

    def _createTables(self):
        try:
            print("\nPreparing database 'Birthdays'...")
            self._conn.execute(
                "CREATE TABLE Birthdays(firstname text, lastname text, year integer, month integer, day integer)")
            self._con.commit()
        except sqlite3.OperationalError:
            print("Database successfully prepared!\n")

    def addBirthday(self):
        first_name = input("\nEnter person's first name here: ")
        last_name = input("Enter person's last name here: ")
        dob = input("Enter his/her date-of-birth here (yyyy-mm-dd): ")

        dob_lit = dob.split('-')
        year, month, day = dob_lit[0], dob_lit[1], dob_lit[2]

        self._conn.execute(
            "INSERT INTO Birthdays(firstname, lastname, year, month, day) VALUES (?,?,?,?,?)",
            (first_name, last_name, year, month, day))
        self._con.commit()

    def checkBirthdays(self):
        today = date.today().timetuple()
        year, month, day = today[0], today[1], today[2]

        res = self._conn.execute(
            "SELECT firstname, lastname, year FROM Birthdays WHERE day=? AND month=?", (day, month)).fetchall()
        if len(res) != 0:
            for person in res:
                birth_year = int(person[2])
                age = year - birth_year
                print("Hurray! Today is %s %s's birthday.\n" % (person[0], person[1]))
                print(person[0], " is now %d years old today." % age)
        else:
            print("There is no birthday today.\n")

    def displayAll(self):
        print("\n")
        res = self._conn.execute("SELECT * FROM Birthdays ORDER BY firstname").fetchall()
        for entry in res: print(entry)

    def displayOne(self, first_name):
        print ( res = self._conn.execute(
            "SELECT * FROM Birthdays WHERE firstname=?", first_name).fetchone()
                )

    def deleteBirthday(self, name_array):
        first_name = name_array[0]
        last_name = name_array[1]

        self._conn.execute(
            "DELETE FROM Birthdays WHERE firstname=? AND lastname=?", (first_name, last_name))
        self._con.commit()


def main():
    app = BirthdayApp()
    app.checkBirthdays()

    print("""You can add a new birthday by entering the word 'new',
check birthdays for today with the word 'today',
check for a person's birthday with 'check',
see all birthdays with the word 'entries',
delete an entry with the word 'delete',
and close the app with the word 'close'.""")

    while True:
        choice = str(input("\nWhat do you want to do now? \nEnter here: "))
        if choice == 'new':
            app.addBirthday()
        elif choice == 'today':
            app.checkBirthdays()
        elif choice == "check":
            app.displayOne([input("\nEnter the person's first name here: ")])
        elif choice == 'entries':
            app.displayAll()
        elif choice == 'delete':
            name = input("\nEnter the person's first and last names, separate by space, here: ")
            name_array = name.split(" ")
            app.deleteBirthday(name_array)
        elif choice == 'close':
            break


if __name__ == '__main__':
    main()
