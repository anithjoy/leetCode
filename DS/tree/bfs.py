from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = deque()

        def innerfunc(root):
            if root is None:
                return None
            print(root.val)
            queue.append(root.left)
            queue.append(root.right)
            innerfunc(queue.popleft())
            
        innerfunc(root)



T6 = TreeNode(6,None,None)
T7 = TreeNode(7,None,None)
T4 = TreeNode(4,None,None)
T5 = TreeNode(5,None,None)
T3 = TreeNode(3,T6,T7)
T2 = TreeNode(2,T4,T5)
T1 = TreeNode(1,T2,T3)
            

obj = Solution()
ans = obj.zigzagLevelOrder(T1)