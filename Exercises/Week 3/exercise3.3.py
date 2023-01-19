import csv

csvfile = open('favorites.csv', newline = '')
linesreader = csv.reader(csvfile, delimiter=',', quotechar='"')

movies = []
colors = []
animals = []

for l in linesreader:
    movies.append(l[1])
    colors.append(l[2])
    animals.append(l[3])

print(movies)
print(colors)
print(animals)

csvfile.close()
