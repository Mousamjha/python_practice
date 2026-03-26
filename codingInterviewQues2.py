"""Write a code to reverse a number"""
"****Method 1***"
number = 908701
reversed_num = int(str(number)[::-1])
# print(reversed_num)

"****Method 2***"
def reverseNumber(number):
    reverse = 0
    tmp = number
    while number > 0:
        remainder = number % 10
        print("Remainder", remainder)
        reverse = (reverse * 10) + remainder
        number = number // 10
        print(f"Number: {number}")
    return reverse

# print(reverseNumber(908701))

"""Write the code to find the Fibonacci series upto the nth term."""
"""
Example for n = 10:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34 
"""
def fibSeries(number):
    if number <= 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibSeries(number-1) + fibSeries(number-2)

# for x in range(10):
#     print(fibSeries(x), end=" ")    


"""Write code to Calculate frequency of characters in a string"""

def calculateFrequency(string):
    frequency = {}
    for char in string:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency

# print(calculateFrequency("hello"))

def nonRepeatingChar(string):
    frequency = {}
    for char in string:
        frequency[char] = frequency.get(char, 0) + 1
    for k, v in frequency.items():
        if v == 1:
            print(f"{k} is non-repeating character")

# print(nonRepeatingChar("swiss"))

"""Write a code to replace a substring in a string."""
def replaceSubstring(string):
    return string.replace('world', 'python')

# print(replaceSubstring("hello world"))







def fibSeries(n):
    fib = [0, 1]
    for num in range(1, n):
        fib.append(fib[-1]+fib[-2])
    return fib

print(fibSeries(10))