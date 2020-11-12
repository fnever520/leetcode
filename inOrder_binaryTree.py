'''
in order traversal
pre order traversal
post order traversal

'''

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution(object):
    def inOrderTraversal(self, root):
        if root == None:
            return []

        return self.inOrderTraversal(root.left)+ [root.data] +self.inOrderTraversal(root.right)


    def preOrderTraversal(self, root):
        if root == None:
            return []

        return [root.data] + self.preOrderTraversal(root.left) +self.preOrderTraversal(root.right)

    def postOrderTraversal(self, root):
        if root == None:
            return []

        return self.postOrderTraversal(root.right) + self.postOrderTraversal(root.left)+ [root.data] 

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5)
root.left.right.right = Node(6)


sol= Solution()
print(sol.inOrderTraversal(root))