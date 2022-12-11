# First main menu where first time checks and setup are done, and the user selects their role to proceed.

# Importing the necessary modules and functions.

import login_area
from time import sleep
from first_time_run import CheckIfFirstTimeRunning
from first_time_setup import FirstTimeSetup
from clear_screen import ClearScreen

# Function to perform first time checks and to show the main menu and take an input to proceed.

def MainMenu():

    ClearScreen()

    if CheckIfFirstTimeRunning() == True:
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