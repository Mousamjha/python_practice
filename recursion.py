def reverseCount(n):
    nums = []
    if n == 0:
        return
    
    return nums.append(reverseCount(n-1))
    
# print(reverseCount(10))

def printName(n, name):
    if n == 0:
        return
    print(name)
    return printName(n-1, name)

# printName(10, 'Mousam')


def facto(n):
    if n == 1:
        return 1
    return n * facto(n-1)

# print(facto(5))

def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n-1)+fib(n-2)
# for nos in range(1,11):
#     print(fib(nos))

def sumofnNos(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return (n+ sumofnNos(n-1))

print(sumofnNos(5))

print(10.0//2)
n = 2E3
print(type(n))

