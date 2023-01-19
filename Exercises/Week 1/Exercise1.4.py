#import random
import random

#empty dictionary
count = {}

#loop through 100
for i in range(100):

    #generate random number
    number = random.randint(1, 10)

    #dictionary count -- gotta go fast version
    count[number] = count.get(number, 0) + 1

#print dictionary
for j in count:
    print(str(j) + ": " + str(count[j]))

#check count
total = 0

#add
for k in count:
    total = total + count[k]

#print total
print("The total is:", total)
