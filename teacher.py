import loginarea
import os
import time

def TeacherMenu(username):
    os.system('clear')
    print(f'''
    -------------------------------------------------------
    Welcome {username}, please select an option from below:
    -------------------------------------------------------
    1) Set up a test
    2) View results
    3) Settings
    4) Student account management
    5) Log out
    -------------------------------------------------------
    ''')
    def ChooseOption():
        choice = input("Please enter your option: ")
        if option == "1":
            time.sleep(1)
            CreateTest()
        elif option == "2":
            time.sleep(1)
            ViewResults()
        elif option == "3":
            Settings()
        elif option == "4":
            StudentAccountManagement()
        elif option == "5":
            loginarea.TeacherLogin()
        else:
            print("Please enter a valid option.")
            ChooseOption()
    ChooseOption()

def CreateTest():
    os.system('clear')

    # Set up test gives option to create a test or edit an existing test (if there is one)

    # View options shows scores table with options to filter

    # Settings allows you to change your password

    # Student account management allows you to add, remove or edit students and view their scores

    # Log out logs you out and returns to the main menu