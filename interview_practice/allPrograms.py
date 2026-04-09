from collections import defaultdict

# Return max length common prefix
def commonPrefix(strList: list) -> str:
    prefix = strList[0]
    for word in strList[1 : ]:
        while not word.startswith(prefix):
            prefix = prefix[: -1]
            if not prefix:
                return " "
    return prefix


# strs = ["appple", "apppa", "apppu"]
# res = commonPrefix(strs)
# print(res)


# group anagrams
def anagramGrouping(strsList: list) -> dict:
    def_dict = defaultdict(list)
    for word in strsList:
        def_dict["".join(sorted(word))].append(word)
    return list(def_dict.values())

# strList = ["eat", "tea", "tan", "ate", "nat", "bat"]
# result = anagramGrouping(strList)
# print(result)


def commonElements(list1: list, list2: list) -> list:
    """
    args : 
        list1 : list of elements
        list2 : list of elements
    return : 
        list of common elements from both list
    """
    return list(set(list1) & set(list2))

# a = [1, 2, 2, 3]
# b = [2, 3, 4]

# result = commonElements(a, b)
# print(result)


def mergeSortedArray(arr1: list, arr2: list) -> list:
    """
        args : 
            arr1: list of sorted element
            arr2: list of sorted elements
        logic :
            merge the two sorted arrays
        return : 
            return the merged sorted arrays
    """
    i = j = 0
    sortedArray = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sortedArray.append(arr1[i])
            i += 1
        else:
            sortedArray.append(arr2[j])
            j += 1
    sortedArray.extend(arr1[i:])
    sortedArray.extend(arr2[j:])
    return sortedArray


# a = [1,2,3,4,5,6]
# b = [2,3,4,5,6,7,8,9]
# result = mergeSortedArray(a,b)
# print(result)

def binarySearch(arr1: list, target: int) -> int:
    """
        args :
            arr1 : sorted list of values
            target : int number to search in arr1
        logic : 
            perform binary search and find the target from the list
        return :
            return the index of target number from arr1, if not found return -1
    """
    low, high = 0, len(arr1) - 1
    while low <= high:
        midIndex = (low + high) //2
        midValue = arr1[midIndex]
        if midValue == target:
            return midIndex
        elif midValue < target:
            low = midIndex + 1
        elif midValue > target:
            high = midIndex - 1
    return -1


arr1 = [1,2,3,4,5,6,7, 8]
target = 8
result = binarySearch(arr1, target)
print(result)
