
from collections import Counter

def findDuplicates(arr1):
    newCounter = Counter(arr1)
    duplicates = [k for k, v in newCounter.items() if v > 1]
    print(duplicates)


def find_duplicates(arr1):
    dup = set()
    seen = set()
    for x in arr1:
        if x not in seen:
            dup.add(x)
        else:
            seen.add(x)
    return list(dup)
arr = [1,2,2,2,3,4,5,5,5,6,6,7]
# findDuplicates(arr)    