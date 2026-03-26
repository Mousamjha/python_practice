# Write a Python program to check if a string is a palindrome.

def palindromeCheck(string):
    if string == string[::-1]:
        return "string is palindrome"
    else:
        return "string is non-palindrome"

# print(palindromeCheck("abc"))    
# print(palindromeCheck("aba"))

# Question 2: Write a Python program to find the factorial of a number.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
# print(factorial(10))    


# Question 2: Write a Python program to find the factorial series for a number.    
def factseries(n):
    fact = [1]
    for x in range(1,n):
        fact.append(fact[-1] + 1)
    return fact    
# print(factseries(10))    

# Question 3: Write a Python program to find the largest element in a list.
def findMaximum(li):
    import numpy as np
    arr = np.array(li)
    return arr.max()

def findMax(li):
    return max(li)

def maxFind(li):
    maxNum = 0
    for x in li:
        if x > maxNum:
            maxNum = x
    return maxNum
# print(maxFind([2,5,2,7,4,7,9,9,2,4]))


# Question 4: Write a Python program to reverse a string.

def reverseString(string):
    return string[: : -1]

# print(reverseString("Apple"))

# Question 5: Write a Python program to count the frequency of each element in a list.

def freqCount(li):
    frequency = {}
    for char in li:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency
# print(freqCount([2,5,2,7,4,7,9,9,2,4]))

# Question 6: Write a Python program to check if a number is prime.
def checkPrime(n):
    status = ""
    for x in range(2, n):
        if n % x == 0:    
            status = "Not a Prime Number"        
            break
        else:
            status = "Prime Number"
    return status
# print(checkPrime(11))  

# Question 7: Write a Python program to find the common elements between two lists.

def commonElement(l1, l2):
    commonEle = []
    for x in l1:
        if x in l2:
            commonEle.append(x)
    return commonEle

print(commonElement([1,2,3,4,5,6], [5,6,7,8,9] ))


# Question 8: Write a Python program to sort a list of elements using the bubble sort algorithm.




# Question 9: Write a Python program to find the second largest number in a list.



# Question 10: Write a Python program to remove duplicates from a list.



# 11. Converting a String of Integers into Decimals
import decimal
strs = "12345"
dec = decimal.Decimal(strs)
print(type(dec))

# 12. Reversing a String using an Extended Slicing Technique
string = "Python Programming"
rev_string = string[::-1]
# print(rev_string)


# 13. Counting Vowels in a Given Word
word = "programming"
vowels = "aeiou"
counter = 0
for char in word:
    if char in vowels:
        counter += 1
# print(counter)      

# 14. Counting Consonants in a Given Word
def countChars(word, type):
    vowel = "aeiou"
    charCount = {}
    for char in word:
        if type == 'Vowel':
            if char in vowel:
                charCount[char] = charCount.get(char, 0) + 1
        elif type == "Consonant":
            if char not in vowel:
                charCount[char] = charCount.get(char, 0) + 1
    return charCount

# print(countChars("programming", "Consonant")   )


# 15. Writing Fibonacci Series

def fibSeries(n):
    fib = [0, 1]
    for n in range(n):
        fib.append(fib[-1]+ fib[-2])
    return fib

# print(fibSeries(10))

# 16. Finding the Maximum Number in a List
def maxNumfromList(li, type):
    num = li[0]
    for nos in li:
        if type == 'largest':
            if nos > num:
                num = nos
        elif type == 'smallest':
            if nos < num:
                num = nos
    return num

# print(maxNumfromList([15, 85, 35, 89, 125], 'largest'))

# 17. Finding the Middle Element in a List
def middleElement(li):
    print(len(li)-1)
    mid = int(len(li)/2)
    print(mid)
    return li[mid]

# print(middleElement([1, 2, 3, 4, 5]))

# 18. Converting a List into a String
def listToString(li):
    string = "".join(li)
    return string
print(listToString(["P", "Y", "T", "H", "O", "N"]))


# 19. Adding Two List Elements Together
# lst1 = [1, 2, 3]
# lst2 = [4, 5, 6]
def addListElement(l1, l2):
    # import numpy as np
    # arr1 = np.array(l1)
    # arr2 = np.array(l2)
    # return arr1 + arr2
    newList = []
    if len(l1) < len(l2):
        for x in range(len(l2)):
            newList.append(l1[x]+l2[x])
    else:
        for x in range(len(l1)):
            newList.append(l1[x]+l2[x])
    return newList

# another approach

def addListAnotherApproach(l1, l2):
    return [x+y for x, y in zip(l1, l2)]
    

# print(addListAnotherApproach([1, 2, 3, 4], [4, 5, 6]))

# 20. Comparing Two Strings for Anagrams

def anagrams(w1):
    d1 = {}
    for char in w1:
        d1[char] = d1.get(char, 0) + 1
    return d1

# data1 = anagrams("heart")
# data2 = anagrams("earth")
# print("Data1: ", data1, "Data2: ", data2)
# if data1 == data2:
#     print("anagrams")
# else:
#     print("non anagrams")    

# another method:
def anagrams2(w1, w2):
    if list(w1.lower()).sort() == list(w2.lower()).sort():
        return "Anagrams"
    else:
        return "Non-anagram"
print(anagrams2("earth", "heart"))    


# Decorator

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Function: {func.__name__}")
        result = func(*args, **kwargs)
        return result
    return wrapper

@log_decorator
def greeting(name):
    return f"Hello {name}"

result = greeting("Python")
print(result)

l = [1,2,3,3,3,4,4,5,6,3,4,2,3]
lk = 0
for n in l:
    if l.count(n) == 1:
        lk = n 
print(lk)