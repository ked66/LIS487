from lxml import etree

parser = etree.XMLParser(dtd_validation=True)
tree = etree.parse("desc2022.xml",parser)
root = tree.getroot()
print(root.tag)
#for e in root.iter("*"):
 #print(e.tag)
