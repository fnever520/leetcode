'''
Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
'''

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        '''
        <1,2,3,4,5>
        <0,1,2,3,4,5>
        <0,1,2,'3',4 ,5>
        <0,1,2,'3',4,5,'None'>
        '''

        prev = ListNode(0)
        prev.next = head

        fast = slow = head

        for i in range(n+1):
            fast = fast.next

        while (fast != None):
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        
        return prev.next