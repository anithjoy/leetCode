# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        """i am going visit the root, func(left) then func(right) . 
        func left right will give me some number. i will create a variable if variable is greater than current number then replace the number else ignore."""
        
        
        diameter = 0
        def func(root):
            
            nonlocal diameter
            

            if not root:
                return 0

            left = 1 + func(root.left,)
            right = 1 + func(root.right)

            newDiameter = max(diameter,left,right)

            if diameter > newDiameter:
                diameter = newDiameter

            return 1     #return some int statement 

        func(root)

        return diameter

class neetCode(object):

    def diameterOfBinaryTree(self,root):

        res = [0]

        def dfs(root):
            
            if not root:
                return -1

            left = dfs(root.left)
            right = dfs(root.right)

            res[0] = max(res[0],2+ left + right ) 
         
            return 1 + max(left,right)

        dfs(root)
        return res[0]


T3 = TreeNode(3,None,None)
T4 = TreeNode(4,None,None)
T5 = TreeNode(5,None,None)
T2 = TreeNode(2,T4,T5)
T1 = TreeNode(1,T2,T3)

obj = neetCode()
ans = obj.diameterOfBinaryTree(T1)

print(ans)