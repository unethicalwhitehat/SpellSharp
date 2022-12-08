import sqlite3
import loginarea
import teacher
import student
import time
import hashlib

conn = sqlite3.connect("teacheraccounts.db")
conn2 = sqlite3.connect("studentaccounts.db")

c = conn.cursor()
c2 = conn2.cursor()


def TeacherSignUp(fname, lname, dob, username, saltedpassword, salt):
    c.execute("INSERT INTO teacheraccounts VALUES (?, ?, ?, ?, ?, ?)", (fname, lname, dob, username, saltedpassword, salt))
    print(f"Teacher account created successfully. Your username is {username}")
    time.sleep(3)
    conn.commit()
    teacher.TeacherMenu(username)


def StudentSignUp(fname, lname, dob, username, saltedpassword, salt, yeargroup, teachername):
    c2.execute("INSERT INTO studentaccounts VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (fname, lname, dob, username, saltedpassword, salt, yeargroup, teachername))
    print(f"Student account created successfully. Your username is {username}")
    time.sleep(3)
    conn2.commit()
    student.StudentMenu(username)


def TeacherLogin(username, password, attempts=0):
    c.execute("SELECT salt FROM teacheraccounts WHERE username = ?", (username,))
    gatheredsalt = c.fetchall()
    try:
        gatheredsalt = str(gatheredsalt[0])
    except TypeError:
        print("Database error")
    saltedpassword = password + gatheredsalt
    saltedpassword = hashlib.sha256(saltedpassword.encode()).hexdigest()
    if attempts < 3:
        c.execute("SELECT * FROM teacheraccounts WHERE username = ? AND saltedpassword = ?", (username, saltedpassword))
        data = c.fetchall()
        try:
            data = str(data[0])
        except TypeError:
            print("Database error")
        if data:
            print("Login successful.")
            conn.close()
            time.sleep(3)
            teacher.TeacherMenu(username)
        else:
            print(f"Login failed. {attempts+1}/3")
            attempts += 1
            loginarea.TeacherLogin(attempts)
    else:
        print("Too many failed attempts")
        time.sleep(3)
        return


def StudentLogin(username, password, attempts=0):
    c2.execute("SELECT salt FROM studentaccounts WHERE username = ?", (username,))
    gatheredsalt = c2.fetchall()
    try:
        gatheredsalt = str(gatheredsalt[0])
    except TypeError:
        print("Database error")
    saltedpassword = password + gatheredsalt
    saltedpassword = hashlib.sha256(password.encode()).hexdigest()
    if attempts < 3:
        c2.execute("SELECT * FROM studentaccounts WHERE username = ? AND saltedpassword = ?", (username, saltedpassword))
        data = c2.fetchall()
        data = str(data)
        if data:
            print("Login successful.")
            c2.execute("SELECT fname FROM studentaccounts WHERE username = ? AND saltedpassword = ?", (username, saltedpassword))
            fname = c2.fetchall()
            conn2.close()
            student.StudentMenu(fname)
        else:
            print("Login failed.")
            attempts += 1
            loginarea.StudentLogin(attempts)
    else:
        print("Too many failed attempts")
        exit()
