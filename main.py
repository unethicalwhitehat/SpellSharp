# Main Menu to select options

# Import modules

import loginarea
import os
import time
import fts


# Function for the main menu
def MainMenu():
    os.system('clear')
    print('''
    ------------------------------------------------------------------------
    Welcome to the spelling test system. Please select an option from below:    
    ------------------------------------------------------------------------   
    1) I'm a student   
    2) I'm a teacher
    3) Exit program    
    -----------------------------------------------------------------------
    ''')

    # Function to choose an option

    def ChooseOption():
        choice = input("Enter your choice: ")
        try:
            choice = int(choice)
        except ValueError:
            print("Please enter a number")
            ChooseOption()
        if choice == 1:
            time.sleep(1)
            os.system('clear')
            loginarea.ChooseOption("S")
        elif choice == 2:
            time.sleep(1)
            os.system('clear')
            loginarea.ChooseOption("T")
        elif choice == 3:
            time.sleep(1)
            print("Goodbye")
            time.sleep(5)
            os.system('clear')
            exit()
        elif choice == 4:
            print("Running first time setup...")
            time.sleep(1)
            fts.FirstTimeSetup()
            MainMenu()
        else:
            time.sleep(1)
            print("Please enter a valid choice.")

    # os.system('clear')
    ChooseOption()


MainMenu()
