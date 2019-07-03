s='abcde'
s1='abde'


def onEdit(s,s1):
    res=""
    if len(s)>len(s1):
        s2=[x for x in s if x not in s1]
        if len(s2)==1:
            for i in s:
                if i in s1:
                    res+=str(i)
                else:
                    res+='X'
    else:

        s2=[x for x in s if x not in s1]
        if len(s2)==1:
            for i in s:
                if i in s1:
                    res+=str(i)
                else:
                    res+='X'

    return res

print(onEdit(s, s1))
