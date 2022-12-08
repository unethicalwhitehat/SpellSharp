# Importing the necessary modules

import base64
import getpass
import os
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


def ChooseOption(usertype, username="user"):
    if usertype == "S":
        print(f'''
        -------------------------------------------------------
        Welcome {username}, please select an option from below:
        -------------------------------------------------------
        1) Log in        
        2) Back
        -------------------------------------------------------
        ''')
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
            os.system('clear')
            StudentLogin()
        elif choice == 2:
            time.sleep(1)
            os.system('clear')
            return
        else:
            time.sleep(1)
            print("Please enter a valid option.")
            time.sleep(2)
            ChooseOption(usertype)
    elif usertype == "T":
        print(f'''
        --------------------------------------------------------
        Welcome, {username}. Please select an option from below:
        --------------------------------------------------------
        1) Log in        
        2) Sign up        
        3) Back
        --------------------------------------------------------
        ''')

        choice = input("Enter your choice: ")
        try:
            choice = int(choice)
        except ValueError:
            time.sleep(1)
            print("Please enter a number.")
            time.sleep(2)
            ChooseOption(usertype)
        if choice == 1:
            time.sleep(1)
            os.system('clear')
            TeacherLogin()
        elif choice == 2:
            time.sleep(1)
            os.system('clear')
            TeacherSignUp()
        elif choice == 3:
            time.sleep(1)
            os.system('clear')
            return
        else:
            time.sleep(1)
            print("Please enter a valid choice.")
            time.sleep(2)
            ChooseOption(usertype)
    else:
        print("Please enter a valid user type.")
        time.sleep(2)
        return


def EnterDob():
    dob = input("Please enter your date of birth (DD/MM/YYYY): ")
    try:
        dob = datetime.datetime.strptime(dob, "%d/%m/%Y")
        return dob
    except ValueError:
        print("Please make sure you enter the date in the correct format")
        EnterDob()


def EnterYearGroup():
    yeargroup = input("Enter the year group you're in (3, 4, 5 or 6)")
    try:
        year = int(yeargroup)
        if 3 > year > 6:
            print("Please ensure you have entered the correct year")
            EnterYearGroup()
        else:
            return year
    except ValueError:
        print("You must enter a number. Please try again")
        EnterYearGroup()


def CreatePassword(username):
    password = getpass.getpass("Enter password: ")
    special_char = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if (len(password) < 8) or (password == username) or (password.isalpha()) or (password.isnumeric()) or (
            special_char.search(password) is None):
        print(
            "Please enter a valid password. Your password must be at least 8 characters long, it cannot be your username, and must contain letters, numbers, and a symbol.")
        CreatePassword(username)
    else:
        return password


def TeacherSignUp():
    os.system('clear')
    fname = input("Please enter your first name: ")
    time.sleep(1)
    lname = input("Please enter your last name: ")
    time.sleep(1)
    username = f"{fname[0:1]}.{lname}{random.randint(0, 100)}".lower()
    dob = EnterDob()
    time.sleep(1)
    password = CreatePassword(username)
    time.sleep(1)
    salt = GenSalt()
    saltedpassword = password + salt
    saltedpassword = hashlib.sha256(password.encode()).hexdigest()
    dblogin.TeacherSignUp(fname, lname, dob, username, saltedpassword, salt)


def StudentSignUp():
    os.system('clear')
    fname = input("Enter your first name")
    time.sleep(1)
    lname = input("Enter your last name")
    time.sleep(1)
    username = f"{fname}.{lname}{random.randint(100, 1000)}".lower()
    dob = EnterDob()
    time.sleep(1)
    yeargroup = EnterYearGroup()
    time.sleep(1)
    teachername = input("Enter the last name of your teacher: ")
    time.sleep(1)
    password = CreatePassword(username)
    time.sleep(1)
    salt = GenSalt()
    saltedpassword = password + salt
    saltedpassword = hashlib.sha256(password.encode()).hexdigest()
    dblogin.StudentSignUp(fname, lname, dob, username, saltedpassword, salt, yeargroup, teachername)


def TeacherLogin(attempts=0):
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    dblogin.TeacherLogin(username, password, attempts)


def StudentLogin(attempts=0):
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    dblogin.StudentLogin(username, password, attempts)
