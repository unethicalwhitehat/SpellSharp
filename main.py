# First main menu where first time checks and setup are done, and the user selects their role to proceed.

# Importing the necessary modules and functions.

import login_area # To allow the user to sign up and log in
import time # For delays.
import first_time_setup as fts # For first time setup.
import first_time_run as ftr # For first time run checks.
from clear_screen import ClearScreen # For clearing the screen.


# Function to perform first time checks and to show the main menu and take an input to proceed.

def MainMenu():
    
    ClearScreen()
    
    if ftr.CheckIfFirstTimeRunning() == True:
        fts.FirstTimeSetup()
    
    print('''
    ------------------------------------------------------
    Welcome to Spellr. Please select an option from below:    
    ------------------------------------------------------ 
    1) I'm a student   
    2) I'm a teacher
    3) Exit program    
    ------------------------------------------------------
    ''')

    def ChooseOption():
        
        choice = input("\n> ")
        
        try:
            choice = int(choice)
        
        except ValueError:
            print("Please enter a number")
            ChooseOption()
        
        if choice == 1:
            time.sleep(1)
            ClearScreen()
            login_area.ChooseOption("S")
        
        elif choice == 2:
            time.sleep(1)
            ClearScreen()
            login_area.ChooseOption("T")
        
        elif choice == 3:
            time.sleep(1)
            print("Goodbye")
            time.sleep(5)
            ClearScreen()
            exit()
        
        else:
            time.sleep(1)
            print("Please enter a valid choice.")
            time.sleep(3)
            ClearScreen()
            MainMenu()

    ChooseOption()

MainMenu()