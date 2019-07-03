import string
s="aaaAAbc123"

def pwdChecker(str1):
    len1,lower,upper,digit,count=len(s),0,0,0,0

    if not len(str1) >=6<=20:
        return False

    for i in str1:
        if i in string.ascii_lowercase:
            lower+=1

    for i in str1:
        if i in string.ascii_uppercase:
            upper+=1

    for i in str1:
        if i in string.digits:
            digit+=1

    idx,res,first,idx1,len1=0,[],str1[0],1,len(str1)
    s1=""

    while idx1 < len1:
        if s[idx]==s[idx1]:
            s1+=s[idx]
            idx+=1
            idx1+=1
        else:
            s1+=s[idx]
            if len(s1)>2:
                return False
            else:
                res.append(s1)
                idx+=1
                idx1+=1
                s1=""
    s1+=s[idx]

    res.append(s1)
    if lower>1 and upper>1 and digit>1 and len(s1)<=2:
        return True
    return False

print(pwdChecker(s))
