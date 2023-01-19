# Katie Dillon
# LIS 487 Week 3 Lab

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

# create list of means, to find highest student mean later
student_means = []

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

    # add mean to means list
    student_means.append(stat.mean(scores))

# Find highest student mean
highest = max(student_means)

# Find student with highest mean
highest_mean = []
for student, stats in students.items():
    if stats[0] == highest:
        highest_mean.append(student)

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

# Close csv file
csvfile.close()

# Write HTML file
# Create variable to write to
html = open('tests.html','w')

# Basic HTML structure, header table style
html.write("<html>\n<head>\n<style> table, th, td {border: 1px solid black;}</style>\n</head>\n<body>\n<h1>Test Data</h1>\n")

# Create table of test Statistics
html.write("<table>\n<tr>\n<th></th>\n")

# header row
for i in range(5):
    html.write("<th>Test "+str(i+1)+"</th>\n")

# rest of test statistics table
for name, stat in test_stats.items():
    html.write("<tr><td>"+name+"</td>\n<td>"+str(stat[0])+"</td>\n<td>"+str(stat[1])+"</td>\n<td>"+str(stat[2])+"</td>\n<td>"+str(stat[3])+"</td>\n<td>"+str(stat[4])+"</td>\n</tr>")

# End table
html.write("</tr>\n</table>")

# Highlight highest student mean
html.write("\n<h2>Highest Mean</h2>\n<p>The highest average score is "+str(highest)+". The student(s) with that score:")

for i in highest_mean:
    html.write(" "+i)

html.write("</p>\n")

# Student table
# Create student table
html.write("<h2>Student Data</h2>\n<table>\n<tr>\n<th>Student</th>\n<th>Mean</th>\n<th>Min</th>\n<th>Max</th>\n")

# Loop through student dictionary for rows
for student, stats in sorted(students.items()):
    html.write("<tr>\n<td>"+student+"</td>\n<td>"+str(stats[0])+"</td>\n<td>"+str(stats[1])+"</td>\n<td>"+str(stats[2])+"</td>\n")

#Close HTML
html.write("\n</body>\n</html>")

# Close HTML file
html.close()
