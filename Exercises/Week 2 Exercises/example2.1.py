import os

# get home directory
home = os.listdir("..")

# get documents folder
documents = os.listdir(".." + os.sep + "Documents")

# get downloaded sample files
sample = os.listdir(".." + os.sep + "Downloads" + os.sep + "Week02_sample_files")

# combine in one list
all = home + documents + sample

# print
for f in all:
    print(f)
