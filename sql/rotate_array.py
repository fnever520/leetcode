# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]


class Solution(object):
    def rotate(self, nums, k):
        
        clone_nums = nums[:]

        for i in range(len(nums)):
            clone_nums[(i+k)%len(nums)] = nums[i]

        for i in range(len(clone_nums)):
            nums[i] = clone_nums[i]
