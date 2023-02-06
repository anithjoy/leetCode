# it will return the max node of the tree

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class solution(object):

    def max(self, root):

        if root is None:
            return -1

        left = self.max(root.left)
        right = self.max(root.right)

        return max(left, right,root.val)


T6 = TreeNode(6,None,None)
T7 = TreeNode(7,None,None)
T4 = TreeNode(4,T6,None)
T5 = TreeNode(5,None,T7)
T3 = TreeNode(3,None,T5)
T2 = TreeNode(2,T4,None)
T1 = TreeNode(1,T2,T3)


obj = solution()
ans = obj.max(T1)

print(ans)