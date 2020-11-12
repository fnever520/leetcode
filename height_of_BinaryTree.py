class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def findHeight(node):
    if node == None:
        return 0
    left = findHeight(node.left)
    right = findHeight(node.right)
    return max(left, right)+1


# Driver program to test above function 
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5)

print(findHeight(root))