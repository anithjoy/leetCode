# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        list = []
        def inorder(element):
            
            if not element:
                return 
            inorder(element.left)
            list.append(element.val)
            inorder(element.right)

        inorder(root)
        return list