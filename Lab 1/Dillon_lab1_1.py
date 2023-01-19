# Katie Dillon
# LIS 487 lab 1.1

# Ask user for temp in Fahrenheit
f_temp = int(input("What is the current temperature, in degrees Fahrenheit? "))

# Convert temp to Celsius
c_temp = (f_temp - 32) * (5/9)

# If for each statement
# If temperature is at edge - e.g. exactly 10 Centigrade - print both statements
if c_temp < 0:
    print("Don't forget your coat and hat!")

if 0 <= c_temp <= 10:
    print("It's quite cold, isn't it?")

if 10 <= c_temp <= 18:
    print("Might need a sweater.")

if 18 <= c_temp <= 24:
    print("Pretty nice weather today!")

if 24 <= c_temp <= 30:
    print("Getting a bit warm.")

if c_temp > 30:
    print("Summer, eh?")
