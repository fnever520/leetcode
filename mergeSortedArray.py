'''
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
'''

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1_save = nums1[:]

        pos1 = 0
        pos2 = 0

        while (pos1 < m and pos2 < n):
            if nums1_save[pos1] <= nums2[pos2]:
                nums1[pos1+pos2] = nums1[pos1]
                pos1+=1
            else:
                nums1[pos1+pos2] = nums2[pos2]
                pos2+=1

        # handle the edge cases where the pointer is out of range
        if pos1 == m:
            nums1[pos1+pos2:] = nums2[pos2:]

        if pos2 == n:
            nums1[pos1+pos2:] = nums1[pos1:]
            