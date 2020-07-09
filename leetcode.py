import time

'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''
class Solution:
    def bruteForce(self, nums, target):
        seen = list()
        for i in nums:
            for j in nums:
                if target == (i+j):
                    array.append(i)
        return array

    def twoSum(self, nums, target):
        """
        type nums: int
        type target : int
        """
        start = time.time()
        seen = dict()
    
        for index, value in enumerate(nums):
            remaining = target - value
            if remaining not in seen:
                seen[value] = index
            else:
                print(seen)
                return [seen[remaining], index]

        return []

sol = Solution()
# print(sol.bruteForce([2,3,4,8], 10))
print(sol.twoSum([2,3,4,8], 10))