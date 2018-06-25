import xml.etree.ElementTree as ET
import sys
import itertools

def process(mySet):
    a = []
    for el in mySet:
        # a.append((el.attrib['category'],el.attrib['polarity'],el.attrib['implicit']))
        a.append((el.attrib['category']))
    return a

if (len(sys.argv) <= 1):
    file1 = 'laptopReviews.xml'
    file2 = 'gayathri/laptopReviewsInter.xml'
else:
    file1 = sys.argv[1]
    file2 = sys.argv[2]

tree1 = ET.parse(file1)
tree2 = ET.parse(file2)

root1 = tree1.getroot()
root2 = tree2.getroot()

# print root1[0]
# print root2[0]
sum1 = 0 # number of different labels
sum2 = 0 # number of same labels
sum3 = 0 # number of different sentences
sum4 = 0 # total number of sentences
y = []
for rev1, rev2 in itertools.izip(root1, root2):
    s1 = (rev1.findall('sentences'))[0]
    s2 = (rev2.findall('sentences'))[0]
    # sum1 = 0 # number of different labels
    # sum2 = 0 # number of same labels
    # sum3 = 0 # number of different sentences
    # sum4 = 0 # total number of sentences
    for sen1, sen2 in itertools.izip(s1, s2):
        sum4 += 1
        if (sen1[0].text != sen2[0].text):
            sum3 += 1
        ops1 = sen1[1]
        ops2 = sen2[1]
        op1 = process(ops1)
        op2 = process(ops2)
        # exit()
        # print(op1)
        # print(op2)
        t1 = sum1
        myset = set(op1).symmetric_difference(set(op2))
        sum1 += len(myset)
        # if bool(myset):
            # print(myset)
        t2 = sum2
        sum2 += len(set(op1)&set(op2))
        # print(set(op1)&set(op2))
    # y.append([sum1, sum2, sum3, sum4])
    # break

# print(y)
print( sum1, sum2, sum3, sum4 )
# mySentences = root[0][0]

# pCategoryDict = {}
# nCategoryDict = {}
# cCategoryDict = {}

# sum3 = 0
# for review in root:
#     mySentences = (review.findall('sentences'))[0]
#     for sentence in mySentences:
#         text = sentence[0]
#         opinions = sentence[1]
#         for opinion in opinions:
#             if (not (pCategoryDict.has_key(opinion.attrib['category']))):
#                 pCategoryDict[opinion.attrib['category']] = 0
#                 nCategoryDict[opinion.attrib['category']] = 0
#                 cCategoryDict[opinion.attrib['category']] = 0
#             if (opinion.attrib['implicit'] == "true"):
#                 pCategoryDict[opinion.attrib['category']] += 1
#             elif (opinion.attrib['implicit'] == "false"):
#                 nCategoryDict[opinion.attrib['category']] += 1
#             else:
#                 cCategoryDict[opinion.attrib['category']] += 1

# sum1 = 0
# sum2 = 0

# print "Counts: "
# print sum(pCategoryDict.values())
# print sum(nCategoryDict.values())
# print sum(cCategoryDict.values())

# print "Implicit:"

# for key, val in pCategoryDict.iteritems():
#     if val != 0:
#         print str(key)+" : " + str(val)

# print "\nExplicit:"

# for key, val in nCategoryDict.iteritems():
#     if val != 0:
#         print str(key)+" : " + str(val)

# print "\nCoreference:"

# for key, val in cCategoryDict.iteritems():
#     if val != 0:
#         print str(key)+" : " + str(val)
