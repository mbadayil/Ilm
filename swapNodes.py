l1=[1, 1, 2, 4,5]
l2=[2,4]

def swapNodes(l1):
    len1=len(l1)
    i=0

    while i<len1:
        if len(l1)%2!=0:
            l1[i],l1[i+1]=l1[i+1],l1[i]
            i+=1
            len1-=1
        else:
            l1[i],l1[i+1]=l1[i+1],l1[i]
            i+=1
            len1-=1
    return l1

print(swapNodes(l1))
