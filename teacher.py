import login_area
import os
import time
import teacher_testing
import teacher_viewresults
import teacher_settings
import teacher_studentaccountmanagement
from clear_screen import ClearScreen

def TeacherMenu(fname, username):

    ClearScreen()

    print(f'''
    -------------------------------------------------------
    Welcome {fname}, please select an option from below:
    -------------------------------------------------------
    1) Testing and word management
    2) View results
    3) Settings
    4) Student account management
    5) Log out
    -------------------------------------------------------
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
            ClearScreen()
            teacher_testing.Menu(fname, username)
        elif choice == 2:
            ClearScreen()
            teacher_viewresults.Menu(fname, username)
        elif choice == 3:
            ClearScreen()
            teacher_settings.Menu(fname, username)
        elif choice == 4:
            ClearScreen()
            teacher_studentaccountmanagement.Menu(fname, username)
        elif choice == 5:
            ClearScreen()
            login_area.TeacherLogin()
        else:
            print("Please enter a valid option.")
            time.sleep(1)
            ChooseOption()

    ChooseOption()