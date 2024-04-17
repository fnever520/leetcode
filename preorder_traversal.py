# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        nodes = []
        
        def traverse(root, arr):
            if root:
                arr.append(root.val)
                traverse(root.left, arr)
                traverse(root.right, arr)

        traverse(root, nodes)

        return nodes
    

