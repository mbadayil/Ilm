meeting=[(0, 1), (3, 5), (4, 8), (9, 10),(10, 12), (13, 15), (14, 18)]
meeting=sorted(meeting)
result=[]
idx,ele=0,0
#for i in range(len(meeting)):
len1=len(meeting)
while idx<len1:
    #print(idx,ele,len(meeting))
    if meeting[idx][ele+1]< meeting[idx+1][ele]:
        result.append((meeting[idx][ele+1],meeting[idx+1][ele]))
        idx+=1
        ele=0

    else:
        meeting[idx]=(meeting[idx][ele],meeting[idx+1][ele+1])
        meeting.remove(meeting[idx+1])
        idx+=1
        ele=0
        print(meeting)
    len1=len(meeting)
    len1-=1


'''
Work on fixing index issue
'''
#print(result)
print(meeting)
