# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        

        def height(root):

            if not root:
                return -1

            left = height(root.left)
            right = height(root.right)

            diff = left - right
            print(diff, " diff ")
            if not -1 <= diff <= 1 :
                return False

            return 1 + max(left,right)

        maxH = height(root)
        print(maxH)
        if maxH is False:return False
        return True


class neetCode(object):

    def isBalanced(self, root):

        def dfs(root):

            if not root:
                return [True, 0]

            left,right = dfs(root.left), dfs(root.right)

            balance = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            return [balance, 1 +max(left[1], right[1])]

        res = dfs(root)
        return res[0]

T6 = TreeNode(6,None,None)
T7 = TreeNode(7,None,None)
T4 = TreeNode(4,T6,None)
T5 = TreeNode(5,None,T7)
T3 = TreeNode(3,None,T5)
T2 = TreeNode(2,T4,None)
T1 = TreeNode(1,T2,T3)

obj = neetCode()
ans = obj.isBalanced(T1)

print(ans)

# [1,2,2,3,null,null,3,4,null,null,4]