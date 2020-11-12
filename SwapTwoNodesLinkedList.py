'''
Swap every two nodes in linked list

'''

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f"{self.data}, ({self.next.__repr__()})"

def swap_every_two(llist):
    head = llist

    curr = head
    while curr is not None and curr.next is not None:
        curr.data, curr.next.data = curr.next.data, curr.data
        curr = curr.next.next
        
    return head

llist = Node(2, Node(1, Node(4, Node(3, Node(5)))))
print(swap_every_two(llist))