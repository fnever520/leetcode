'''
Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
'''

def remove_duplicates(nums):
    pointer = 1
    if len(nums) == 0:
        return 0

    for index in range(1, len(nums)):
        if nums[index] != nums[index-1]:
            nums[pointer] = nums[index]
            pointer += 1
    return nums[:pointer]

nums = [0,0,1,2,2,3,3,4]
print(remove_duplicates(nums))