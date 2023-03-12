# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # queue = deque()
        # rev = False

        # def innerfunc(root):
        #     if root is None:
        #         return None
        #     print(root.val)
        #     queue.append(root.left)
        #     queue.append(root.right)
        #     innerfunc(queue.popleft())
            
        # innerfunc(root) 


        res = [] #final result
        queue = deque([root] if root else [])

        while queue:
            level = [] #sub array to insert for each level
            for i in range(len(queue)):

                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level = reversed(level) if len(res) % 2 == 1 else level
            res.append(level)

        return res

            