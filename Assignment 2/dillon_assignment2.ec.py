## Katie Dillon
## LIS 487 Assignment 2 - XML
## Extra Credit

## Goal -- Graph total monthly spending for the top 5 spending categories
## Much support from https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html

## Import pandas, numpy, matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

## Read in csv
df = pd.read_csv("XML_project.csv", header = None)

## Add column names
df.columns = ["name", "email", "category", "amount", "date"]

## Remove $ from amount
## https://stackoverflow.com/questions/42349572/remove-first-x-number-of-characters-from-each-row-in-a-column-of-a-python-datafr
df["amount"] = df["amount"].str[1:]

## Convert amount to float
df["amount"] = df["amount"].astype(float)

### Find top 5 spending categories
## Group by Category
categories = df.groupby("category")

## Create dictionary of category:total
# Empty dictionary
cat_dict = {}

# Loop through df
for name, data in categories:
    total = data["amount"].sum()
    total = round(total,2)

    cat_dict[name] = total

## Get names of top 5 spending categories
top_5 = sorted(cat_dict, key=cat_dict.get)[-5:]

### Get data for Graph
## Create dictionary with 5 categories of interest
for_graph = {}
for i in top_5:
    for_graph[i] = list()

## Group by year-month
df["year_month"] = df["date"].str[:-3]
new_df = df.groupby("year_month")

## List of year-months for x-axis
time = list()

## Loop through year-months
for name, data in new_df:
    ## Add year-month to list
    time = list(time)
    time.append(name)

    ## Loop through categories
    categories = data.groupby("category")
    for category, amt in categories:
        ## Add to dictionary if category of interest
        if category in for_graph:
            all = list(for_graph[category])
            all.append(round(amt["amount"].sum(), 2))
            for_graph[category] = all

    ## If no value for that year-month, add 0 to dictionary
    for key, value in for_graph.items():
        if len(value) < len(time):
            all = list(for_graph[key])
            all.append(0)
            for_graph[key] = all

## Create figure, add subplot
fig = plt.figure(figsize=(12, 5))
ax = fig.add_subplot(111)

## Graph each category
for key, value in for_graph.items():
    ax.plot(time, value, label=key)

## Add labels and title
plt.xlabel('Year-Month')
plt.ylabel('Total Spending (USD)')
plt.title('Total Monthly Spending Per Category')

## Add legend
plt.legend()

## Plot
plt.show()
