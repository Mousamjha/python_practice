l = [3, 6, 8, 12, 14, 15]
result = [num*num for num in l]
# print(result)


# reverse string using while loop

string = "Mousam"
n_string = ''
i = len(string)
while i > 0:
    n_string = n_string + string[i - 1]
    i = i-1

# print(n_string)    

# reverse string using for loop
r_string = ''
for idx in range(len(string) - 1, -1, -1):
    r_string = r_string + string[idx]
# print(r_string)    


# reverse traversing in for loop
# for idx in range(10, -1, -1):
#     print(idx)

# apple
def reverseStringForLoop(string):
    r_string = ''
    for s in string:
        r_string = s + r_string
    return r_string
# print(reverseStringForLoop("apple"))

# reverse each word in statement
def reverseWord(statement):
    statement_list = statement.split()    
    rev = []
    for word in statement_list:
        r_word = ''
        for char in word:
            r_word = char + r_word
        rev.append(r_word)
    return (" ").join(rev)

# print(reverseWord("Love Python"))


def countN(string):
    string_l = string.split()
    repeated_string = []
    n = {}
    for word in string_l:
        # if string_l.count(word) > 1 and word not in repeated_string:
        #     repeated_string.append(word)
        n[word] = n.get(word, 0) + 1
    for k, v in n.items():
        if n[k] >=2:
            print(k, v)
    return n

# print(countN("latt latt latt app ap app dog cat lap cat"))

"""Write a program to sort characters and numbers so that first alphabets and then numbers are printed
input: A7B1R3
output: ABR137
"""

def sortChars(sting):
    numericChars = [char for char in sting if char.isalpha()]
    stringChars = [char for char in sting if char.isnumeric()]
    joined = sorted(numericChars)+ sorted(stringChars)
    return "".join(joined)
    print(joined)
print(len(str(10)))
    

def armStrongnumbers(start, end):
    numDigits = 0
    armstrongs = []
    
    for number in range(start, end):
        a_length = len(str(number))
        sumOfnthPower = 0
        for char in str(number):
            nthPower = int(char)**a_length
            # print(nthPower)
            sumOfnthPower += nthPower
        if sumOfnthPower == number:
            armstrongs.append(number)
        else:
            pass
    return armstrongs

print(armStrongnumbers(0,1000))

