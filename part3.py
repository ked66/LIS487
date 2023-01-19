## Import JSON, pandas, plotly
import json
import pandas as pd
import plotly.express as px

## BRING IN DATA

## Import mesh data, load as JSON
file = open('mesh.json')
full_mesh = json.load(file)

## Open HTML
html = open("mesh_report.html", "a")

## Define empty list
data = []

## Loop through mesh data to extract relevant columns
for i in full_mesh:
    ## Only include descriptor if it has associated tree number(s)
    if 'DescriptorName' in full_mesh[i] and 'TreeNumberList' in full_mesh[i]:
        tree_numbers = full_mesh[i]['TreeNumberList']

        ## Get allowable qualifiers
        if 'AllowableQualifiersList' in full_mesh[i]:
            allowableQualifiers = full_mesh[i]['AllowableQualifiersList']
        ## If none, define as list with length 0
        else:
            allowableQualifiers = []

        ## Each tree number as new row
        for j in range(len(tree_numbers)):
            data.append([full_mesh[i]['DescriptorName'], allowableQualifiers, tree_numbers[j]])

## Convert list to dataframe
df = pd.DataFrame(data, columns = ["Name", "AllowableQualifiersList", "TreeNumber"])

## Write to html
html.write("""<h2>Analysis of Allowable Qualifiers</h2>
                <h3>Mean Number of Allowable Qualifers by Primary Tree Branch</h3>
""")

## FIND MEAN NUMBER OF ALLOWABLE QUALIFIERS BY PRIMARY TREE BRANCH

## Calculate number of allowable qualifiers by tree number
df['NumberQualifiers'] = df.apply(lambda row: len(row.AllowableQualifiersList), axis = 1)
## Define Primary tree level -- leading letter in tree number
df['Primary'] = df.apply(lambda row: row.TreeNumber[0], axis = 1)

## Find mean number of qualifiers by primary tree branch; format as dataframe and reset index
## Sort dataframe by Primary tree branch value
df1 = pd.DataFrame(df.groupby(["Primary"]).mean("NumberQualifiers").round(2)).reset_index().sort_values('Primary')

html.write(df1.to_html(index=False, border=0))

## FIND TOP 5 ALLOWABLE QUALIFIERS BY PRIMARY TREE BRANCH

## Define empty dictionary
dict = {}

## Loop dataframe
for index, row in df.iterrows():
    ## If primary tree branch not in dictionary, add as empty dictionary
    if row.Primary not in dict:
        dict[row.Primary] = {}

    ## Loop through allowable qualifiers
    for qualifier in row.AllowableQualifiersList:
        ## If qualifier is not in primary tree branch dictionary, add with count = 1
        if qualifier['QualifierReferredTo']['QualifierName'] not in dict[row.Primary]:
            dict[row.Primary][qualifier['QualifierReferredTo']['QualifierName']] = 1

        ## Otherwise, increase count by 1
        else:
            dict[row.Primary][qualifier['QualifierReferredTo']['QualifierName']] += 1

html.write("""<h3>Most Common Allowable Qualifiers by Primary Tree Branch</h3>""")

## Loop primary tree branch dictionaries
for branch, qualifiers in sorted(dict.items()):
    ## Find top 5 qualifiers by count
    ## adapted from https://stackoverflow.com/questions/40496518/how-to-get-the-3-items-with-the-highest-value-from-dictionary
    top = sorted(qualifiers, key=qualifiers.get, reverse=True)[:5]

    ## Print Primary tree branch and top five qualifiers, with counts
    html.write("<p>"+branch+":</p><ul>")
    for i in top:
        value = qualifiers[i]
        html.write("<li>"+i+" ("+str(value)+" descriptors)</li>")

    html.write("</ul>")

html.close()
