import loginarea


def StudentMenu(username):
    print(f'''
    Welcome {username}, please select an option from below:
    
    ----------------------------------------------------
    
    1) Take a test
    2) View results
    3) Log out
    
    ----------------------------------------------------\n
    ''')
    option = input("Please enter your option: ")
    if option == "1":
        # TakeTest()
        print("Test")
    elif option == "2":
        # ViewResults()
        print("Results")
    elif option == "3":
        login.Login()
    else:
        print("Please enter a valid option.")
        StudentMenu()
