'''
Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"
'''

from collections import defaultdict
class Solution:
   def destCity(self, paths):
        hashmap = defaultdict(list)
        seen = []
        for i, j in paths:
           hashmap[i] = j
           seen.append(i), seen.append(j)

        for x in seen:
            if not hashmap[x]:
                return x

sol= Solution()
print(sol.destCity(paths = [["B","C"],["D","B"],["C","A"]]))