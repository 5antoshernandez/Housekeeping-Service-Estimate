import sqlite3
conn = sqlite3.connect('housekeeping.db')
curr = conn.cursor()
clientList = curr.execute('SELECT name FROM Clients')

for client in clientList:
    print(client[0])
