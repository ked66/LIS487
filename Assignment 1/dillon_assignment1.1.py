## Katie Dillon
## LIS 487
## Assignment 1 Play

import re

## Read HTML
readFile = open("Henry V Entire Play.html", "r")
henry = readFile.readlines()
readFile.close()

## Define search expressions
act = re.compile("<h3>(ACT.*)</h3>", re.IGNORECASE)
scene = re.compile("<h3>(SCENE[^\.]*)\. (.*)</h3>", re.IGNORECASE)
direction = re.compile("<i>(.*)</i>")
# Speaker indicated by name attribute = "speech"
speaker = re.compile("<a name=\"speech[^>]*><b>([^>]*)<.*")
# Play lines indicated by name attribute = digits
text = re.compile("<a name=\"\d[^>]*>([^<>]*)<.*")

## Open new text file
newFile = open("HenryV.txt", "w")

## Loop through lines
for line in henry:
    # if line is act
    n = act.search(line)
    if n:
        newFile.write("=="+n.group(1)+"==\n\n")
        continue

    # if line is scene
    m = scene.search(line)
    if m:
        newFile.write("=" + m.group(1) + "=\n{" + m.group(2) + "}\n\n")
        continue

    # if line is stage direction
    d = direction.search(line)
    if d:
        newFile.write("\n["+d.group(1)+"]\n\n")
        continue

    # if line indicates speaker
    sp = speaker.search(line)
    if sp:
        newFile.write("\n\n"+sp.group(1)+":\n\n")
        continue

    # if line is spoken line in play
    txt = text.search(line)
    if txt:
        newFile.write("\t"+txt.group(1)+"\n")
        continue

    # else, do not write to new file

## Close new file
newFile.close()
