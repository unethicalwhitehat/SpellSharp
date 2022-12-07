import sqlite3
import os
import loginarea
import datetime
import teacher
import student
import time
import hashlib

conn = sqlite3.connect("teacheraccounts.db")
conn2 = sqlite3.connect("studentaccounts.db")

c = conn.cursor()
c2 = conn2.cursor()

if os.path.exists("teacheraccounts.db"):
    pass
else:
    c.execute('''
    CREATE TABLE teacheraccounts
    (fname text), (lname text), (dob datetime), (username text), (password text), (salt text)''')

if os.path.exists("studentaccounts.db"):
    pass
else:
    c.execute('''
    CREATE TABLE studentaccounts
    (fname text), (lname text), (dob datetime), (username text), (password text), (salt text), (usertype text), (year text), (teacher text) ''')


def TeacherSignUp(fname, lname, dob, username, password, salt):
    c.execute("INSERT INTO teacheraccounts VALUES (?, ?, ?, ?, ?, ?)", (fname, lname, dob, username, password, salt))
    conn.commit()
    print("Teacher created successfully.")
    conn.close()
    TeacherLogin()


def StudentSignUp(fname, lname, dob, username, password, salt, year, teacher):
    c2.execute("INSERT INTO studentaccounts VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
               (fname, lname, dob, username, password, salt, year, teacher))
    conn.commit()
    print("Student account created successfully.")
    conn2.close()
    StudentLogin(username, password)


def TeacherLogin(username, password, attempts=0):
    c.execute("SELECT hash FROM teacheraccounts WHERE username = ?", username)
    gatheredhash = c.fetchall()
    saltedpassword = password + gatheredhash
    saltedpassword = hashlib.sha256(password.encode()).hexdigest()
    if attempts < 3:
        c.execute("SELECT * FROM teacheraccounts WHERE username = ? AND password = ?", (username, saltedpassword))
        data = c.fetchall()
        if data:
            print("Login successful.")
            conn.close()
            teacher.TeacherMenu()
        else:
            print("Login failed.")
            attempts += 1
            loginarea.TeacherLogin()
    else:
        print("Too many failed attempts")
        exit()


def StudentLogin(username, password, attempts=0):
    c2.execute("SELECT hash FROM studentaccounts WHERE username = ?", username)
    gatheredhash = c2.fetchall()
    saltedpassword = password + gatheredhash
    saltedpassword = hashlib.sha256(password.encode()).hexdigest()
    if attempts < 3:
        c2.execute("SELECT * FROM studentaccounts WHERE username = ? AND password = ?", username, saltedpassword)
        data = c2.fetchall()
        if data:
            print("Login successful.")
            conn2.close()
            student.StudentMenu()
        else:
            print("Login failed.")
            attempts += 1
            loginarea.StudentLogin()
    else:
        print("Too many failed attempts")
        exit()
