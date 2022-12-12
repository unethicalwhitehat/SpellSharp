# Module to handle connecting to the database and account functions.

# Importing the necessary modules and functions.

import sqlite3
import login_area
import teacher
import student
import time
import hashlib

# Connecting to the database.

conn = sqlite3.connect("spellsharp.db")

c = conn.cursor()

# Function to add a new teacher account to the teacheraccounts table

def TeacherSignUp(fname, lname, dob, username, saltedpassword, salt):

    c.execute("INSERT INTO teacheraccounts VALUES (?, ?, ?, ?, ?, ?)",
              (fname, lname, dob, username, saltedpassword, salt))
    print(f"Teacher account created successfully. Your username is {username}")
    time.sleep(3)
    conn.commit()
    teacher.TeacherMenu(fname, username)

# Function to add a new student account to the studentaccounts table

def StudentSignUp(fname, lname, dob, username, saltedpassword, salt, yeargroup, teachername):

    c.execute("INSERT INTO studentaccounts VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
              (fname, lname, dob, username, saltedpassword, salt, yeargroup, teachername))
    print(f"Student account created successfully. Your username is {username}")
    time.sleep(3)
    conn.commit()
    student.StudentMenu(fname, username)

# Function to handle a teacher logging in

def TeacherLogin(username, password, attempts=0):

    c.execute("SELECT salt FROM teacheraccounts WHERE username = ?", (username,))
    gatheredsalt = c.fetchall()

    try:
        gatheredsalt = str(gatheredsalt[0])
    except TypeError:
        time.sleep(1)
        print("Database error")
    except IndexError:
        time.sleep(1)
        print("User does not exist")
        time.sleep(2)
        login_area.ChooseOption("T")

    saltedpassword = password + gatheredsalt
    hashedpassword = hashlib.sha256(saltedpassword.encode('utf-8')).hexdigest()
    print(hashedpassword)
    if attempts < 3:
        c.execute("SELECT * FROM teacheraccounts WHERE username = ? AND hashedpassword = ?",
                  (username, hashedpassword))
        data = c.fetchall()
        print(data)
        try:
            data = str(data[0])
        except TypeError:
            print("Database error")
        except IndexError:
            print("User does not exist")
            time.sleep(2)
            login_area.ChooseOption("T")
        if data:
            print("Login successful.")
            c.execute("SELECT fname FROM studentaccounts WHERE username = ? AND hashedpassword = ?",
                       (username, hashedpassword))
            fname = c.fetchall()
            conn.close()
            teacher.TeacherMenu(fname, username)
        else:
            print(f"Login failed. {attempts+1}/3")
            attempts += 1
            login_area.TeacherLogin(attempts)
    else:
        print("Too many failed attempts")
        time.sleep(3)
        return


def StudentLogin(username, password, attempts=0):

    c.execute("SELECT salt FROM studentaccounts WHERE username = ?", (username,))
    gatheredsalt = c.fetchall()
    try:
        gatheredsalt = str(gatheredsalt[0])
    except TypeError:
        print("Database error")
    saltedpassword = password + gatheredsalt
    hashedpassword = hashlib.sha256(saltedpassword.encode('utf-8')).hexdigest()
    if attempts < 3:
        c.execute("SELECT * FROM studentaccounts WHERE username = ? AND hashedpassword = ?",
                   (username, hashedpassword))
        data = c.fetchall()
        data = str(data)
        if data:
            print("Login successful.")
            c.execute("SELECT fname FROM studentaccounts WHERE username = ? AND hashed = ?",
                       (username, hashedpassword))
            fname = c.fetchall()
            conn.close()
            student.StudentMenu(fname, username)
        else:
            print("Login failed.")
            attempts += 1
            login_area.StudentLogin(attempts)
    else:
        print("Too many failed attempts")
        exit()