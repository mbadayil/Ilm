l1=[1, 1, 2, 4]
l2=[2,4]

def addTwoNumbers(l1,l2):
    sum1,carry,res=0,0,[]

    if len(l1)!=len(l2):
        if len(l1)>len(l2):
            diff =len(l1)-len(l2)
            for i in range(diff):
                l2.insert(i,0)
        else:
            diff =len(l2)-len(l1)
            for i in range(diff):
                l1.insert(i,0)


    len1,idx=len(l1),0
    res=[x for x in range(len1)]
    while len1>0:
        sum1=l1[len1-1]+l2[len1-1]
        if sum1>=10:
            res[len1-1]=0+carry
            carry=1
            len1-=1
        else:
            sum1+=carry
            res[len1-1]=sum1
            carry=0
            len1-=1
    res1=""
    for i in res:
        res1+=str(i)
    return res,res1

print(addTwoNumbers(l1,l2))
