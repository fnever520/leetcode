class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
# Foyd Tortoise and Hare

class Solution(object):
    def hasCycle(self, head):
        if head == None:
            return False

        slow = head
        fast = head.next

        while (slow != fast):

            if (fast == None) or (fast.next == None):
                return False

            slow = slow.next
            fast = fast.next.next

        return True


first = ListNode(1)
sec = ListNode(5)

first.next = sec

sol = Solution()
print(sol.hasCycle(first))
