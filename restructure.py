file1 = open("myTabListing.txt", "r")
myDict = {}
for line in file1.readlines():
    temp = line.strip()
    categories = temp.split("#")
    if categories[0] not in myDict:
        myDict[categories[0]] = {}
    if categories[1] not in myDict[categories[0]]:
        myDict[categories[0]][categories[1]] = []
    if not (categories[2] in myDict[categories[0]][categories[1]]):
        (myDict[categories[0]][categories[1]]).append(categories[2])
    
for (m1, m1val) in myDict.items():
    print(m1)
    for m2, m2val in m1val.items():
        print("\t" + m2)
        for m3 in m2val:
            print("\t\t"+m3)

