def revStr(str1):
    s1=""
    s2=""
    string_new=""
    #print(type(str1))
    if type(str1)!= str:
        print("Expected string input")
        return False

    for i in str1:
        if i.isalpha() or i==" ":
            string_new+=i

    for i in string_new:
        if i!=" ":
            s2+=i
        else:
            s1=s2+" "+s1
            s2=""
    s1=s2+" "+s1

    return s1.strip()

print(revStr("sky is blue"))
print(revStr("123"))
print(revStr("sky123 is blue"))
print(revStr("123 45"))
print(revStr("sjklasjdklasd@#$#@$@#$lkfgldkfglkdfkgld flgkd fgdl;fgk fd;glk "))
print(revStr("-343453345345"))
print(revStr("    sdffsd    "))
