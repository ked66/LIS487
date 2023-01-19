# Katie Dillon
# LIS 487 Lab 2.3

import codecs

# Read numbers.txt lines into list
File = codecs.open("numbers.txt", "r", "utf-8")
lines = File.readlines()
File.close()

# Remove line breaks, append to list as integer
numbers = []
for i in lines:
    numbers.append(int(i[:-1]))

# Find length of numbers
print("The list has {} numbers in it.".format(len(numbers)))

# Find sum of numbers
print("The sum of the list is {}.".format(sum(numbers)))
