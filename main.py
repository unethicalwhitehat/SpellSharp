# Main Menu to select options

# Import modules

import loginarea
import os


def MainMenu():
    print('''
    Welcome to the spelling test system. Please select an option from below:    
    -----------------------------------------------------------------------   
    1) I'm a student   
    2) I'm a teacher
    3) Exit    
    -----------------------------------------------------------------------
    ''')

    def ChooseOption():
        choice = input("Enter your choice: ")
        try:
            choice = int(choice)
        except ValueError:
            print("Please enter a number.")
            ChooseOption()
        if choice == 1:
            loginarea.Login("S")
        elif choice == 2:
            loginarea.Login("T")
        elif choice == 3:
            exit()
        else:
            print("Please enter a valid choice.")
    os.system('clear')
    ChooseOption()


MainMenu()
