import array

newArray = array.array("i", [])
for x in range(500, 800, 15):
    newArray.append(x)
print(newArray)
print(newArray[:-3])
print(newArray[-3:])
print(newArray[0])