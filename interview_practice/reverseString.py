

def reverseString(strs):
    i = len(strs)-1
    rev = ''
    while i < (len(strs)-1) and i = 0:
        rev += strs[i]
        i -= 1
    return rev

print(reverseString("apple"))
