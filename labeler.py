import re

def my_replace(match):
    # print(match.group(3))
    match = match.group()
    match1 = re.sub(r'%', r"'", match)
    match2 = re.sub(r'@', r'"', match1)
    return re.sub(r'`', r'"', match2)

testFile = open("try2.txt")

bigString = testFile.read();
# for line in testFile:
    # print(line)
print(bigString)
myStrings = bigString.split("\n\n")
s1 = '[.!?]\'\s'
s2 = '([A-Z0-9]+[A-Za-z\s\'0-9\-,/"\(\)~]+[.!?])([\s\Z])'
s3 = '\.\.\.'
s4 = '~'
p = re.compile(s2)
p1 = re.compile(s3)
finalString = "<Reviews>\n"
i = 0
for myStr in myStrings:
    myStr = p1.sub(r'~', myStr)
    string = p.sub(r'\t\t\t<sentence id=":">\n\t\t\t\t<text>\n\t\t\t\t\t\1\n\t\t\t\t</text>\n\t\t\t\t<Opinions>\n\t\t\t\t\t<Opinion category="" polarity="" implicit="" />\n\t\t\t\t</Opinions>\n\t\t\t</sentence>\n', myStr)
# print(string)
    finalString += "\t<Review rid=\""+str(i)+"\">\n\t\t<sentences>\n"+string+"\t\t</sentences>\n\t</Review>\n"
    i += 1
# print(string2)
finalString += "</Reviews>"

p2 = re.compile(s4)
finalString = p2.sub(r'...', finalString)

with open('out.xml', 'w') as myFile:
    myFile.write(finalString)
exit();

# s3 = '[A-Za-z]\'[a-z]|(s\')'

# S1 = '([A-Za-z]+)\'([a-z])' # replace with $1#$2
# S2 = '(s)\'' # replace with $1#
# S3 = '\'([A-Za-z ]*)\'' # replace with ~$1~
# S4 = '(\n| )\'([A-Za-z\#\s\(\).,!?;-]+[.,!?;\-])\'(\s)' # replace with $1%$2%$3
# S5 = '(\n| )\'([A-Za-z\#\%\s\~\(\).,!?;-]+[.,!?;\-])\'(\s)' # replace with $1@$2`$3
# S6 = '(\n| )\'([A-Za-z\#\s\(\).,!?;-]+[.,!?;\-\s])\'(\s)' # replace with $1%$2%$3 exception
# S7 = '\@((.|\n)*?)\%((.|\n)*?)\%((.|\n)*?)\`' # replace "$1'$3'$5"
# S8 = '[%]' # replace with "
# S9 = '[#~]' # replace with '

# p = re.compile(S1)
# string1 = p.sub(r'\1#\2', bigString)
# #print(string1)
# p2 = re.compile(S2)
# string2 = p2.sub(r'\1#', string1)

# p3 = re.compile(S3)
# string3 = p3.sub(r'~\1~', string2)

# p4 = re.compile(S4)
# string4 = p4.sub(r'\1%\2%\3', string3)

# p5 = re.compile(S5)
# string5 = p5.sub(r'\1@\2`\3', string4)


# p6 = re.compile(S6)
# string6 = p6.sub(r'\1%\2%\3', string5)


# with open('try1.txt', 'w') as myFile:
#     myFile.write(string6)

# # print(p6.findall(string5))
# # print(p6.findall(string6))

# p7 = re.compile(S7)
# string7 = p7.sub(my_replace, string6)
# # print(len(p7.findall(string6)))

# with open('try2.txt', 'w') as myFile:
#     myFile.write(string7)

# p8 = re.compile(S8)
# string8 = re.sub(S9, r"'", p8.sub(r'"', string7))

# with open('q1a.txt', 'w') as myFile:
#     myFile.write(string8)

# exit()


# S3a = '( )\'([A-Za-z\#\s\(\).,.!?;-]+[.,.!?;(--)])\'(\s)'
# S4a = '\n\'[A-Za-z\#\s\(\).,.!?;-]+[.,.!?;(--)]\'\s'
# p = re.compile(s2)
# p1 = re.compile(s1)
# s = '\'These are my friends. Happy friends.\' Cool? '

# m = p.finditer(s)
# m1 = p1.finditer(s)
# print("String: "+s)
# for n in m:
#     print(n.group())

# # ((\n')|( '))[A-Za-z\s.,.!?;]+\'\s

# # ((\n')|( '))[A-Za-z\s.,.!?;-]+[.,.!?;(--)]\'\s

# # (\n'| ')[A-Za-z\s.,.!?;-]+[.,.!?;(--)]\'\s

# # (\n| )'([A-Za-z\#\s\(\).,!?;-]+[.,!?;\-])\'(\s) # working