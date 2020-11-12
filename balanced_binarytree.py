'''
Given a binary tree, determine if it is height-balanced
'''

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isBalanced(self, root):

        if root == None:
            return True

        left = self.findDepth(root.left)
        right = self.findDepth(root.right)

        return abs(left - right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def findDepth(self, root):
        if root == None:
            return 0

        left = self.findDepth(root.left)
        right = self.findDepth(root.right)
        return (max(left, right) + 1)

    # def dfs(self,root):
    #     if root == None:
    #         return 1
        
    #     left = self.dfs(root.left)
    #     if left < 0:
    #         return -1
    #     right = self.dfs(root.right)
    #     if right < 0:
    #         return -1
        
    #     if abs(left-right) > 1:
    #         return -1
        
    #     return max(left, right) + 1

root = TreeNode(1) 
root.left = TreeNode(2) 
root.right = TreeNode(3) 
root.left.left = TreeNode(4) 
root.left.right = TreeNode(5)
# root.left.left.left = TreeNode(6)


sol = Solution()
print(sol.isBalanced(root))