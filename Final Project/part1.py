## Import etree and json
from lxml import etree
import json

## Parse xml file and get root
tree = etree.parse("desc2022.xml")
root = tree.getroot()

## Define empty dictionary
DescriptorRecordSet = {}

## Loop through records ('Descriptors')
for Descriptor in root:

    ## Define empty dictionary for individual record
    DescriptorRecord = {}

    ## Add attribute 'DescriptorClass', if exists
    if Descriptor.attrib['DescriptorClass']:
        DescriptorRecord['@DescriptorClass'] = Descriptor.attrib['DescriptorClass']

    ## Loop through elements of descriptor record
    for element in Descriptor:

            ## If element is 'DescriptorName', define as text of child element 'String'
            if element.tag == 'DescriptorName':
                for child in element:
                    DescriptorRecord[element.tag] = child.text

            ## If element is 'DateCreated', 'DateCreated', or 'DateEstablished' define as dictionary
            ##(date is given in separate year, month, day elements)
            elif element.tag in ('DateCreated', 'DateRevised', 'DateEstablished'):
                DescriptorRecord[element.tag]={}

                ## Loop child elements (year, month, day) and add to dictionary
                for child in element:
                    DescriptorRecord[element.tag][child.tag]=child.text.strip()

            ## If element is 'AllowableQualifiersList' or 'SeeRelatedList', define as list
            elif element.tag in ("AllowableQualifiersList", "SeeRelatedList"):
                DescriptorRecord[element.tag] = []

                ## Loop through child elements -- individual qualifiers or related descriptors
                for child in element:
                    ## Define empty dictionary 'qualifier'
                    qualifier = {}

                    ## Loop through elements of individual qualifier or related descriptor
                    for child2 in child:

                        ## If element contains 'ReferredTo', define as dictionary
                        if "ReferredTo" in child2.tag:
                            qualifier[child2.tag] = {}

                            ## Loop child elements
                            for child3 in child2:

                                ## If child element contains 'Name', define as value of child element 'string'
                                if "Name" in child3.tag:
                                    for child4 in child3:
                                        qualifier[child2.tag][child3.tag] = child4.text.strip()

                                ## Otherwise, define as element value
                                else:
                                    qualifier[child2.tag][child3.tag] = child3.text.strip()

                        ## If "ReferredTo" not in element name, define element as element value
                        else:
                            qualifier[child2.tag] = child2.text.strip()

                    ## Append individual qualifier to qualifier list
                    DescriptorRecord[element.tag].append(qualifier)

            ## If descriptor element is 'PreviousIndexingList' or 'TreeNumberList',
            ## define as list
            elif element.tag in ("PreviousIndexingList", "TreeNumberList"):
                DescriptorRecord[element.tag] = []

                ## loop individual 'Previous Indexing' or 'Tree Number'
                for child in element:
                    ## Append value to list
                    DescriptorRecord[element.tag].append(child.text)

            ## If descriptor element is 'PharmacologicalActionList', define as list
            elif element.tag == "PharmacologicalActionList":
                DescriptorRecord[element.tag] = []

                ## loop each PharmacologicalAction, define empty dictionary
                for child in element:
                    pharmAction = {}

                    ## loop subelements
                    for child2 in child:
                        ## If element is 'DescriptorName', get string from child element
                        if child2.tag == 'DescriptorName':
                            for child3 in child2:
                                pharmAction[child2.tag] = child3.text
                        ## Otherwise, element equals text
                        else:
                            pharmAction[child2.tag] = child2.text

                    ## Append individual pharmAction to PharmacologicalActionList
                    DescriptorRecord[element.tag].append(pharmAction)

            ## If element is 'ConceptList', define as empty list
            elif element.tag == "ConceptList":
                DescriptorRecord[element.tag] = []

                ## Loop each concept
                for child in element:
                    ## Define concept as empty dictionary
                    concept = {}
                    ## Get attribute 'PreferredConceptYN' -- required, will always exist
                    concept['@PreferredConceptYN'] = child.attrib['PreferredConceptYN']

                    ## Loop elements in concept
                    for x in child:
                        ## If 'ConceptName', get text from child element
                        if x.tag == 'ConceptName':
                            for child2 in x:
                                concept[x.tag] = child2.text

                        ## If 'RelatedRegistryNumberList', define as empty list
                        elif x.tag == 'RelatedRegistryNumberList':
                            concept[x.tag] = []
                            ## Append each child Registry Number to list
                            for child2 in x:
                                concept[x.tag].append(child2.text)

                        ## If 'ConceptRelationList', define as empty list
                        elif x.tag == "ConceptRelationList":
                            concept[x.tag] = []

                            ## Loop each Relation, define as empty dictionary
                            for child2 in x:
                                relation = {}
                                ## Define RelationName attribute -- required, will always be included
                                relation['@RelationName'] = child2.attrib['RelationName']

                                ## Loop child elements, add to dictionary
                                for child3 in child2:
                                    relation[child3.tag] = child3.text

                                ## Append concept dictionary to concept list
                                concept[x.tag].append(relation)

                        ## If 'TermList', define as empty list
                        elif x.tag == "TermList":
                            concept[x.tag] = []

                            ## Loop individual terms, define as dictionary
                            for child2 in x:
                                term = {}

                                ## Loop attributes in term, add to dictionary
                                for attribute, value in child2.items():
                                    term['@'+attribute] = value

                                ## Loop child elements
                                for child3 in child2:
                                    ## If 'TermName', get value from child string element
                                    if child3.tag == 'TermName':
                                        for child4 in child3:
                                            term[child3.tag] = child4.text

                                    ## If 'DateCreated', define dictionary for date
                                    elif child3.tag == 'DateCreated':
                                        term[child3.tag] = {}

                                        ## Loop date components (Year-Month-Day)
                                        for child4 in child3:
                                            term[child3.tag][child4.tag] = child4.text

                                    ## If 'ThesaurusIDlist', define empty list
                                    elif child3.tag == 'ThesaurusIDlist':
                                        term[child3.tag] = []

                                        ## Loop ThesaurusIDs, append to list
                                        for child4 in child3:
                                            term[child3.tag].append(child4.text)

                                    ## Otherwise, element equals element value
                                    else:
                                        term[child3.tag] = child3.text.strip()

                                concept[x.tag].append(term)

                        ## Otherwise, element equals element value
                        else:
                            concept[x.tag] = x.text

                    ## Append concept to concept list
                    DescriptorRecord[element.tag].append(concept)

            ## If element is 'EntryCombinationList', define as empty list
            elif element.tag == 'EntryCombinationList':
                DescriptorRecord[element.tag] = []

                ## Loop each entry combination, define empty dictionary
                for child in element:
                    entry = {}

                    ## Loop ECIN and ECOUT, define as empty dictionary
                    for child2 in child:
                        entry[child2.tag] = {}

                        ## Loop descriptor and qualifier, define as empty dictionary
                        for child3 in child2:
                            entry[child2.tag][child3.tag] = {}

                            ## Loop ID and Name
                            for child4 in child3:

                                ## If name, get string from child element
                                if 'Name' in child4.tag:
                                    for child5 in child4:
                                        entry[child2.tag][child3.tag][child4.tag] = child5.text

                                ## Otherwise, element is element text
                                else:
                                    entry[child2.tag][child3.tag][child4.tag] = child4.text

                ## Append entry to entry list
                DescriptorRecord[element.tag].append(entry)

            ## Otherwise, element is element text
            else:
                DescriptorRecord[element.tag] = element.text.strip()

    ## Add descriptor to descriptor set dictionary, with descriptorUI as key
    DescriptorRecordSet[DescriptorRecord['DescriptorUI']] = DescriptorRecord

## Convert dictionary to JSON
json_object = json.dumps(DescriptorRecordSet)

# Writing to mesh.json
with open("mesh.json", "w") as outfile:
    outfile.write(json_object)
