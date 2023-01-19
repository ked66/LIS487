# Katie Dillon
# LIS 487 lab 1.2

# Input
string =  "When I pronounce the word Future,\nthe first syllable already belongs to the past.\n\nWhen I pronounce the word Silence,\nI destroy it.\n\nWhen I pronounce the word Nothing,\nI make something no nonbeing can hold.\n\nWislawa Szymborska"

# Replace \n with space
replaced = string.replace("\n", " ")

# Make all letter upper case
upper = replaced.upper()

# Split input into list of words with space as delimiter
split = upper.split()

# Define empty dictionary
starts = {}

# Loop through words
for word in split:
    # Get first letter
    first = word[0]

    # Add to dictionary as count
    starts[first] = starts.get(first, 0) + 1

# Loop through dictionary to print
for i in starts:
    print(i, ": ", starts[i])
