import base64
import getpass
import os
import main
import teacher
import student
import hashlib
import dblogin
import re
import random
import datetime


def GenSalt():
    salt = os.urandom(32)
    salt = base64.b64encode(salt).decode('utf-8')
    return salt


# Pepper as well?

def ChooseOption(usertype):
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
            ChooseOption(usertype)
        if choice == 1:
            StudentLogin()
        elif choice == 2:
            main.MainMenu()
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
            ChooseOption(usertype)
        if choice == 1:
            TeacherLogin()
        elif choice == 2:
            StudentSignUp()
        elif choice == 3:
            main.MainMenu()
        else:
            print("Please enter a valid choice.")
            ChooseOption(usertype)
    else:
        print("Please enter a valid user type.")
        main.ChooseOption()


def EnterDob():
    dob = input("Please enter your date of birth (DD/MM/YYYY): ")
    try:
        dob = datetime.datetime.strptime(dob, "%d/%m/%Y")
        return dob
    except:
        print("Please make sure you enter the date in the correct format")
        EnterDob()


def TeacherSignUp():
    fname = input("Please enter your first name: ")
    lname = input("Please enter your last name: ")
    username = f"{fname[0:1]}.{lname}{random.randint(0, 100)}".lower()
    dob = EnterDob()
    password = getpass.getpass("Enter password: ")
    special_char = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if (len(password) < 8) or (password == username) or (password.isalpha()) or (password.isnumeric()) or (
            special_char.search(password) is None):
        print(
            "Please enter a valid password. Your password must be at least 8 characters long, it cannot be your username, and must contain letters, numbers, and a symbol.")
        ChooseOption("T")
    else:
        salt = GenSalt()
        password.append(salt)
        password = hashlib.sha256(password.encode()).hexdigest()
        dblogin.TeacherSignUp(fname, lname, dob, username, password, salt)
    # username = input("Choose username: ")
    # if usertype == "S":
    #     year = input("Enter year group: ")
    #     teacher = input("Enter teacher's username: ")
    # password = getpass.getpass("Choose password: ")
    # special_char = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    # if (len(password) < 8) or (password == username) or (password is alpha) or (password is numeric) or (special_char.search(password) is None):
    #     print("Please enter a valid password. Your password must be at least 8 characters long, it cannot be your username, and must contain letters, numbers, and a symbol.")
    #     SignUp(usertype)
    # else:
    #     password.append(salt)
    #     password = hashlib.sha256(password.encode()).hexdigest()
    #     if usertype == "S":
    #         dblogin.StudentSignUp(username, password, salt, usertype, year, teacher)
    #     elif usertype == "T":
    #         dblogin.TeacherSignUp(username, password, salt, usertype)
    # fname = input("Enter first name: ")
    # lname = input("Enter last name: ")
    # username = fname[0] + lname + random.randint(100, 1000)


def StudentSignUp():
    fname = input("Enter your first name")
    lname = input("Enter your last name")
    username = f"{fname}.{lname}{random.randint(100, 1000)}".lower()


def TeacherLogin():
    print("Teacher login")


def StudentLogin():
    print("Student login")

# def LogIn():
#     username = input("Enter username: ")
#     password = getpass.getpass("Enter password: ")
#     password = hashlib.sha256(password.encode()).hexdigest()
#     dblogin.LogIn(username, password)
#
# if action == "login":
#     LogIn()
# elif action == "signup":
#     SignUp(usertype)
# else:
#     print("Please enter a valid action.")
#     Login(usertype)
