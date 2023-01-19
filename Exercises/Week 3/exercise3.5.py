import csv
import statistics as stat

csvfile = open("numbers.csv", newline = "")
lines = csv.reader(csvfile, delimiter = ",")

numbers = []

for l in lines:
    numbers.append(int(l[1]))

print("Descriptive Statistics")
print("Mean: "+str(stat.mean(numbers)))
print("Median: "+str(stat.median(numbers)))
print("Mode: "+str(stat.mode(numbers)))
print("Standard Deviation: "+str(stat.stdev(numbers)))

csvfile.close()
