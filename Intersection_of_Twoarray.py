'''
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
'''

class Solution(object):
    def intersect(self,num1, num2):
        
        num1.sort()
        num2.sort()

        seen = []

        pos1 = 0
        pos2 = 0 

        while (pos1 < len(num1)) and (pos2 < len(num2)):
            if num[pos1] == num[pos2]:
                seen.append(num[pos1])
                pos1+=1
                pos2+=1
            elif num[pos1] < num[pos2]:
                pos1+=1
            else:
                pos2+=1
        
        return seen