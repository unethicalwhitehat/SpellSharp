# Module for student testing

# Importing the necessary modules and functions.

import time
import sqlite3
import db_login
import student
import random
from clear_screen import ClearScreen

# Function to show the testing menu and take an input to proceed.

def Menu(fname, username):

    ClearScreen()
    
    print(f'''
    ----------------------------------------------------
    Welcome {fname}, please select an option from below:
    ----------------------------------------------------
    1) Start test
    2) Back
    ----------------------------------------------------
    ''')

    def ChooseOption():

        choice = input("> ")

        try:
            choice = int(choice)
        except ValueError:
            print("Please enter a number.")
            time.sleep(1)
            ChooseOption()

        if choice == 1:
            ChooseTest(username)
        elif choice == 2:
            ClearScreen()
            student.StudentMenu(fname, username)
        else:
            print("Please enter a valid option.")
            time.sleep(1)
            ChooseOption()
    
    ChooseOption()

# Function to choose the test.

def ChooseTest(username):
    conn = sqlite3.connect('spellsharp.db')
    c = conn.cursor()
    c.execute("SELECT testid FROM tests")
    testids = c.fetchall()

    print(f'''
    ------------------------------------------------------------------------------------------
    Please select the ID of the test you wish to take (your teacher will have given you this):
    ------------------------------------------------------------------------------------------
    ''')


    testnums = testids.count() 
    if testnums >= 5:
        testnums = testnums
    else:
        testnums = 5

    count = 0

    testidslist = []

    for i in range(testnums):
        count += 1
        print(f"{count}) {testids[i]}")
        testidslist.append(testids[i])

    print('''
    ------------------------------------------------------------------------------------------
    ''')

    def ChooseTest():

        choice = input("> ")

        try:
            choice = int(choice)
        except ValueError:
            print("Please enter a number.")
            time.sleep(1)
            ChooseTest()

        if choice - 1 in testidslist:
            Test(username, choice - 1)

        else:
            print("Please enter a valid option.")
            time.sleep(1)
            ChooseTest()

# Function for the test itself

def Test(username, testid):
