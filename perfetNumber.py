def perfNum(num):
    sum=0
    factors=[]
    for i in range(2,num+1):
        if num%i==0:
            factors.append(i)
    return factors

    """
    if sum(factors) == num:
        return True
    else:
        return False
    """

print(perfNum(28))
