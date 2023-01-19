import re

readFile = open("dates.txt", "r")
fileText = readFile.readlines()
readFile.close()

newFile = open("dates2.txt", "w")

pat = re.compile("(\d\d)/(\d\d)/(\d\d\d\d)")

for i in fileText:
    m = pat.search(i)
    newFile.write("{}-{}-{}\n".format(m.group(3), m.group(1), m.group(2)))

newFile.close()
