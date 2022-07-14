# connect db -> ../db.sqlite3
# create table (persons [pid, fullname, contactaddress])
# insert data
# select data
# update data
# search data
# delete data

import sqlite3
import sys
from person import Person

DB_FILE = "../db.sqlite3"

def create_table():
    conn = None
    sql = '''CREATE TABLE persons (
        pid INTEGER PRIMARY KEY,
        name TEXT(50),
        address TEXT(50)
    )'''
    try:
        conn = sqlite3.connect(DB_FILE) # connect with db
        cursor = conn.cursor()
        cursor.execute(sql);
        conn.close() # connection close
        print("Create table successfully")
    except:
        print("Error : ", sys.exc_info()[0])
    finally:
        del sql
        del conn


def insertRecord(objPerson):
    conn = None
    sql = '''INSERT INTO persons (pid, name, address) VALUES(?,?,?)'''
    values = (objPerson.getPID(), objPerson.getName(), objPerson.getAddress())

    try:
        conn = sqlite3.connect(DB_FILE)  # connect with db
        cursor = conn.cursor()
        cursor.execute(sql, values); # record insert
        conn.commit() # save inserted record
        conn.close()  # connection close
        print("Record insert successfully")
    except:
        print("Error : ", sys.exc_info()[0])
    finally:
        del sql
        del conn
#create_table()

person  = Person(1, "Raj Rai", "KTM")
insertRecord(person)