a=3
b=[1,2,1,3]

def flightMovie(fTime,Mtime):
    sum1=set()
    for idx, ele in enumerate(Mtime):
        travel=fTime-ele
        if travel in Mtime:
            return True
        sum1.add(ele)
        print(sum1)
    return False
flightMovie(a, b)
