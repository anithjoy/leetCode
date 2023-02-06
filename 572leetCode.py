# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if subRoot is None:
            return True

        if root is None:
            return False

        if self.innerFunc(root,subRoot):
            return True
        return (self.isSubtree(root.left,subRoot) or 
        self.isSubtree(root.right,subRoot))

        
            

    def innerFunc(self,a,b):

        if a is None and b is None:
            return True

        elif a and  b and a.val == b.val:
            left = self.innerFunc(a.left,b.left)
            right  = self.innerFunc(a.right,b.right)
            return left and right
        return False
            



T6 = TreeNode(6,None,None)
T7 = TreeNode(7,None,None)
T4 = TreeNode(4,T6,None)
T5 = TreeNode(5,None,T7)
T3 = TreeNode(3,None,T5)
T2 = TreeNode(2,T4,None)
T1 = TreeNode(1,T2,T3)


obj = Solution()

ans = obj.isSubtree(T1,T2)

print(ans)