import re

string = "C:\Simmons\classes\488\images\pic.png"

pat = re.compile(r"\\images")
m = pat.search(string)

print(m)

pat2 = re.compile("\\\images")
m2 = pat2.search(string)
print(m2)
