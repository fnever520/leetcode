class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def findminMax(node):
    if node is None:
        return float("-inf")

    temp = node.data
    ltemp = findminMax(node.left)
    rtemp = findminMax(node.right)

    if ltemp > temp:
        temp = ltemp
    if rtemp > temp:
        temp = rtemp

    return temp
    

root = Node(2)  
root.left     = Node(7)  
root.right     = Node(5)  
root.left.right = Node(6)  
root.left.right.left=Node(1)  
root.left.right.right=Node(11)  
root.right.right=Node(9)  
root.right.right.left=Node(4)

print(findminMax(root))