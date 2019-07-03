l1=[10,7,12,4,7,9,13]

def countSort(l1):
    range_list,count_list,sum_list,result,sum1=[],[],[],[],0
    range_list=[x for x in range(min(l1),max(l1)+1)]
    count_list=[l1.count(x) for x in range_list]
    result=[x for x in range(len(l1))]
    for i in count_list:
        sum1+=i
        sum_list.append(sum1)
    for i in l1:
        if i in range_list:
            idx=range_list.index(i)
            idx=sum_list[idx]
            idx=idx-1
            result[idx]=i

    return result

countSort(l1)
