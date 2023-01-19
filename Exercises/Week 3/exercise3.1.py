import random
import statistics

numbers = []

for i in range(100):
    numbers.append(random.randint(0, 100))

mean = statistics.mean(numbers)
median = statistics.median(numbers)
mode = statistics.mode(numbers)
sd = statistics.stdev(numbers)

print("Representative Statistics of this Random Dataset:")
print("Mean - {}".format(mean))
print("Median - {}".format(median))
print("Mode - {}".format(mode))
print("Standard Deviation - {}".format(sd))
