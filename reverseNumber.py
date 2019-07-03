n=123

def revNum(n):
    rev=0

    while n>0:
        remi=n%10
        rev=rev*10+remi
        n=n//10
    return rev

print(revNum(n))
