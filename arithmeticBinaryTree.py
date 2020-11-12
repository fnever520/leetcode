class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

PLUS = "+"
MINUS = "-"
MULTIPLY = "*"
DIVIDE = "/"

def evaluate(root):
    if root.val == PLUS:
        return evaluate(root.left) + evaluate(root.right)
    elif root.val == MINUS:
        return evaluate(root.left) - evaluate(root.right)
    elif root.val == MULTIPLY:
        return evaluate(root.left) * evaluate(root.right)
    elif root.val == DIVIDE:
        return evaluate(root.left) / evaluate(root.right)
    else:
        return root.val

tree = Node(MULTIPLY)
tree.left = Node(PLUS)
tree.left.left = Node(3)
tree.left.right = Node(4)
tree.right = Node(PLUS)
tree.right.left = Node(4)
tree.right.right = Node(3)
print(evaluate(tree))
#print 49
