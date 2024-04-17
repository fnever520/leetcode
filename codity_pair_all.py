'''
you are given an array of integers. your task is to create pair of them, such that every opair consinsts of equal number. each array element may belong to one pair only. is it possible to use all of the integer? 

'''
from collections import defaultdict

def can_pair_all(list_element):
    seen = {}
    for num in list_element:
        if num in seen:
            seen[num] += 1

        else:
            seen[num] = 1

    for num in seen:
        if seen[num] %2 != 0:
            return False
        
  
    # for key, value in seen:
    #     if value % 2 != 0:
    #         return False
        
    return True

print(can_pair_all([1,2,2,1]))