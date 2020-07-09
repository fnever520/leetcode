"""
Find duplicate Number

Given an array nums containing n+1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example:
Input [1,3,4,2,2]
Output: 2

You must not modify the array ( assume the array is read-only)
You must use only constant, O(1) extra space
Your runtime complexity should be less that O(n2)
There is only one duplicate number in the array, but it could be repeated more than once
"""

def find_duplicate1(nums):
    # Linear scan
    nums.sort()
    for index, n in enumerate(nums):
        if nums[index] == nums[index+1]:
            return n

def find_duplicate2(nums):
    # Hashmap for reducing time complexity
    seen = {}
    for num in nums:
        if num in seen:
            return num
        seen[num] = True

def find_duplicate3(nums):
    # Floyd's Tortoise and Hare 
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break
    ptr1 =nums[0]
    ptr2 = tortoise
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]
        print(ptr1, ptr2)
    
    return ptr1



print(find_duplicate3([1,3,4,4,2]))
