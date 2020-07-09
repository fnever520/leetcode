# Given a non-empty array of integers, every element appears twice except for one. Find that single one

# Approach 2: Hash table
from collections import defaultdict

class Solution(object):
    def singleNumber(object):
        seen = defaultdict(int)
        for i in nums:
            seen[i] += 1
        
        for i in seen:
            if seen[i] == 1:
                return i

# Approach 4: Bit Manipulation
class Solution(object):
    def singleNumber(self, nums):
        a = 0

        for i in nums:
            a ^= i
        
        return a
