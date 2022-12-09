import loginarea
import os
import time

import teacher_testing
import teacher_viewresults
import teacher_settings
import teacher_studentaccountmanagement

def TeacherMenu(fname, username):
    os.system('clear')
    print(f'''
    -------------------------------------------------------
    Welcome {fname}, please select an option from below:
    -------------------------------------------------------
    1) Testing
    2) View results
    3) Settings
    4) Student account management
    5) Log out
    -------------------------------------------------------
    ''')

    def ChooseOption():
        choice = input("Please enter an option: ")
        try:
            choice = int(choice)
        except ValueError:
            time.sleep(1)
            print("Please enter a number")
            time.sleep(2)
            ChooseOption()
        if choice == 1:
            time.sleep(1)
            teacher_testing.Menu(fname, username)
        elif choice == 2:
            time.sleep(1)
            teacher_viewresults.Menu(fname, username)
        elif choice == 3:
            time.sleep(1)
            teacher_settings.Menu(fname, username)
        elif choice == 4:
            time.sleep(1)
            teacher_studentaccountmanagement.Menu(fname, username)
        elif choice == 5:
            time.sleep(1)
            return
        else:
            time.sleep(1)
            print("Please enter a valid option.")
            time.sleep(2)
            ChooseOption()

    ChooseOption()











    # Set up test gives option to create a test or edit an existing test (if there is one)

    # View options shows scores table with options to filter

    # Settings allows you to change your password

    # Student account management allows you to add, remove or edit students and view their scores

    # Log out logs you out and returns to the main menu
