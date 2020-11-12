def bs(arr, first, end, target):
    if first<=end:
        mid = (end - first + first) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] > target:
            return bs(arr, mid+1, end, target)
        
        else:
            return bs(arr, first, mid+1, bs)

class Solution(object):
    def search(self, nums, target, start=0, end=None):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        
        start, end = 0, len(nums)-1
        while (start<=end):
            mid = start + (end-start)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1

sol = Solution()
print(sol.search([-1,0,3,5,9,12], 9))
            
