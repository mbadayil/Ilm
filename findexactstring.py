import re
with open ('/Users/mbadayil/Desktop/git/Ilm/test.txt') as f1:
    lines=f1.readlines()
    for line in lines:
        if re.findall('\\bis\\b',line):
            print(line)



#        print(str(search1))
#        exit()
