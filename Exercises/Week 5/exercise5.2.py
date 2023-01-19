import re

pat = re.compile("\w*at\w*")
string = "the cat at bat wears hats"

m = pat.finditer(string)

for i in m:
    print(i)
