def min_substring(string):
    last_occurence = {char:index for index, char in enumerate(string)}

    j = anchor = 0
    ans = 0

    for i, c in enumerate(string):
        j = max(j, last_occurence[c])
        if i == j:
            ans += 1
            anchor = i + 1

    return ans

def min_substring_2(string):
    # last_occurence = {}
    # for i in range(len(string)):
    #     last_occurence[string[i]] = i
    
    last_occurence = {c:i for i, c in enumerate(string)}
    print(last_occurence)
    count = 0
    max_index =0
    for i in range(len(string)):
        max_index = max(max_index, last_occurence[string[i]])
        if i == max_index:
            count += 1
            max_index = i + 1

    return count

print(min_substring_2('aaabaab'))