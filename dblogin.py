import sqlite3
import os
import loginarea
import hashlib
import datetime

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


def StudentSignUp(fname, lname, dob, username, password, salt, usertype, year, teacher):
    c2.execute("INSERT INTO studentaccounts VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
               (fname, lname, dob, username, password, salt, usertype, year, teacher))
    conn.commit()
    print("Student account created successfully.")
    conn2.close()
    StudentLogin(username, password)


def TeacherLogin(username, password, attempts=0):
    if attempts < 3:
        c.execute("SELECT * FROM teacheraccounts WHERE username = ? AND password = ?", (username, password))
        data = c.fetchall()
        if data:
            print("Login successful.")
            conn.close()
            loginarea.TeacherMenu()
        else:
            print("Login failed.")
            attempts += 1
            conn.close()
            loginarea.Login(usertype)

# def StudentLogin(username, password):
#     c.execute("SELECT * FROM accounts WHERE uname = ? AND password = ?", (username, password))
#     data = c.fetchall()
#     if data:
#         print("Login successful.")
#         if usertype == "S":
#             student.StudentMenu()
#         elif usertype == "T":
#             teacher.TeacherMenu()
#     else:
#         print("Login failed.")
