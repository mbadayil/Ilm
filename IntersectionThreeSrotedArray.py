l1=[2,6,9,11,13,17]
l2=[3,6,7,10,13,18]
l3=[4,5,6,9,11,13]
def findInterSection(l1,l2,l3):
    res=[]
    x,y,z=0,0,0
    while x<len(l1) and y<len(l2) and z <len(l3):
        if (l1[x]==l2[y] and l2[y]==l3[z]):
            res.append(l1[x])
            x+=1
            y+=1
            z+=1
        elif l1[x]<l2[y]:
            x+=1
        elif l2[y]<l3[z]:
            y+=1
        else:
            z+=1
    return res


print(findInterSection(l1,l2,l3))
