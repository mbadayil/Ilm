import random
l1=[1, 2, 6, 5, 9]
def get_random(floor, ceiling):

    return random.randrange(floor, ceiling+1)

def shuffle(list1):
    if len(list1)<=1:
        return list1

    last_index=len(list1)-1

    for idx in range(0,len(list1)):
        random_idx=get_random(idx, last_index)
        #print(idx,random_idx)
        if random_idx!=idx:
            #print(idx,random_idx)
            list1[idx],list1[random_idx]=list1[random_idx],list1[idx]
    return list1


print(shuffle(l1))
