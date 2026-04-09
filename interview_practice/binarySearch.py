

def binarySearch(sortedArray, target):
    sortedArray =list(reversed(sortedArray))
    low, high = 0, len(sortedArray) - 1
    print(f"low: {low}, high: {high}")
    while low <= high:
        midIndex = (low + high) // 2
        midValue = sortedArray[midIndex]
        print(f"low: {low}, high: {high}, midIndex: {midIndex}, midValue: {midValue}, target: {target}")
        if midValue == target:
            return midIndex
        elif midValue < target:
            high = midIndex + 1
        elif midValue > target:
            low = midIndex - 1

    return -1


arr1 = [1,2,3,4,5,6,7]
target = 6
result = binarySearch(arr1, target)
print(result)
            