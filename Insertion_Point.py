def InsPoint(nums, target):
    if target in nums:
        return nums.index(target)


    j=len(nums)-1
    for i in range(0,j):
        if nums[i]>=target:
            return i

print(InsPoint([1,2,5,6],0))
