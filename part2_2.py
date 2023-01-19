## Import JSON, pandas, plotly
import json
import pandas as pd
import plotly.express as px

## Import mesh data, load as JSON
file = open('mesh.json')
full_mesh = json.load(file)

## Open HTML file
html = open("mesh_report.html", "a")

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
fig2 = px.sunburst(df3, names = 'Name', branchvalues = 'total', parents = 'Parent', values='Weight', color='Parent')
fig2.update_layout(title_text="Descriptors Along Nerual Pathways Tree", font_size=14)
fig2.write_html(html)

html.close()
