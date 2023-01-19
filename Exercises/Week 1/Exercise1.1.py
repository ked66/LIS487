#Ask user what year they were born
birthYear = int(input("What year were you born? "))

#calculate age
age = 2022 - birthYear

#report age
print("You are", str(age), "years old. Cool beans!")

#respond appropriately
if age < 18:
    print("You are too young to vote.")

elif age < 35:
        print("You can vote but can't be President.")

elif age < 65:
        print("You can be President, but can't retire.")

else:
        print("You could retire OR you could be President!")
