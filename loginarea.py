import getpass
import teacher
import student
import hashlib
import json


def Login(usertype):
    if usertype == "S":
        print('''
        Welcome student, please select an option from below:
        ----------------------------------------------------
        1) Log in        
        2) Exit
        ----------------------------------------------------
        ''')

        choice = input("Enter your choice: ")
        try:
            choice = int(choice)
        except ValueError:
            print("Please enter a number.")
            Login(usertype)
        if choice == 1:
            EnterCreds("S")
        elif choice == 2:
            exit()
    elif usertype == "T":
        print('''
        Welcome, teacher. Please select an option from below:
        -----------------------------------------------------
        1) Log in        
        2) Sign up        
        3) Exit
        -----------------------------------------------------
        ''')

        choice = input("Enter your choice: ")
        try:
            choice = int(choice)
        except ValueError:
            print("Please enter a number.")
            Login(usertype)
        if choice == 1:
            EnterCreds("T")
        elif choice == 2:
            SignUp(usertype)
        elif choice == 3:
            exit()
        else:
            print("Please enter a valid choice.")
            Login(usertype)
    else:
        print("Please enter a valid user type.")
        exit()


def EnterCreds(usertype):
    with open("creds.txt", "r+") as file:
        creds = file.read()
        username = input("Enter username: ")
        if username in creds:
            password = getpass.getpass("Enter password: ")
            password = hashlib.sha256(password.encode()).hexdigest()
            if password in creds:
                if usertype == "S":
                    student.StudentMenu(username)
                elif usertype == "T":
                    teacher.TeacherMenu(username)
                else:
                    print("Please enter a valid user type.")
                    Login()
            else:
                print("Incorrect password.")
                Login()
        else:
            if usertype == "T":
                print("Username not found. Please make sure it is correct, or sign up in the previous menu.")
                Login(usertype)
            else:
                print("Your username was not found in the system. Please make sure you have entered it correctly or "
                      "ask your teacher to create an account for you.")


def SignUp(usertype):
    # Go through the text file to see if the username already exists. If it does, tell the user. If not,
    # take a password, encrypt it and add it to the file alongside the username and a unique ID
    username = input("Enter a username")
    with open ("creds.txt", "a+") as file:
        if username in



