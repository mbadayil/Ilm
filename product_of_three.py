nums=[1, 10, -5, 1, -100]
#print(sorted(nums))
assert len(nums) >= 3 # assume the input has been validated
a1 = nums[-1] * nums[-2] * nums[-3]
a2 = nums[0] * nums[1] * nums[-1]
#print(max(a1, a2))

'''You have a list of integers,
 and for each index you want to find the product of every integer except
 the integer at that index.'''
l1=  [1,2,6,5,9]
sum1=1
l2=[]
if len(nums)<3: print("None")
so=sorted(l1)
        #3 positive or two positive and one negative
print(max(so[-1]*so[-2]*so[-3],so[-1]*so[0]*so[1]))
