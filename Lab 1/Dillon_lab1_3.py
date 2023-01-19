# Katie Dillon
# LIS 487 lab 1.3

import random

# Create dictionary
states = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona':'Phoenix',
    'Arkansas':'Little Rock',
    'California': 'Sacramento',
    'Colorado':'Denver',
    'Connecticut':'Hartford',
    'Delaware':'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinios': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Moines',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'St. Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Neveda': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'
}

# Create list of keys
keys = []
for state in states:
    keys.append(state)

# Set counters
correct = 0
incorrect = 0
question_number = 1

# Introduce quiz
print("Let's see how well you know your U.S. state capitals!")
print("(Hint: Make sure you captialize the first letter of each word.)")
print("")

# Loop of 10
for i in range(10):

    # Pick random key
    test = random.choice(keys)

    # Remove key from list so it isn't chosen again
    keys.remove(test)

    # Ask user for answer
    guess = input("{}/10. What is the capital of {}?  ".format(question_number, test))

    # Check answer vs dictionary; add to counter
    if states[test] == guess:
        print("That is correct!")
        correct = correct + 1

    else:
        print("Sorry, that is incorrect.")
        incorrect = incorrect + 1

    # Increase question number
    question_number = question_number + 1

# Report number correct/incorrect
print("")
print("Good job!")
print("You answered", correct, "correctly and", incorrect, "incorrectly.")
