meeting=['a','b','c','d','e']
''' Best Solution with space'''
def revInplace(meeting):
    i,j=0,len(meeting)-1
    while i!=j:
        meeting[i],meeting[j]=meeting[j],meeting[i]
        i+=1
        j-=1
    return meeting

print(revInplace(meeting))
