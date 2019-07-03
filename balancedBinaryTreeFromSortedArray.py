# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         l1=[1,2,3,4,5,6,7]

class balancedTree():
    def arrayToBST(self,nums):
        if not nums or len(nums)==0:
            return None

        return self.myTree(nums, 0, len(nums)-1)


    def myTree(self, nums, start, end):
        if start> end:
            return None

        mid= start+(end-start)//2
        root=TreeNode(nums[mid])
        root.left=self.myTree(nums, start, mid-1)
        root.right=self.myTree(nums, mid+1, end)

        return root


a=balancedTree()
a.arrayToBST([-10,-3,0,5,9])
