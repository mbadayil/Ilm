s="aaaaasdasd"
idx,idx1=0,1
len1=len(s)
s1=""
res=[]
while idx1<len1:
    if s[idx]==s[idx1]:
        s1+=s[idx]
        idx+=1
        idx1+=1
    else:
        s1+=s[idx]
        if len(s1)>2:
            print("break")
        else:
            res.append(s1)
            idx+=1
            idx1+=1
            s1=""
res.append(s1)

print(res, idx, idx1)
