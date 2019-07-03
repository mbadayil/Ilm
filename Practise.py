a=[[0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]]
len1=len(a)
list1=[]
for i in range(len1):
    if 0 in a[i]:
        for j in range(len(a[i])):
            if a[i][j]==0:
                list1.append((i,j))

'''
for idx, ele in list1:
    for i in range(len(a[idx])):
        a[idx][i]=0
        a[i][ele]=0
'''
print(list1)
print(a)
