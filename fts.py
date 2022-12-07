import sqlite3
import os


def FirstTimeSetup():
    conn = sqlite3.connect("teacheraccounts.db")
    conn2 = sqlite3.connect("studentaccounts.db")

    c = conn.cursor()
    c2 = conn2.cursor()

    c.execute("""CREATE TABLE teacheraccounts (
                fname text,
                lname text,
                dob integer,
                username text,
                password text,
                salt text
                )""")

    c2.execute("""CREATE TABLE studentaccounts (
                fname text,
                lname text, 
                dob integer,
                username text,
                password text,
                salt text,
                yeargroup integer,
                teacher text
                )""")

    conn.commit()
    conn2.commit()

    conn.close()
    conn2.close()

    print("First time setup complete.")