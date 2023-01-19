## Katie Dillon
## LIS 487 Exercise 12.4

## Import sqlite and csv
import sqlite3 as s3
import csv

## Connect to ExportMe.db file, create cursor
conn = s3.connect("ExportMe.db")
c = conn.cursor()

## Find table names in db
print("tables:")
c.execute("SELECT name from sqlite_master WHERE type='table';")
tables = c.fetchall()
for table_name in tables:
    print(table_name) ## We see there are 2 tables - 'employees' and 'departments'

## Create employees csv
e_csv = open('employees.csv', 'w', encoding='UTF8')
writer = csv.writer(e_csv)

## Get data from database
employees = c.execute("SELECT * FROM employees;")

## Get column names (adapted from https://stackoverflow.com/questions/7831371/is-there-a-way-to-get-a-list-of-column-names-in-sqlite)
e_header = []
for x in employees.description:
    e_header.append(x[0])

## Add column names to csv
writer.writerow(e_header)

## Add values to csv
for e in employees:
    writer.writerow(list(e))

## Close csv
e_csv.close()

## And again for departments
## Create csv file
d_csv = open('departments.csv', 'w', encoding='UTF8')
writer = csv.writer(d_csv)

## Get data
depts = c.execute("SELECT * FROM departments")

## Get column names (adapted from https://stackoverflow.com/questions/7831371/is-there-a-way-to-get-a-list-of-column-names-in-sqlite)
d_header = []
for y in depts.description:
    d_header.append(y[0])

## Add column names to csv
writer.writerow(d_header)

## Add data
for d in depts:
    writer.writerow(list(d))

## Close csv
d_csv.close()

## Close connection
conn.close()
