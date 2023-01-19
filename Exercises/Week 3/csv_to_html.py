import csv

csvfile = open('favorites.csv', newline='')
linesreader = csv.reader(csvfile, delimiter=',',quotechar='"')


movies = [] #create an empty list
colors = []
animals = []

for l in linesreader: #for each of the lines in the file - append the movies
    print(l)
    movies.append(l[1]) #I know that l[1] is the 2nd column and it is the movie title
    colors.append(l[2])
    animals.append(l[3])

print (movies) #print this to make sure that we have the right thing


html = open('faves.html','w') #create a variable to open a new html file that we can write to

html.write("<html>\n<body>\n<h1>Movies</h1>\n<ul>\n")#Boiler plate html Hard coding that this is a list of movies
                                                     #close the h1 tag and then start ann unordered list
#Just like in slide 5 use m instead of s - this will write out each individual movie as its own list item
for m in movies:
    html.write("<li>"+m+"</li>\n")

html.write("</ul>") #Close the list

html.write("\n<h1>Colors</h1>\n<ul>\n")

for c in colors:
    html.write("<li>"+c+"</li>\n")

html.write("</ul>")

html.write("\n<h1>Animals</h1>\n<ul>\n")

for a in animals:
    html.write("<li>"+a+"</li>\n")

html.write("</ul>")

csvfile.close() #close the csvfile - very important
html.close() #close the html - very important
