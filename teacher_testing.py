# Function for the teacher to create and assign tests.

# Importing the necessary modules and functions.

import time
from clear_screen import ClearScreen
import sqlite3

# Function for the menu.

def Menu(fname):
    ClearScreen()
    print(f'''
    ----------------------------------------------------------------------------------------
    Welcome to the testing and vocabulary menu, {fname}. Please select an option from below:
    ----------------------------------------------------------------------------------------
    1) Create a new test
    2) Re-assign an old test
    3) View old tests
    4) Add vocabulary
    5) Go back
    ----------------------------------------------------------------------------------------
    ''')

    def ChooseOption():

        choice = input("> ")

        try:
            choice = int(choice)
        except ValueError:
            print("Please enter a number")
            time.sleep(1)
            ChooseOption()

        if choice == 1:
            CreateNewTest()
        elif choice == 2:
            # ReassignOldTest()
            return
        elif choice == 3:
            # ViewOldTests()
            return
        elif choice == 4:
            # AddVocabulary()
            return
        elif choice == 5:
            return
        else:
            print("Please select a valid option")
            time.sleep(1)
            ChooseOption()

    ChooseOption()

def CreateNewTest():

    ClearScreen()

    print(f'''
    ----------------------------------------------------------------------------
    How would you like to create a new test? Please select an option from below:
    ----------------------------------------------------------------------------
    1) Add new words and definitions
    2) Randomly generate words and definitions from the internet (experimental)
    3) Reuse old words and definitions from the database
    4) Go back
    ----------------------------------------------------------------------------
    ''')

    def ChooseOption():

        choice = input("> ")

        try:
            choice = int(choice)
        except ValueError:
            print("Please enter a number")
            time.sleep(1)
            ChooseOption()

        if choice == 1:
            CreateNewTest_Manually()
        elif choice == 2:
            # CreateNewTest_Internet()
            return
        elif choice == 3:
            # CreateNewTest_Database()
            return
        elif choice == 4:
            return
        else:
            print("Please select a valid option")

    ChooseOption()

def CreateNewTest_Manually():
    
        ClearScreen()
    
        print(f'''
        -------------------------------------------------------------
        Please enter the number of words you would like to add below:
        -------------------------------------------------------------
        ''')
    
        def ChooseOption():
    
            choice = input("> ")
    
            try:
                choice = int(choice)
            except ValueError:
                print("Please enter a number")
                time.sleep(1)
                ChooseOption()
    
            if choice > 0:
                AddWords(choice)
            else:
                print("Please enter a number greater than 0")
                time.sleep(1)
                ChooseOption()
    
        ChooseOption()

def AddWords(num):
    
    ClearScreen()

    words = []
    definitions = []

    for i in range(num):
        print('''
        -----
        Word:
        -----
        ''')

        word = input("> ")
        words.append(word)

        print('''
        -----------
        Definition:
        -----------
        ''')

        definition = input("> ")
        definitions.append(definition)

    ClearScreen()
    print('''
    -------------------------------
    You have entered the following:
    -------------------------------
    ''')

    for i in range(num):
        print(f"{words[i]}: {definitions[i]}")

    print('''\n
    -------------------------------
    ''')

    choice = input("Would you like to save this test and add the wordds to the database? (y/n)\n> ")

    if choice.lower() == "y":
        AddManuallyToDatabase(words, definitions)
        print("\nTest saved.")
        time.sleep(1)
        return
    elif choice.lower() == "n":
        print("\nTest not saved.")
        time.sleep(1)
        return

def AddManuallyToDatabase(words, definitions):
    
    conn = sqlite3.connect("spellsharp.db")
    c = conn.cursor()

    for i in range(len(words)):
        c.execute("INSERT INTO spellings VALUES (:word, :definition)", {"word": words[i], "definition": definitions[i]})

    c.execute("SELECT * FROM spellings WHERE integer = cursor.lastrowid")
    print(c.fetchall())

    conn.commit()
    conn.close()


# def CreateNewTest_Internet():


# def CreateNewTest_Database():