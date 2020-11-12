from collections import defaultdict

def preprocess(string):
    string = string.lower()
    string = [key.strip(",").strip(":") for key in string.split()]
    return "".join(string)

def check_palindrome(s):

    s = preprocess(s)
    seen = defaultdict(int)

    for i in s:
        seen[i] += 1

    odd_char = ""
    palindrome = ""

    for c, count in seen.items():
        if count % 2 == 0:
            palindrome += c * (count//2)
        elif not odd_char:
            odd_char = c
            palindrome += c * (count//2)
        else:
            # return None
            return False

    return palindrome + odd_char + palindrome[::-1]

print(check_palindrome("momom"))
print(check_palindrome("Papa"))
print(check_palindrome("A man, a plan, a canal: Panama"))