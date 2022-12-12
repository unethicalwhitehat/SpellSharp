# Module to handle the login and sign up areas of the program.

# Importing the necessary modules and functions.

import base64
from getpass import getpass
import hashlib
import os
import db_login
import re
import random
from datetime import datetime
from time import sleep
from clear_screen import ClearScreen

# Function to show the options for the users based on their type and to take an input to proceed.

def LoginMenu(usertype):

    if usertype == "S":

        print('''
        ----------------------------------------------------
        Welcome student, please select an option from below:
        ----------------------------------------------------
        1) Log in        
        2) Back
        ----------------------------------------------------
        ''')

        def StudentChooseOption():

            choice = input("> ")

            try:
                choice = int(choice)
            except ValueError:
                print("Please enter a number.")
                sleep(1)
                StudentChooseOption()

            if choice == 1:
                ClearScreen()
                StudentLogin()
            elif choice == 2:
                ClearScreen()
                return
            else:
                print("Please enter a valid choice.")
                sleep(2)
                StudentChooseOption(usertype)

        StudentChooseOption()

    elif usertype == "T":

        print(f'''
        -----------------------------------------------------
        Welcome, teacher. Please select an option from below:
        -----------------------------------------------------
        1) Log in        
        2) Sign up        
        3) Back
        -----------------------------------------------------
        ''')

        def TeacherChooseOption():

            choice = input("> ")

            try:
                choice = int(choice)
            except ValueError:
                print("Please enter a number.")
                sleep(1)
                TeacherChooseOption()

            if choice == 1:
                ClearScreen()
                TeacherLogin()
            elif choice == 2:
                ClearScreen()
                TeacherSignUp()
            elif choice == 3:
                ClearScreen()
                return
            else:
                print("Please enter a valid choice.")
                sleep(1)
                TeacherChooseOption()

        TeacherChooseOption()

    else:
        print("Please enter a valid user type.")
        sleep(1)
        return

# Function to handle taking a date of birth and checking it is valid, it also turns it into a datetime object.

def EnterDob():

    dob = input("Please enter your date of birth (DD/MM/YYYY).\n> ")

    try:
        dob = datetime.strptime(dob, "%d/%m/%Y")
        return dob
    except ValueError:
        print("Please make sure you enter the date in the correct format.")
        EnterDob()

# Function to handle taking the year group and ensuring it is valid (may be changed so students can enter different year groups depending on their school).

def EnterYearGroup():

    yeargroup = input(
        "Please enter the year group you're in (3, 4, 5 or 6).\n> ")

    try:
        year = int(yeargroup)
        if 3 > year > 6:
            print("Please ensure you have entered the correct year group.")
            EnterYearGroup()
        else:
            return year
    except ValueError:
        print("You must enter a number. Please try again.")
        EnterYearGroup()

# Function to handle taking a password and checking it is valid, it returns the password if it is valid.

def CreatePassword(username):
    password = getpass("Please choose a password:\n> ")
    special_char = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if (len(password) < 8) or (password == username) or (password.isalpha()) or (password.isnumeric()) or (
            special_char.search(password) is None):
        print(
            "Please enter a valid password. Your password must be at least 8 characters long, it cannot be your username, and must contain a letter, a number, and a symbol.")
        CreatePassword(username)
    else:
        return password

# Function to handle a teacher signing up.

def TeacherSignUp():
    os.system('clear')
    fname = input("Please enter your first name:\n> ")
    sleep(1)
    lname = input("Please enter your last name:\n> ")
    sleep(1)
    username = f"{fname[0:1]}.{lname}{random.randint(0, 100)}".lower()
    dob = EnterDob()
    sleep(1)
    password = CreatePassword(username)
    sleep(1)
    salt = GenSalt()
    saltedpassword = password + salt
    saltedpassword = hashlib.sha256(saltedpassword.encode()).hexdigest()
    db_login.TeacherSignUp(fname, lname, dob, username, saltedpassword, salt)

# Function to handle a student signing up.

def StudentSignUp():
    os.system('clear')
    fname = input("Please enter your first name:\n> ")
    sleep(1)
    lname = input("Please enter your last name:\n> ")
    sleep(1)
    username = f"{fname}.{lname}{random.randint(100, 1000)}".lower()
    dob = EnterDob()
    sleep(1)
    yeargroup = EnterYearGroup()
    sleep(1)
    teachername = input("Please enter the last name of your teacher:\n> ")
    teachername = teachername.lower()
    teachername[0] = teachername[0].upper()
    sleep(1)
    password = CreatePassword(username)
    sleep(1)
    salt = GenSalt()
    saltedpassword = password + salt
    saltedpassword = hashlib.sha256(saltedpassword.encode()).hexdigest()
    db_login.StudentSignUp(fname, lname, dob, username,
                          saltedpassword, salt, yeargroup, teachername)

# Function to handle a teacher logging in

def TeacherLogin(attempts=0):
    username = input("Please enter your username:\n> ")
    password = getpass("Please your password:\n> ")
    db_login.TeacherLogin(username, password, attempts)

# Function to handle a student logging in

def StudentLogin(attempts=0):
    username = input("Please enter your username:\n> ")
    password = getpass("Enter your password:\n> ")
    db_login.StudentLogin(username, password, attempts)

# Function to generate the salt for the password

def GenSalt():
    salt = base64.b64encode(os.urandom(32)).decode('utf-8')
    return salt