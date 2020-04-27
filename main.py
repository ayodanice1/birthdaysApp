from checkBirthdays import BirthdayApp

def main():
    """
    Welcome to the birthday app.
    The program is case-insensitive.
    
    The list of things you can do on the program are:
    'ADD' - to add a new birthday,
    'TODAY' - to check birthdays for today,
    'CHECK' - to check for a person's birthday,
    'ALL' - to see all birthdays,
    'DELETE' - to delete an entry,
    'CLOSE' - to close the app.
    """
    # Create an instance of Birthday app, initiated with the specified db name
    db_name = input("Specify the database name ending in .db: ")
    app = BirthdayApp(db_name)
    
    # Keep the terminal opened till the user's choice is 'close'
    while True:
        choice = (str(input("\nEnter action choice here: "))).lower()
        # Add a new entry
        if choice == 'add':
            first_name = (input("\nEnter the first name here: ")).capitalize()
            last_name = (input("Enter the last name here: ")).capitalize()
            dob = input("Enter the date-of-birth here (yyyy-mm-dd): ")
            app.addBirthday(first_name, last_name, dob)
        # Check the birthdays for the current date
        elif choice == 'today':
            birthdays_today, current_year = app.checkBirthdays()
            if len(birthdays_today) == 0: print("There are no birthdays today")
            else:
                for birthday in birthdays_today:
                    first_name = birthday[0]
                    last_name = birthday[1]
                    birth_year = int(birthday[2])
                    age = current_year - birth_year
                    print(f"{first_name} {last_name} is {age} years old today.")
        # Check for a specific birthday
        elif choice == "check":
            name = input("\nEnter both the first and last names separated by space, here: ")
            name_array = name.split(" ")
            print(app.displayOne(name_array))
        # See all the entries on the app
        elif choice == 'all':
            print("\nAll birthday entries on this app are:")
            for entry in app.displayAll(): print(entry)
        # Delete a specific entry
        elif choice == 'delete':
            name = input("\nEnter both the first and last names separated by space, here: ")
            name_array = name.split(" ")
            app.deleteBirthday(name_array)
        # Close the app
        elif choice == 'close': break


if __name__ == '__main__':
    main()
