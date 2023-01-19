import sqlite3 as s3

conn = s3.connect('test.db')
c = conn.cursor()

try:
    c.execute('''CREATE TABLE people (ID integer, name text, birthdate text)''')
except:
    print("Oops! Does table 'people' already exist?")

try:
    c.execute('''CREATE TABLE pets (name text, species text, age integer)''')
except:
    print("Oops! Does table 'pets' already exist?")

c.execute("SELECT name from sqlite_master WHERE type='table';")
tables = c.fetchall()
for table_name in tables:
    print(table_name)

conn.close()
