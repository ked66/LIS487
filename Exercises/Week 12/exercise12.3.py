import sqlite3 as s3

conn = s3.connect('test.db')
c = conn.cursor()

c.execute("SELECT * FROM pets;")
data = c.fetchall()

for d in data:
    print("{} is a {} year old {}".format(d[0], d[2], d[1]))

conn.close()
