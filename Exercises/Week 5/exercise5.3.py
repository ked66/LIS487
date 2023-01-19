import re

pat = re.compile("(\d\d)-(\d\d)-(\d\d\d\d)")
m = pat.match("20-07-1969")

for i in range(1, 4):
    print(m.span(i))
