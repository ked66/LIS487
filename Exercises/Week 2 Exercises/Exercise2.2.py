# Read in file as lines
readFile = open("jabberwocky.txt", "r")
fileText = readFile.readlines()
readFile.close()

# For each line
for line in fileText:

    # Split into words, find length
    words = line.split()
    length = len(words)

    # Print length and line
    print("[{}] {}".format(length, line))
