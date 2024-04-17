"""
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
"""

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 1
        right = 1
        ans = nums[0]

        for i in range(len(nums)):
            if left ==0:
                left = 1
            elif right == 0:
                right =1

            left *= nums[i]
            right *= nums[~i]

            # ans = max(ans, max(left, right))
            if max(left, right) > ans:
                ans = max(left, right)
        return ans


sol = Solution()
print(sol.maxProduct([2,3,-2,4]))