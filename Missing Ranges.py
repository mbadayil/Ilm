l1=[0, 1, 3, 50, 75]


def missingRange(num):
    l2,idx,idx1=[],0,1
    if l1[-1]!=100:
        l1.append(100)
        while idx1<len(l1):
            if l1[idx1]-l1[idx]==1:
                idx+=1
                idx1+=1
            elif l1[idx1]-l1[idx]==2:
                l2.append(str(l1[idx]+1))
                idx+=1
                idx1+=1
            elif l1[idx1]-l1[idx]>2:
                l2.append((str(l1[idx]+1),str(l1[idx1]-1)))
                idx+=1
                idx1+=1
    return l2

print(missingRange(l1))
