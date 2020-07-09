'''
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
'''

class Solution(object):
    def reverseString(self,s):
        first = 0
        end = len(s) - 1

        while (first < end):
            s[end], s[first] = s[first], s[end]
            first += 1
            end -= 1