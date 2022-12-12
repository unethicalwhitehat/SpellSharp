# First main menu where first time checks and setup are done, and the user selects their role to proceed.

# Importing the necessary modules and functions.

import login_area
from time import sleep
from first_time_run import CheckIfFirstTimeRunning
from first_time_setup import FirstTimeSetup
from clear_screen import ClearScreen
import sqlite3


# Function to perform first time checks and to show the main menu and take an input to proceed.

def MainMenu():
    ClearScreen()

    if CheckIfFirstTimeRunning():
        FirstTimeSetup()

    print('''
    ----------------------------------------------------------
    Welcome to SpellSharp. Please select an option from below:    
    ----------------------------------------------------------
    1) I'm a student   
    2) I'm a teacher
    3) Exit program
    ----------------------------------------------------------
    ''')

    def ChooseOption():

        choice = input("> ")

        try:
            choice = int(choice)
        except ValueError:
            print("Please enter a number.")
            sleep(1)
            ChooseOption()

        if choice == 1:
            ClearScreen()
            login_area.LoginMenu("S")
        elif choice == 2:
            ClearScreen()
            login_area.LoginMenu("T")
        # elif choice == 3:
        #     conn = sqlite3.connect("test.db")
        #     c = conn.cursor()
        #     try:
        #         c.execute("""
        #         CREATE TABLE test (
        #         ID integer PRIMARY KEY AUTOINCREMENT,
        #         test text
        #         )""")
        #     except sqlite3.OperationalError as ex:
        #         print("Error creating table: " + str(ex))
        #         pass
        #     conn.commit()
        #
        #     # q: If I want the ID to increment automatically what do I pass into the ID column?
        #
        #
        #     # q: I'm getting an error because a value has not been added to the ID column. How do I fix this?
        #
        #     # a: You can use the AUTOINCREMENT keyword. This will automatically increment the ID by 1 each time a new entry is added.
        #
        #     # q: Right, but when I want to insert a new value into the ID column that increments automatically how do I do that?
        #
        #     # a: You can use the NULL keyword. This will automatically increment the ID by 1 each time a new entry is added.
        #
        #     # q: Thanks, that's done it
        #
        #     # a: No problem, glad I could help.
        #
        #
        #     for i in range (10):
        #
        #         try:
        #             c.execute("INSERT INTO test VALUES (null, 'archie brownsword')")
        #             conn.commit()
        #         except sqlite3.OperationalError as ex:
        #             print("Error inserting into table: " + str(ex))
        #             pass
        #         try:
        #             c.execute("SELECT * FROM test")
        #             print(c.fetchall())
        #         except sqlite3.OperationalError as ex:
        #             print("Error selecting from table: " + str(ex))
        #             pass
        #
        #     conn.close()
        elif choice == 3:
            print("Goodbye.")
            sleep(3)
            ClearScreen()
            exit()
        else:
            print("Please enter a valid choice.")
            sleep(1)
            ChooseOption()

    ChooseOption()


MainMenu()


# q: Hey, can you help?

# a: Sure, what's up?

# q: Basically on line 55 I'm doing integer PRIMARY KEY AUTOINCREMENT so each entry has a unique ID, are you following so far?

# a: Yeah, I'm following.

# q: Problem is, I'm getting this error: Error creating table: AUTOINCREMENT is only allowed on an INTEGER PRIMARY KEY

# a: Oh, I see. I think I know what the problem is.

# q: What is it?

# a: I think you're trying to create a table with a column called integer, and then you're trying to make that column the primary key.

# q: Is that not allowed?

# a: No, it's not. You can't have a column called integer.

# q: What should I do?

# a: You can use any other name you want. For example, you could use the name "id".

# q: Yesterday you said I could. What gives?

# a: I said you could use any name you want, but you can't use the name "integer".

# q: Yeah, but you said it was called integer and that I could refer to it as such. That very code was something you suggested.

# a: I did? I don't remember that.

# q: Yeah, you did. You said I could use the name "integer" and refer to it as such.

# a: I don't remember that. I don't think I said that.

# q: You definitely did, I can show you what you said if you want?

# a: No, I don't think I said that. I don't think I said you could use the name "integer".

# q: Okay well let me tell you exactly what you said.

# a: Okay.

# q: You said: "a: Yes, it's called "integer". You can use this to refer to the ID in other functions."

# a: Oh, I see. I think I know what the problem is.

# q: Yeah, it's you and your misinformation.

# a: I don't think I said that.
