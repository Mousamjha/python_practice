

def mergeSortedArrays(arr1, arr2):
    i = 0
    j = 0
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


a = [1,2,3,4,5,6]
b = [2,3,4,5,6,7,8,9]
result = mergeSortedArrays(a,b)
print(result)