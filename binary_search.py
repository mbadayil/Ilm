l1=  [1,2,6,5,9,10,11,15]

def bin_search(l1,num, start, end):
    l1=sorted(l1)
    mid=start+(end-start)//2

    if l1[mid]==num:
        return mid
    else:
        if num<l1[mid]:
            return bin_search(l1, num, start, mid-1)
        else:
            return bin_search(l1, num, mid+1, end)



print(bin_search(l1,15,0,8))
