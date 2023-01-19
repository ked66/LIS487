# Katie Dillon
# LIS 487 Lab 2.4

import codecs

# Create empty dictionary of characters
characters = {}

# Read data as single string
File = codecs.open("MOCK_DATA.txt", "r", "utf-8")
data = File.read()
File.close()

# Loop through letters
for i in data:
    # If character isn't in dictionary, add. Otherwise, increase count by 1
    characters[i] = characters.get(i, 0) + 1

# Create chars.txt file
newFile = codecs.open("chars.txt", "w", "utf-8")

# Loop through dictionary, add to chars.txt
# Sorted dictionary as suggested by https://www.geeksforgeeks.org/python-sort-python-dictionaries-by-key-or-value/
for j in sorted(characters):
    newFile.write("{} - {}\n".format(j, characters[j]))

# Close chars.txt
newFile.close()
