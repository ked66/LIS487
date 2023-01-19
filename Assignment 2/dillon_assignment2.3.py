## Katie Dillon
## LIS 487 Assignment 2 - XML
## Part 3 - Generate XML

## Import pandas and re
import pandas as pd

## Read in csv, add headers
df = pd.read_csv("XML_project.csv", header = None)
df.columns = ["name", "email", "category", "amount", "date"]

## Start xml
xml = open("budget.xml", "w")
xml.write("<?xml version='1.0' encoding='UTF-8'?><!DOCTYPE budgets SYSTEM 'budgets.xsd'>")
xml.write("<budget>\n")

## Loop through df
for i, row in df.iterrows():
    ## Print row as list
    row_list = [row["name"], row["email"], row["category"], row["amount"], row["date"]]
    print(row_list)

    ## Begin xml entry
    xml.write("<budget_item>\n<name>\n")

    ## Split name to firstname and lastname
    name = row["name"].split()
    xml.write("<firstname>"+name[0]+"</firstname>\n<lastname>"+name[1]+"</lastname>\n</name>\n")

    ## Remove $ from amount
    amount = row["amount"][1:]

    ## Add email, amount, category, date
    xml.write("<email>"+row["email"]+"</email>\n<amount>"+amount+"</amount>\n<category>"+row["category"]
    +"</category>\n<date>"+row["date"]+"</date>\n")
    xml.write("</budget_item>\n")

## Finish xml
xml.write("</budget>")
xml.close()

## Validate XML
from lxml import etree

## Set schema
schema = etree.XMLSchema(etree.parse("budgets.xsd"))

## Validate
print(schema.validate(etree.parse("budget.xml")))
