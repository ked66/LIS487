## Katie Dillon
## LIS 487 Assignment 2 - XML
## Part 4 - Use XPath

## Import etree
from lxml import etree

## Parse xml
tree = etree.parse("budget.xml")

## Get emails and categories for transactions < $5.00
## Returns list [email, category, email, category . . . ]
small = tree.xpath("./budget_item[amount<5.00]/email/text() | ./budget_item[amount<5.00]/category/text()")

## Set counter
i = 0

## Print context
print("Individuals with the following emails made purchases of less that $5.00 in the following Budget categories.")
print("")

## Loop through small, print email, then category
while i < len(small):
    print(small[i],": ", small[i+1])
    i = i + 2

## Get dates of computer purchases
computer = tree.xpath("./budget_item[category='Computers']/date/text()")

## Print context
print("")
print("")
print("Purchases in the 'Computers' Budget Category were made on the following dates.")
print("")

## Sort/print
for j in sorted(computer):
    print(j)

## Get first names of purchases in 2017-03
march = tree.xpath("//budget_item[date[contains(.,'2017-03')]]/name/firstname/text()")

## Print context
print("")
print("")
print("Inividuals with the following first names made purchases in March, 2017.")
print("")

## Print
for k in march:
    print(k)
