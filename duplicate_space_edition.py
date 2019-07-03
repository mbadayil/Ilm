l1=[1,2,3,4,5,3,2,1,5]

def finDuplicate(l1):
    l2=[]
    for x in l1:
        if x not in l2:
            l2.append(x)
    #l2=[x for x in l1 if l1.count(x)>1 and x not in l2]
    return l2

finDuplicate(l1)
