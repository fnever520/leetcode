"""
write a function solutoin, that given a string S consisting of N characters, returns alphabatically smallest string that can be obtained by removing exactly one letter from S
"""

def solution(string):
    for i in range(len(string)-1):
        if string[i] > string[i+1]:
            return string[:i] + string[i+1:]
    return string[:-1]

print(solution('abedf'))