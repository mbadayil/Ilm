def longPal(s):
    len1=0
    l2=[]
    s1=s[0]
    idx=1
    for i in s:
        s1=i
        for j in s[idx:]:
            s1+=j
            #print(s1)
            if s1==s1[::-1]:
                l2.append(s1)
        idx+=1
    max1=0
    s2=""
    for i in l2:
        if len(i)>max1:
            max1=len(i)
            s2=i
    #max1=[len(x) for x in l2]
    #return ax1
    return max1, s2


print(longPal("bbeeeeeebbbbbbbMALAYALAM"))
