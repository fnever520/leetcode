'''
Given a(singly) linked list with head node root, write a function to split the linked list into k consecutive linked list "parts".

The length of each part should be as equal as possible: no two parts should have a size differing by more than 1. This may lead to some parts being null.

The parts should be in order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal parts occurring later.

Return a List of ListNode's representing the linked list parts that are formed.

Examples 1 -> 2 -> 3 -> 4, k = 5 // 5 equal parts[[1], [2], [3], [4], null]
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        cur = root
        for N in xrange(1001):
            if not cur:
                break
            cur = cur.next
        width, remainder = divmod(N, k)
        
        ans = []
        cur = root
        for i in xrange(k):
            head = cur
            for j in xrange(width + (i< remainder) -1):
                if cur:
                    cur = cur.next
            if cur:
                cur.next, cur = None, cur.next
            ans.append(head)
            
        return ans
