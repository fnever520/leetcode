def remove_duplicates(nums):
    len_ = 1
    if len(nums) == 0:
        return 0

    for index in range(1, len(nums)):
        if nums[index] != nums[index-1]:
            nums[len_] = nums[index]
            len_ += 1
    return nums[:len_]

nums = [0,0,1,2,2,3,3,4]
print(remove_duplicates(nums))