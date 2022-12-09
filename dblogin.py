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
    teacher.TeacherMenu(fname, username)


def StudentSignUp(fname, lname, dob, username, saltedpassword, salt, yeargroup, teachername):
    c2.execute("INSERT INTO studentaccounts VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (fname, lname, dob, username, saltedpassword, salt, yeargroup, teachername))
    print(f"Student account created successfully. Your username is {username}")
    time.sleep(3)
    conn2.commit()
    student.StudentMenu(fname)


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
        loginarea.ChooseOption("T")
    saltedpassword = password + gatheredsalt
    hashedpassword = hashlib.sha256(saltedpassword.encode('utf-8')).hexdigest()
    print(hashedpassword)
    if attempts < 3:
        c.execute("SELECT * FROM teacheraccounts WHERE username = ? AND hashedpassword = ?", (username, hashedpassword))
        data = c.fetchall()
        print(data)
        try:
            data = str(data[0])
        except TypeError:
            print("Database error")
        except IndexError:
            print("User does not exist")
            time.sleep(2)
            loginarea.ChooseOption("T")
        if data:
            print("Login successful.")
            c2.execute("SELECT fname FROM studentaccounts WHERE username = ? AND hashedpassword = ?", (username, hashedpassword))
            fname = c2.fetchall()
            conn2.close()
            teacher.TeacherMenu(fname, username)
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
    hashedpassword = hashlib.sha256(saltedpassword.encode('utf-8')).hexdigest()
    if attempts < 3:
        c2.execute("SELECT * FROM studentaccounts WHERE username = ? AND hashedpassword = ?", (username, hashedpassword))
        data = c2.fetchall()
        data = str(data)
        if data:
            print("Login successful.")
            c2.execute("SELECT fname FROM studentaccounts WHERE username = ? AND hashed = ?", (username, hashedpassword))
            fname = c2.fetchall()
            conn2.close()
            student.StudentMenu(fname, username)
        else:
            print("Login failed.")
            attempts += 1
            loginarea.StudentLogin(attempts)
    else:
        print("Too many failed attempts")
        exit()
