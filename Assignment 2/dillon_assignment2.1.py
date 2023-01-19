## Katie Dillon
## LIS 487 Assignment 2 - XML
## Part 1 - Generate HTML

## Import pandas
import pandas as pd

## Read in csv
df = pd.read_csv("XML_project.csv", header = None)

## Add column names
df.columns = ["name", "email", "category", "amount", "date"]

## Create three series
dates = df["date"]
categories = df["category"]
amts = df["amount"]

## Create new HTML file
html = open("html_table.html", "w")

## Write beginning of HTML, including table style
## Write table header row
html.write("""<html>
                <head>
                  <style> table, th, td {border: 1px solid black; padding: 5px}</style>
                </head>
                <body>
                  <table>
                     <tr>
                        <th>Date</th>
                        <th>Category</th>
                        <th>Amount</th>
                      </tr>""")

## Loop through series, add to HTML
for i in range(len(dates)):
    html.write("\n<tr>")
    html.write("\n<td>"+dates[i]+"</td>\n<td>"+categories[i]+"</td>\n<td>"+amts[i]+"</td>\n</tr>")


## Write end of HTML
html.write("\n</table>\n</body>\n</html>")

## Close HTML file
html.close()
