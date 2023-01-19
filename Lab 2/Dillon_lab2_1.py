# Katie Dillon
# LIS 487 Lab 2.1

# Import codecs
import codecs

# If 'PeopleIveMet' exists, open to append.  Else, create
# As suggested in https://stackoverflow.com/questions/20432912/writing-to-a-new-file-if-it-doesnt-exist-and-appending-to-a-file-if-it-does
File = codecs.open("PeopleIveMet.txt", "a+", "utf-8")

# Ask user's first name
first = input("Hi there! I'm Py Thon. What's your first name? ")

# Ask user's last name
last = input("Nice to meet you, {}. What's your last name? ".format(first))

# Ask user's age
age = input("You sound pretty cool, {} {}. How old are you, in years? ".format(first, last))

# Add info to PeopleIveMet
File.write("{}, {}: {}\n".format(last, first, age))

# Close PeopleIveMet
File.close()
