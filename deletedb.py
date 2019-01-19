import sqlite3
conn = sqlite3.connect("housekeeping.db")
curr = conn.cursor()

deletedb = input("Are you sure you want to delete the DB?")
if deletedb == "Y" or deletedb == "y":
    curr.executescript('''
    DROP TABLE House;
    DROP TABLE Clients;
    DROP TABLE Services
    ''')
