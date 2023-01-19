# Katie Dillon
# LIS 487 Lab 2.2

# Import codec and random
import codecs
import random

# Create numbers.txt
newFile = codecs.open("numbers.txt", "w", "utf-8")

# Generate random number of how many random numbers
num = random.randint(100,1000)

# For that many random numbers . . .
for i in range(num):
    # Generate random numbers
    rand = random.randint(1, 100)

    # Append random number to numbers.txt
    newFile.write("{}\n".format(rand))

# Close numbers.txt
newFile.close()
