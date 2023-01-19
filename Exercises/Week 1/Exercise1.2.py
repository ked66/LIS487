for i in range(100):
    current = i + 1
    if current % 3 == 0:
        if current % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif current % 5 == 0:
        print("Buzz")
    else:
        print(current)
