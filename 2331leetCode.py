# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def evaluateTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        # top down approach 
        # base conditon for returning value for the left and right from the bottom

        # left side
        # right side

        # left and right side together should return some thing


        if root.val == 1:
            return 1
        elif root.val == 0:
            return 0

        left = self.evaluateTree(root.left)
        right = self.evaluateTree(root.right)
        if root.val == 3:
            return left and right
        else:
            return left or right


#  i ran this in leetcode environment and it ruturns true.
