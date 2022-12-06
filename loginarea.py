# Importing the necessary modules

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
import time


# Function to generate the salt for the password

def GenSalt():
    salt = os.urandom(32)
    salt = base64.b64encode(salt).decode('utf-8')
    return salt


def ChooseOption(usertype):
    if usertype == "S":
        print('''
        Welcome student, please select an option from below:
        ----------------------------------------------------
        1) Log in        
        2) Exit
        ----------------------------------------------------
        ''')
        time.sleep(1)
        choice = input("Enter your choice: ")
        time.sleep(1)
        try:
            choice = int(choice)
        except ValueError:
            time.sleep(1)
            print("Please enter a number.")
            time.sleep(2)
            ChooseOption(usertype)
        if choice == 1:
            time.sleep(1)
            StudentLogin()
        elif choice == 2:
            time.sleep(1)
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
            TeacherSignUp()
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


def EnterYear():
    year = input("Enter the year group you're in (3, 4, 5 or 6)")
    try:
        year = int(year)
        if 3 > year > 6:
            print("Please ensure you have entered the correct year")
            EnterYear()
        else:
            return year
    except ValueError:
        print("You must enter a number. Please try again")
        EnterYear()


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
        print(f"Sign up successful. Your username is {username}")


def StudentSignUp():
    fname = input("Enter your first name")
    lname = input("Enter your last name")
    dob = EnterDob()
    year = EnterYear()
    teacher = input("Enter the last name of your teacher: ")
    username = f"{fname}.{lname}{random.randint(100, 1000)}".lower()
    password = getpass.getpass("Choose a password")
    special_char = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if (len(password) < 8) or (password == username) or (password.isalpha()) or (password.isnumeric()) or (
            special_char.search(password) is None):
        print(
            "Please enter a valid password. Your password must be at least 8 characters long, it cannot be your "
            "username, and must contain letters, numbers, and a symbol.")
        StudentSignUp()
    else:
        salt = GenSalt()
        password.append(salt)
        password = hashlib.sha256(password.encode()).hexdigest()
        dblogin.StudentSignUp(fname, lname, dob, username, password, salt, year, teacher)
        print(f"Sign up successful. Your username is {username}")
        time.sleep(3)
        print("Taking you go the login page...")
        time.sleep(2)
        StudentLogin()


def TeacherLogin():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    dblogin.TeacherLogin(username, password)


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
