## Katie Dillon
## LIS 487
## Assignment 1 todo

import re

## Read original file
readFile = open("todo.txt", "r")
todo = readFile.readlines()
readFile.close()

## Define search expressions
name = re.compile("([^,]*),")
date = re.compile("(\d{1,2})[/,-](\d{1,2})[/,-](\d{4})")
phone = re.compile("[\s\(1-]{0,3}(\d{3})[)\s]?.?(\d{3}).?(\d{4})")
email = re.compile("([^,\s]*@[^,\s]*)")
message = re.compile("\w.*")

## Open new file
newFile = open("Tasks.txt", "w")

## Define tasks dictionary
tasks = {}

## Loop through todo lines
for line in todo:
    ## Match date, name, phone
    d = date.search(line)
    n = name.search(line)
    p = phone.search(line)

    ## If contact is phone
    if p:
        ## format phone number
        final_contact = "("+p.group(1)+")-"+p.group(2)+"-"+p.group(3)
        ## remove phone from line
        line = re.sub(re.escape(p.group(0)), "", line)

    ## If contact is email
    else:
        e = email.search(line)
        final_contact = e.group(1)
        ## remove email from line
        line = re.sub(e.group(1), "", line)

    ## remove name and date from line
    line = re.sub(n.group(0), "", line)
    line = re.sub(d.group(0), "", line)

    ## If month is missing leading zeros, add
    if len(d.group(1)) == 1:
        month = "0"+d.group(1)
    else:
        month = d.group(1)

    ## If day is missing leading zeros, add
    if len(d.group(2)) == 1:
        day = "0"+d.group(2)
    else:
        day = d.group(2)

    ## Format date, save name
    final_date = d.group(3)+"-"+month+"-"+day
    final_name = n.group(1)

    ## Match message, strip trailing spaces
    m = message.search(line)
    final_message = m.group(0).strip()

    ## Save to dictionary
    tasks[final_date] = [final_name, final_contact, final_message]

## Loop through sorted dictionary
for key, value in sorted(tasks.items()):

    ## Add to new file, formatted
    newFile.write(key+": "+value[2]+"\n\t"+value[0]+", "+value[1]+"\n\n")

## close new file
newFile.close()
