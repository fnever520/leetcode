"""
you are given a string consisitngs of lowercase letter of the english alphabet. You must split this string into minimal number of substrings in such a way that no letter occurs more than once in each substring. 

for example, here are the correct split of the string "abacdec": ("a", "bac", "dec), ("a", "bacd", "ec") and ("ab", "ac", "dec")

write a  function that given string S of length N, returns the minimum number of substring into which string has to be split.
"""

def unique_substring(string):
    last_occurence = {}p
    start = 0 
    count = 0

    for i in range(len(string)):
        if string[i] in last_occurence:
            start = max(start, last_occurence[string[i]] + 1)
        last_occurence[string[i]] = i

        if i + 1 == len(string) or \
            string[i+1] in last_occurence and last_occurence[string[i+1]] >= start:
            count += 1
            start = i + 1

    return count

print(unique_substring('abcabc'))
# print(unique_substring('world'))