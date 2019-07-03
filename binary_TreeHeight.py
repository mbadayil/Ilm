# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """


        if root is None:
            return 0
        if root.left and root.right:
            return max(self.maxDepth(root.left), self.maxDepth(root.right))+1
        elif root.left:
            return self.maxDepth(root.left)+1
        elif root.right:
            return self.maxDepth(root.right)+1
        else:
            return 1
