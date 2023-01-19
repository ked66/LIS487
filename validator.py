from lxml import etree

schema = etree.XMLSchema(etree.parse("budgets.xsd"))
print(schema.validate(etree.parse("budget.xml")))
