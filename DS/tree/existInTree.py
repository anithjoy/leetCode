# it will return if the input value is in the tree else it will return false

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class solution(object):

    def existInTree(self, root, value):

        if root is None:
            return False
        elif root.val == value:
            return True
        
        left = self.existInTree(root.left, value)
        right = self.existInTree(root.right, value)

        return left or right

T6 = TreeNode(6,None,None)
T7 = TreeNode(7,None,None)
T4 = TreeNode(4,T6,None)
T5 = TreeNode(5,None,T7)
T3 = TreeNode(3,None,T5)
T2 = TreeNode(2,T4,None)
T1 = TreeNode(1,T2,T3)

obj = solution()
ans = obj.existInTree(T1,8)

print(ans)