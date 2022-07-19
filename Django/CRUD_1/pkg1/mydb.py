# connect db -> ../db.sqlite3
# create table (persons [pid, fullname, contactaddress])
# insert data
# select data
# update data
# search data
# delete data

import sqlite3
import sys
from pkg1.person import Person

# DB_FILE = "../db.sqlite3" # Console app path
DB_FILE = "./db.sqlite3" # Web app path

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

def updateRecord(objPerson):
    conn = None
    sql = '''UPDATE persons SET name=?, address=? WHERE pid=?'''
    values = (objPerson.getName(), objPerson.getAddress(), objPerson.getPID())
    try:
        conn = sqlite3.connect(DB_FILE)  # connect with db
        cursor = conn.cursor()
        cursor.execute(sql, values) # record insert
        conn.commit() # save inserted record
        conn.close()  # connection close
        print("Record update successfully")
    except:
        print("Error : ", sys.exc_info()[0])
    finally:
        del sql
        del conn

def deleteRecord(pid):
    conn = None
    sql = '''DELETE FROM persons WHERE pid=?'''
    values = (pid,)
    try:
        conn = sqlite3.connect(DB_FILE)  # connect with db
        cursor = conn.cursor()
        cursor.execute(sql, values) # record insert
        conn.commit() # save inserted record
        conn.close()  # connection close
        print("Delete Record successfully")
    except:
        print("Error : ", sys.exc_info()[0])
    finally:
        del sql
        del conn

def selectAll():
    conn = None
    sql = '''SELECT * FROM persons'''
    persons = []
    try:
        conn = sqlite3.connect(DB_FILE)  # connect with db
        cursor = conn.cursor()
        cursor.execute(sql);  # Select All
        rows = cursor.fetchall()
        for row in rows:
            persons.append(row)
            # print(row)
        cursor.close()
        conn.close()  # connection close
        print("Display all records successfully")
        return persons
    except:
        print("Error : ", sys.exc_info()[0])
    finally:
        del sql
        del conn

def search(searchTerm):
    conn = None
    sql = "SELECT * FROM persons WHERE name LIKE '%"+searchTerm+"%' OR address LIKE '%"+searchTerm+"%'"
    persons = []
    try:
        conn = sqlite3.connect(DB_FILE)  # connect with db
        cursor = conn.cursor()
        cursor.execute(sql);  # Search
        rows = cursor.fetchall()
        for row in rows:
            persons.append(row)
            # print(row)
        cursor.close()
        conn.close()  # connection close
        print("Display all records successfully")
        return persons
    except:
        print("Error : ", sys.exc_info()[0])
    finally:
        del sql
        del conn

