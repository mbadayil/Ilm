s="caam"
s1="aabc"
s3=s1


def canDoit(s, s1):
    len1=len(s)
    count1,idx=0,0
    for i in s:
        if s.count(i)!=s1.count(i):
            return False
        else:
            count1+=1
    if count1==len(s):
        return True


print(canDoit(s, s1))
