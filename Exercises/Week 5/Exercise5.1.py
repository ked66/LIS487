import re

pat = re.compile("[a-z]+", re.IGNORECASE)
string = "The cat AT bat wears HATS"

m = pat.match(string)
print(m)

g = m.group()
print(g)

s = m.start()
print(s)

e = m.end()
print(e)

sp = m.span()
print(sp)
