class ListNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution(object):
    def rotateRight(self, head, k)
        if not head or not head.next:
            return head
        
        # head
        # current
        # tail
        n = 1
        current = head

        while (current.next):
            current = current.next
            n += 1
        current.next = head

        current = head
        tail = current

        for _ in xrange(n - k%n):
            tail = current
            current = current.next
        tail.next = None

        return current
