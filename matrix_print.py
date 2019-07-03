a=[[0,1,2],
   [4,5,6],
   [7,8,9]]
print(a)
len1=len(a)
"""
for i in range(len1):
    print([a[len1-i-1][len1-i-1]])


for i in range(len(a)):
    print(a[i][i])

for i in range(len1):
    print(a[len1-1][i])



for i in range(len1):
    print(a[1][i])



i,j=0,0
for i in range(len1):
    while i>0:
        print(a[i][j])
        i-=1
        j+=1
"""


i,j=0,0
for i in range(len1):
    while i>0:
        print(a[i][j], i,j)
        i-=1
        j+=1
