# First time initialisation of the program. This is run when the program is first run, and creates the database and tables.

# Importing sqlite3 for database management (temp, will be changed to mysql server hosted remotely), time for delays and clear_screen for clearing the screen.

import sqlite3
import time
from clear_screen import ClearScreen

# Function to create the database and tables.

def FirstTimeSetup():

    ClearScreen()

    print('''
    -------------------------------------------
    Welcome to SpellSharp. 
    We just need to set a few things up first.
    -------------------------------------------
    ''')

    ClearScreen()

    conn = sqlite3.connect("spellr.db")

    print("Database created.")

    c = conn.cursor()

    try:
        c.execute("""CREATE TABLE teacheraccounts (
                    integer PRIMARY KEY AUTOINCREMENT,
                    fname text,
                    lname text,
                    dob integer,
                    username text,
                    saltedpassword text,
                    salt text
                    )""")
    except sqlite3.OperationalError:
        pass

    try:
        c.execute("""CREATE TABLE studentaccounts (
                    integer PRIMARY KEY AUTOINCREMENT,
                    fname text,
                    lname text, 
                    dob integer,
                    username text,
                    saltedpassword text,
                    salt text,
                    class text,
                    teacher text
                    )""")
    except sqlite3.OperationalError:
        pass

    try:
        c.execute("""CREATE TABLE scores (
                    integer PRIMARY KEY AUTOINCREMENT,
                    username text,
                    testdate integer,
                    score integer,
                    testid integer
                    )""")
    except sqlite3.OperationalError:
        pass
    
    try:
        c.execute("""CREATE TABLE spellings (
                    integer PRIMARY KEY AUTOINCREMENT,
                    word text,
                    definition text
                    )""")
    except sqlite3.OperationalError:
        pass

    try:
        c.execute("""CREATE TABLE tests (
                    integer PRIMARY KEY AUTOINCREMENT,
                    testid text,
                    testdate integer,
                    testword text,
                    testdefinition text
                    )""")
    except sqlite3.OperationalError:
        pass

    try:
        c.execute("""CREATE TABLE classes (
                    integer PRIMARY KEY AUTOINCREMENT,
                    class text,
                    teacher text
                    )""")
    except sqlite3.OperationalError:
        pass

    conn.commit()

    conn.close()

    print("\nFirst time setup complete, taking you to the main menu.")
    time.sleep(3)
    ClearScreen()
    return

# q: I want to give each table entry a unique ID, but I don't want to have to manually enter it. Is there a way to do this automatically?

# a: Yes, you can use the AUTOINCREMENT keyword. This will automatically increment the ID by 1 each time a new entry is added.

# q: Does it have a name that I can use to refer to it?

# a: Yes, it's called "integer". You can use this to refer to the ID in other functions.

# q: How do I use it?

# a: You can use it in the same way as you would use any other variable. For example, if you wanted to add a new entry to the teacheraccounts table, you could do the following:

# c.execute("INSERT INTO teacheraccounts VALUES (:integer, :fname, :lname, :dob, :username, :saltedpassword, :salt)", {'integer': None, 'fname': 'John', 'lname': 'Smith',

# q: In the statement above, you used the keyword "None". What does this do?

# a: This is a placeholder for the ID. When you use the keyword "None", the ID will automatically be incremented by 1.

# q: What if I want to use a different value for the ID?

# a: You can use any value you want, but it must be unique. If you try to use a value that is already in use, you will get an error.

# q: What if I want to use a value that is already in use?

# a: You can use the REPLACE keyword. This will replace the existing entry with the new one.

# q: Thanks

# a: No problem

# q: I want to make it so that when I add a new entry to the table, it returns the unique ID of the new entry. Is this possible?

# a: Yes, you can use the cursor.lastrowid function. This will return the ID of the last entry that was added to the table.

# q: Fantastic, thanks

# a: No problem