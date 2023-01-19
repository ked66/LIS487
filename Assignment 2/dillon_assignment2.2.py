## Katie Dillon
## LIS 487 Assignment 2 - XML
## Part 2 - Data Analysis

## Import pandas
import pandas as pd

## Read in csv
df = pd.read_csv("XML_project.csv", header = None)

## Create HTML to display results, add initial html
html = open("spending.html", "w")

html.write("""<html>
                <head>
                    <style> table, th, td {border: 1px solid black; padding: 5px} </style>
                </head>
                <body>
                    <h1>Budget Analysis</h1>
                    <h2>By Budget Category</h2>
                    <table>
                        <tr>
                            <th>Budget Category</th>
                            <th>Amount</th>
                        </tr>""")

## Add column names
df.columns = ["name", "email", "category", "amount", "date"]

## Remove $ from amount
## https://stackoverflow.com/questions/42349572/remove-first-x-number-of-characters-from-each-row-in-a-column-of-a-python-datafr
df["amount"] = df["amount"].str[1:]

## Convert amount to float
df["amount"] = df["amount"].astype(float)

## Group by Category
categories = df.groupby("category")

## Set highest
highest_amt = 0
highest_name = ""

## Loop through cateogries
for name, data in categories:
    total = data["amount"].sum()
    total = round(total,2)

    ## If highest so far, set as highest
    if total > highest_amt:
        highest_amt = total
        highest_name = name

    ## Write to html
    html.write("<tr><td>"+name+"</td>\n<td>$"+str(total)+"</td></tr>")

## Finish table html
html.write("</table>")

## Add highest to html
highest_amt = round(highest_amt,2)
html.write("<p>People spent the most on <strong>"+highest_name+"</strong>, to the tune of <strong>$"+str(highest_amt)+"</strong></p>")


## Group by month
## Add column year_month
df["year_month"] = df["date"].str[:-3]

## Group by year_month
months = df.groupby("year_month")

## Initial year_month html
html.write("""<h2>By Month</h2>
                <table><tr>
                <th>Year-Month</th>
                <th>Amount</th></tr>""")

## Loop through year_months
for name, data in months:
    total = data["amount"].sum()
    total = round(total,2)

    ## Write to html
    html.write("<tr><td>"+name+"</td><td>$"+str(total)+"</td></tr>")

## Finish year_month table
html.write("</table>")

## Find person who spent most
big_spender = df[df["amount"] == df["amount"].max()]
name = str(big_spender.iloc[0,0])
amt = str(big_spender.iloc[0,3])
cat = str(big_spender.iloc[0,2])

## Write to html
html.write("<h2>Big Spender</h2><p><strong>"+name+"</strong> spent <strong>$"+amt+"</strong> on <strong>"+cat+"</strong> items.</p>")

## End html
html.write("</body></html>")
html.close()

## Tell user where to find results
print("Open 'spending.html' to view results of the analysis.")
