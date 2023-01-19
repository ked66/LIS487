import sqlite3 as s3

conn = s3.connect('test.db')
c = conn.cursor()

c.execute("INSERT INTO pets VALUES ('Speedy', 'tortoise', 102)")

names = ["Bonita", "Cookie", "Casey", "Chris"]
species = ["hamster", "guinea pig", "dog", "cat"]
ages = [2, 4, 12, 15]

for i in range(4):
    c.execute("INSERT INTO pets VALUES (?,?,?)",(names[i], species[i], ages[i]))

conn.commit()

conn.close()
