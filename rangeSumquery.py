l1=[-2, 0, 3, -5, 2, -1]

def sumRange(array1, i, j):
    """
        :type i: int
        :type j: int
        :rtype: int
        """
    return sum(array1[i:j+1])

print(sumRange(l1, 0, 5))
