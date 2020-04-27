import sqlite3
from datetime import date


class BirthdayApp(object):

    def __init__(self, db_name):
        self.db_name = db_name
        self._con = sqlite3.connect(db_name)
        self._conn = self._con.cursor()
        self.createTables()

    def createTables(self):
        try:
            print(f"\nPreparing database '{self.db_name}'...")
            print("Creating table Birthdays...")
            self._conn.execute("""
                CREATE TABLE Birthdays(firstname text, lastname text, year integer, month integer, day integer)
            """)
            self._con.commit()
        except sqlite3.OperationalError as err: print(err)
        else: print("Database successfully prepared!\n")

    def addBirthday(self,first_name, last_name, dob):
        dob_lit = dob.split('-')
        year, month, day = dob_lit[0], dob_lit[1], dob_lit[2]
        # Check if entry already exist. If it does, do not add entry. Else add entry
        check = self.checkEntryExistence(first_name, last_name, year, month, day)
        if len(check) == 1: print("Entry already exist!")
        else:
            self._conn.execute(
                "INSERT INTO Birthdays(firstname, lastname, year, month, day) VALUES (?,?,?,?,?)",
                (first_name, last_name, year, month, day))
            self._con.commit()
            print("Entry added successfully!")

    def checkBirthdays(self):
        today = date.today().timetuple()
        year, month, day = today[0], today[1], today[2]
        return self._conn.execute(
            "SELECT firstname, lastname, year FROM Birthdays WHERE day=? AND month=?", (day, month)).fetchall(), year

    def displayAll(self):
        return self._conn.execute("SELECT * FROM Birthdays ORDER BY firstname").fetchall()

    def displayOne(self, name_array):
        first_name = name_array[0].capitalize()
        last_name = name_array[1].capitalize()
        return self._conn.execute(
            "SELECT * FROM Birthdays WHERE firstname=? AND lastname=?", (first_name, last_name)).fetchone()

    def deleteBirthday(self, name_array):
        first_name = name_array[0].capitalize()
        last_name = name_array[1].capitalize()

        self._conn.execute(
            "DELETE FROM Birthdays WHERE firstname=? AND lastname=?", (first_name, last_name))
        self._con.commit()
        print("Entry deleted successfully!")
    
    def checkEntryExistence(self, first_name, last_name, year, month, day):
        return self._conn.execute(
            "SELECT * FROM Birthdays WHERE firstname=? AND lastname=? AND year=? AND day=? AND month=?", 
            (first_name, last_name, year, day, month)).fetchall()
        
