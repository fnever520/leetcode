class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        """
        create a stack that and two pointers - slow and fast pointer
        """
        if head == None:
            return True

        stack = []
        slow = fast = head

        while (fast and fast.next):
            stack.append(fast.val)
            slow = slow.next
            fast = fast.next.next

        if fast:
            slow = slow.next

        while (slow and len(stack)):
            if stack.pop() != slow.val:
                return False
            slow = slow.next

        return True
            