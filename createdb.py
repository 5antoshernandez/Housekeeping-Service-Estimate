import sqlite3
conn = sqlite3.connect('housekeeping.db')
cur = conn.cursor()

cur.executescript('''
    CREATE TABLE House (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        bedrooms INTEGER NOT NULL,
        bathrooms REAL NOT NULL,
        sqft INTEGER NOT NULL,
        address TEXT NOT NULL,
        pets TEXT,
        entry_code TEXT,
        client_id INTEGER
    );
    CREATE TABLE Clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT NOT NULL,
        business TEXT,
        service_fee INTEGER,
        referral_id INTEGER,
        house_id INTEGER
    );
    CREATE Table Services (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        house_id INTEGER,
        client_id INTEGER,
        kitchen INTEGER NOT NULL,
        frequency INTEGER NOT NULL,
        extra_services INTEGER,
        int_windows INTEGER,
        fridge INTEGER,
        oven INTEGER,
        blinds INTEGER,
        special_services INTEGER,
        fee INTEGER
    );

''')
print("DB Tables created succesfully.")
