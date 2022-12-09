import time
import os


def Menu(fname):
    os.system('clear')
    print(f'''
    -------------------------------------------------------------------------
    Welcome to the testing menu, {fname}. Please select an option from below:
    -------------------------------------------------------------------------
    1) Create a new test
    2) Re-assign an old test
    3) View old tests
    4) Add vocabulary
    5) Go back
    -------------------------------------------------------------------------
    ''')

    def ChooseOption():
        time.sleep(1)
        choice = input("Please enter your choice: ")
        try:
            choice = int(choice)
        except ValueError:
            time.sleep(1)
            print("Please enter a number")
            time.sleep(2)
            ChooseOption()
        if choice == 1:
            time.sleep(1)
            CreateNewTest()
        elif choice == 2:
            time.sleep(1)
            ReassignOldTest()
        elif choice == 3:
            time.sleep(1)
            ViewOldTests()
        elif choice == 4:
            time.sleep(1)
            AddVocabulary()
        elif choice == 5:
            time.sleep(1)
            return
        else:
            print("Please select a valid option")
