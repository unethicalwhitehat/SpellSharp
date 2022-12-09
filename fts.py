import sqlite3
import os
import time


def FirstTimeSetup():
    conn = sqlite3.connect("teacheraccounts.db")
    conn2 = sqlite3.connect("studentaccounts.db")
    conn3 = sqlite3.connect("scores.db")
    conn4 = sqlite3.connect("wordsanddefs.db")
    conn5 = sqlite3.connect("tests.db")

    c = conn.cursor()
    c2 = conn2.cursor()
    c3 = conn3.cursor()
    c4 = conn4.cursor()
    c5 = conn5.cursor()

    c.execute("""CREATE TABLE teacheraccounts (
                fname text,
                lname text,
                dob integer,
                username text,
                saltedpassword text,
                salt text
                )""")

    c2.execute("""CREATE TABLE studentaccounts (
                fname text,
                lname text, 
                dob integer,
                username text,
                saltedpassword text,
                salt text,
                yeargroup integer,
                teacher text
                )""")

    c3.execute("""CREATE TABLE scores (
                username text,
                testdate integer,
                score integer,
                testid integer
                )""")

    c4.execute("""CREATE TABLE wordsanddefs (
                word text,
                definition text
                )""")

    c5.execute("""CREATE TABLE tests (
                testid integer,
                testname text,
                testdate integer,
                testwords text
                )""")

    conn.commit()
    conn2.commit()
    conn3.commit()
    conn4.commit()
    conn5.commit()

    conn.close()
    conn2.close()
    conn3.close()
    conn4.close()
    conn5.close()

    print("First time setup complete. Five databases have been created.")
    time.sleep(3)
    os.system('clear')
    return
