

def twoArrayIntersection(arr1: list, arr2: list):
    """
        args : list1 - list of elements
               list2 - list if elements
        return : list of common elements from both list
    """
    newArr = list(set(arr1) & set(arr2))
    return newArr

a = [1, 2, 2, 3]
b = [2, 3, 4]

result = twoArrayIntersection(a, b)
print(result)