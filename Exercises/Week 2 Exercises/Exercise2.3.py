# Read using codecs and UTF-8
import codecs
file1 = codecs.open("MOCK_DATA.txt", "r", "utf-8")
text = file1.readlines()
file1.close()

# Create empty net edu file
newFile = codecs.open("NET_EDU.txt", "w", "utf-8")

# For each line
for line in text:

    # Check if each address ends .net or .edu
    if line[-4:-1].upper() == "NET" or line[-4:-1].upper() == "EDU":

        # Add line to net edu file
        newFile.write(line)

# Close new file
newFile.close()
