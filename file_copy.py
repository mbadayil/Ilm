"""
import os
with open ('file.txt','r') as f1:
    f_contents=f1.read()
    print(f_contents)


print(os.c
"""
s="ABA"

for i in  range(0,len(s)):
    if s[i]==s[len(s)-1-i]:
        print("yes")
    print("no")
