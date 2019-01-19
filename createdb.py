import sqlite3
conn = sqlite3.connect('housekeeping.db')
cur = conn.cursor()

cur.executescript('''
    CREATE TABLE House (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        bedrooms INTEGER NOT NULL,
        bathrooms REAL NOT NULL,
        sqft INTEGER NOT NULL,
        address TEXT NOT NULL UNIQUE,
        pets TEXT,
        entry_code TEXT,
        client_id INTEGER,
        kitchen TEXT,
        frequency TEXT,
        extra_services TEXT,
        int_windows TEXT,
        fridge TEXT,
        oven TEXT,
        blinds TEXT,
        special_services INTEGER,
        fee INTEGER
    );
    CREATE TABLE Clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT NOT NULL UNIQUE,
        business TEXT,
        referral_id INTEGER,
        house_id INTEGER
    );


''')
print("DB Tables created succesfully.")
