def retIndex(arr1):
    idx=1
    sum1=arr1[0] #sum1=3
    for i in range(1,len(arr1)):
        if sum1==sum(arr1[idx::]):
            return arr1.index(arr1[idx])
        else:
            idx+=1
            sum1+=arr1[i]