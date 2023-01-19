## Import JSON, pandas, plotly
import json
import pandas as pd
import plotly.express as px

## Import mesh data, load as JSON
file = open('mesh.json')
full_mesh = json.load(file)

## Open HTML file
html = open("mesh_report.html", "w")

## Define empty list
data = []

## Loop through mesh data to extract relevant columns
for i in full_mesh:
    ## Only include descriptor if it has associated tree number(s)
    if 'DescriptorName' in full_mesh[i] and 'TreeNumberList' in full_mesh[i]:
        tree_numbers = full_mesh[i]['TreeNumberList']
        ## Each tree number in list as new row
        for j in range(len(tree_numbers)):
            data.append([full_mesh[i]['DescriptorName'], tree_numbers[j]])

## Convert list to dataframe
df = pd.DataFrame(data, columns = ["Name", "TreeNumber"])

## Define tree levels
## Primary is main tree branch -- leading letter in tree number
df['Primary'] = df.apply(lambda row: row.TreeNumber[0], axis = 1)
## Secondary is next 2 numbers
df['Secondary'] = df.apply(lambda row: row.TreeNumber[1:3], axis = 1)
## Tertiary is next 3 numbers (skipping '.' in position 3)
df['Tertiary'] = df.apply(lambda row: row.TreeNumber[4:7], axis = 1)

## Find count of each Primary-Secondary-Tertiary combination
## Format as dataframe and reset index
## adapted from https://stackoverflow.com/questions/10373660/converting-a-pandas-groupby-output-from-series-to-dataframe
df1 = pd.DataFrame({'count' : df.groupby([ "Primary", "Secondary", "Tertiary"] ).size()}).reset_index().sort_values('Primary')

## Graph as sunburst plot
## Adapted from https://towardsdatascience.com/visualize-hierarchical-data-using-plotly-and-datapane-7e5abe2686e1

## Write HTML context
html.write("""<h1>MeSH Report</h1>
                <h2>Graphs</h2>
                <h3>Figure 1: Graph of Descriptors by Tree Location</h3>""")

## Primary-Secondary-Tertiary - More information
fig2 = px.sunburst(df1, path=['Primary', 'Secondary', 'Tertiary'], values='count', color='Primary')
fig2.update_layout(title_text="Descriptors by Primary, Secondary, and Tertiary Tree Branch", font_size=14)
fig2.write_html(html)

## Limit to A08.612
df2 = df.loc[df['TreeNumber'].str.contains('A08.612')]

## Define empty list
data2 = []

## Loop dataframe to get relevant information
for index, row in df2.iterrows():
    names = row['Name']
    treeNumber = row['TreeNumber']
    ## If tree number is A08.612, no parent
    if treeNumber == 'A08.612':
        parent = ''
    ## Otherwise, parent has tree number equal to child minus last four digits
    else:
        parent = df2[df2['TreeNumber'] == row['TreeNumber'][:-4]].iloc[0]['Name']

    ## Weight equals number of downstream tree numbers
    weight = len(df2[df2['TreeNumber'].str.contains(row['TreeNumber'])])

    ## Append to list
    data2.append([names, treeNumber, parent, weight])

## Convert to dataframe
df3 = pd.DataFrame(data2, columns = ["Name", "TreeNumber", "Parent", "Weight"])

## Write html context
html.write("""<h3>Figure 2 - Graph of Descriptors by Tree Location, Neural Pathways""")

## Graph as sunburst
fig3 = px.sunburst(df3, names = 'Name', branchvalues = 'total', parents = 'Parent', values='Weight', color='Parent')
fig3.update_layout(title_text="Descriptors Along Nerual Pathways Tree", font_size=14)
fig3.write_html(html)

html.close()
