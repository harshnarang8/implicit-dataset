import xml.etree.ElementTree as ET

tree = ET.parse('mobileReviews.xml')

root = tree.getroot()

mySentences = root[0][0]

pCategoryDict = {}
nCategoryDict = {}
cCategoryDict = {}

sum3 = 0
for review in root:
    mySentences = (review.findall('sentences'))[0]
    for sentence in mySentences:
        text = sentence[0]
        opinions = sentence[1]
        for opinion in opinions:
            if (not (pCategoryDict.has_key(opinion.attrib['category']))):
                pCategoryDict[opinion.attrib['category']] = 0
                nCategoryDict[opinion.attrib['category']] = 0
                cCategoryDict[opinion.attrib['category']] = 0
            if (opinion.attrib['implicit'] == "true"):
                pCategoryDict[opinion.attrib['category']] += 1
            elif (opinion.attrib['implicit'] == "false"):
                nCategoryDict[opinion.attrib['category']] += 1
            else:
                cCategoryDict[opinion.attrib['category']] += 1

sum1 = 0
sum2 = 0

print "Implicit:"

for key, val in pCategoryDict.iteritems():
    if val != 0:
        print str(key)+" : " + str(val)

print "\nExplicit:"

for key, val in nCategoryDict.iteritems():
    if val != 0:
        print str(key)+" : " + str(val)

print "\nCoreference:"

for key, val in cCategoryDict.iteritems():
    if val != 0:
        print str(key)+" : " + str(val)
