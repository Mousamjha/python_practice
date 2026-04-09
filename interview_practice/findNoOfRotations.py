

def findRotationCount(arr):
    minValue = min(arr)
    findIdx = arr.index(minValue)
    noOfRotation = len(arr)+1 - findIdx
    return noOfRotation


arr = [3,5,7, 1,2]
findRotationCount(arr)    