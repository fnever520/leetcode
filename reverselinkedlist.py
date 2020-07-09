class LinkedList(object):
    def __init__(self, data=0):
        self.data = data
        self.next = None

class Solution(object):
    def reverse(self, head):
        # prev, current.next, current, head
        prev = None
        current = head

        while (current != None):
            current.next, prev, current = prev, current, current.next

        return prev