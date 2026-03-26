"""Write a Python program to find the maximum of three numbers"""
def max_num(a, b, c):
    return max(a,b,c)

# print(max_num(2,5,3))

"""Write a Python program to count the number of vowels in a string"""
def vowelCount(string):
    vowels = {"a":0, "e": 0, "i": 0, "o": 0, "u": 0}
    count = 0
    for character in string.lower():
        for k, v in vowels.items():
            if character == k:
                vowels[k] += 1
            else:
                pass
    return vowels

# print(vowelCount("I Love YoU"))

"""Write a Python program to calculate the factorial of a number"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# print(factorial(5))

"""Write a Python code to merge two dictionaries"""
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
newdict = dict1|dict2
mergedDict = {**dict1, **dict2}
# print(newdict)
# print(mergedDict)

"""Write a Python program to find common elements in two lists"""
def commonElements(list1, list2):
    commonEle = [x for x in list1 if x in list2]
    return commonEle

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
# print(commonElements(list1, list2))

"""Write a Python code to remove duplicates from a list"""
def removeDuplicates(list3):
    return list(set(list3))

list3 = [1, 2, 3, 4, 3, 4, 5, 6]
# print(removeDuplicates(list3))


"""Write a Python code to check if a string is a palindrome"""
def checkPalindrome(string: str):
    if string == string[::-1]:
        return f"{string} is palindrome"
    else:
        return f"{string} is not palindrome"

# print(checkPalindrome("madam"))    


"""Write a Python program to find the longest word in a sentence"""
"""The fox jumps over the lazy dog"""
def maxWord(string):
    stringArray = string.split(" ")
    return max(stringArray, key=len)

# print(maxWord("The fox jumps over the lazy dog"))


"""Write a Python code to find the first non-repeating character in a string"""

def firstNonRepeatingChars(string):
    chars = {}
    for char in string:
        chars[char] = chars.get(char, 0) + 1
    for char in chars:
        if chars[char] == 1:
            return char
        
# print(firstNonRepeatingChars("nxntwave"))        

"""Write a Python code to count the number of uppercase letters in a string"""
def upperCase(string):
    case = {"upper": 0, "lower": 0}
    for char in string:
        if char.isupper():
            case["upper"] +=1
        else:
            case['lower'] +=1
    return case
# print(upperCase("The fox Jumps over the lazy dog")["upper"])    


"""Write a Python code to implement a binary search algorithm"""
def binarySearch(arr: list, target: int):
    sortedArray = sorted(arr)
    low, high = 0, len(sortedArray) - 1
    while low <= high:
        mid = (low + high) // 2
        print("mid: ", mid)
        if sortedArray[mid] < target:
            low = mid + 1
        elif sortedArray[mid] > target:
            high = mid - 1
            
        else:
            return mid
    return -1

# print(binarySearch([1, 4, 3, 6, 5], 4))  # 2


"""Write a Python code to implement a function to flatten a nested list"""
def flatten(list4):
    flatList = []
    for val in list4:
        if isinstance(val, list):
            flatList.extend(flatten(val))
        else:
            flatList.append(val)
    return flatList


# print(flatten([1, [2, [3, 4], 5], 6]))  # [1, 2, 3, 4, 5, 6]


"""Write a Python code to check if a number is a perfect square"""
def perfectSquare(num):
    return int(num ** 0.5) **2 == num

# print(perfectSquare(16))  # True
# print(perfectSquare(14))  # False

# print(int(14**0.5)**2)
# print((14**0.5)**2)

# Reverse the number
def reverseNumber(nos):
    reverse = 0
    while nos > 0:
        remainder = nos % 10
        reverse = (reverse * 10) + remainder
        nos = nos // 10
    return reverse

# print(reverseNumber(123456))

def fibonacciSeries(n):
    # fib = [0, 1]
    if n <= 0:
        return n
    elif n <= 1:
        return 1
    else:
        # fib.append(fibonacciSeries(n-1))
        
        return (fibonacciSeries(n-1) + fibonacciSeries(n-2))

print(fibonacciSeries(10))

def fibSeries(n):
    fib = [0, 1]
    for num in range(1, n):
        fib.append(fib[-1]+fib[-2])
    return fib

print(fibSeries(10))