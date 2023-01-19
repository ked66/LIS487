# import packages
import csv
import statistics as stat

# read csv into lines
csvfile = open("testdata.csv", newline="")
lines = csv.reader(csvfile, delimiter=";")

# create list for each test
test1 = []
test2 = []
test3 = []
test4 = []
test5 = []

# create dictionary for students
students = {}

# loop through lines
for l in lines:

    # append test scores to test lists
    test1.append(int(l[1]))
    test2.append(int(l[2]))
    test3.append(int(l[3]))
    test4.append(int(l[4]))
    test5.append(int(l[5]))

    # make list of student's scores
    scores = []
    scores.append(int(l[1]))
    scores.append(int(l[2]))
    scores.append(int(l[3]))
    scores.append(int(l[4]))
    scores.append(int(l[5]))

    # add student names and summary stats to dictionary
    split_name = l[0].split()
    name = "{}, {}".format(split_name[1], split_name[0])
    students[name] = [stat.mean(scores), min(scores), max(scores)]

# Create list of tests
tests = [test1, test2, test3, test4, test5]

# Create dictionary for test statistics
test_stats = {
    "Max": [],
    "Min": [],
    "Mean": []
}

# loop through tests, add statistics to dictionary
for t in tests:
    test_stats["Mean"].append(stat.mean(t))
    test_stats["Min"].append(min(t))
    test_stats["Max"].append(max(t))

print(test_stats)

# Close csv file
csvfile.close()
