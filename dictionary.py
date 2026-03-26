data = {3: "Banana", 1: "Apple", 2: "Orange", }
# print(sorted(data))
keyList = sorted(data)

sortedData = {}
for k in keyList:
    newKV = {k: data[k]}
    sortedData.update(newKV)
# print(sortedData)

# print(f"Data details are {data.items()}")

#Program to create a dictionary for a number and its cube
def calcCube():
    cubeDict = {}
    keyNum = eval(input("Enter Number: "))
    if keyNum:
        for n in range(keyNum+1):
            cubeDict[n] = n * n * n
    return cubeDict
# print(cubeDict)        

#Program to determine the total amount of all the products.”
def calcDictValSum():
    product= {'Book': 800, 'Shirt':1000, 'Mobile': 15000, 'Laptop': 35000}
    productVal = product.values()
    print(type(productVal))
    totalVal = sum(productVal)
    print(totalVal)

#Program to determine number of upper, lower case letters in sentence.

def countChar(charString):
    charCount = {"upper": 0, "lower": 0}
    for char in charString:
        if char.islower():
            charCount["lower"] += 1
        if char.isupper():
            charCount["upper"] += 1
    return charCount

# data = countChar("Hello World")
# print(data) 

#Program to calculate the number of letters and digits in a string.”

def charCalc(charString):
    charcount = {"number": 0, "letters": 0, "upper": 0, "lower": 0}
    for char in charString:
        if char.isdigit():
            charcount["number"] += 1
        if char.isalpha():
            charcount["letters"] += 1
        if char.islower():
            charcount["lower"] += 1
        if char.isupper():
            charcount["upper"] += 1
    return charcount

# data = charCalc("Hello World to Python 3")
# print(data) 


def nosFriends():
    friends = {}
    count = 0
    name = ''
    while (name != "stop"):
        name = input("Friends Name? :  ")
        if name != "stop":
            count += 1
            friends[count] = name
    print("Total Friends: ", count)
    maxCharName = ''
    nameLength = 0
    for n in friends.values():
        if len(n) > nameLength:
            maxCharName = n
            nameLength = len(n)
    print(f"All friends: {friends}")
    print(f"Name with max Char: {maxCharName}")
    print(f"Length of maxCharName: {len(maxCharName)}")
    return friends

# data = nosFriends()
# print(data)
    
test=[80,50,40,20,30,40,30,60,30,60,90,40]
print(test[-3:])
print(test.count(40))

