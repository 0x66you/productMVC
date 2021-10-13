import sqlite3

conn = sqlite3.connect('marketplace.db')
c = conn.cursor()

sql = ''' 
CREATE TABLE product(
    id INTEGER,
    name TEXT,
    price REAL,
    quantity INTEGER,
    date TEXT,
    PRIMARY KEY('id')
)
'''
c.execute(sql)
conn.commit()
conn.close()