# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        def compare(a,b):
            if a is None and b is None:
                return True
            elif a and b:
                if a.val != b.val:
                    return False

                left = compare(a.left, b.left)
                right = compare(a.right, b.right)

                bal = left and right 
                if bal is None:
                    return True
                return bal 
            return False
        return  compare(p,q)

        

T6 = TreeNode(6,None,None)
T7 = TreeNode(7,None,None)
T4 = TreeNode(4,T6,None)
T5 = TreeNode(5,None,T7)
T3 = TreeNode(3,None,T5)
T2 = TreeNode(2,T4,None)
T1 = TreeNode(1,T2,T3)


obj = Solution()
ans = obj.isSameTree(T1,T1)

print(ans)