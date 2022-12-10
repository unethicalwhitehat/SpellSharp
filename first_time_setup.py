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
    Welcome to Spellr. 
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
                    yeargroup integer,
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
        c.execute("""CREATE TABLE wordsanddefs (
                    integer PRIMARY KEY AUTOINCREMENT,
                    word text,
                    definition text
                    )""")
    except:
        pass

    try:
        c.execute("""CREATE TABLE tests (
                    integer PRIMARY KEY AUTOINCREMENT,
                    testname text,
                    testdate integer,
                    testwords text
                    )""")
    except:
        pass

    conn.commit()

    conn.close()

    print("\nFirst time setup complete, taking you to the main menu.")
    time.sleep(3)
    ClearScreen()
    return
