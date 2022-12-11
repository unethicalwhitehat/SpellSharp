# Student menu

# Importing the necessary modules and functions.

import time
import login_area
import student_testing
import student_results

# Function to show the student menu and take an input to proceed.

def StudentMenu(fname, username):

    print(f'''
    ----------------------------------------------------
    Welcome {fname}, please select an option from below:
    ----------------------------------------------------
    1) Testing
    2) Results
    3) Log out
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

        if choice == "1":
            student_testing.Menu(fname, username)
        elif choice == "2":
            student_results.Menu(fname, username)
        elif choice == "3":
            login_area.StudentLogin()
        else:
            print("Please enter a valid option.")
            time.sleep(1)
            ChooseOption()