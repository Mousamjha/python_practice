# with open("new.txt", '+a') as afile:
#     data = afile.readlines()
#     newString = "\nHello World !"
#     nos = afile.write(newString)
#     print(nos)


# with open("new.txt", "+br") as file:
#     text = file.readlines()
#     lineList = [line for line in text]
#     print(lineList)

# def outer():
#     x = 'old'
#     print(x)
#     def changer():
#         nonlocal x; x = 'new'
#         print(x)
#     return changer

# chang = outer()                
# chang
funcs = [lambda x: x**2, lambda x: x ** 3, lambda x: x*10]
# print(funcs)  # This will print the memory addresses like in your question

# # To read or use them:
# print(funcs )  # 11
# print(funcs )  # 20
x=10
for index, func in enumerate(funcs):
    print(f"At index {index +1 } = {func(x)}")

def addTwoNums(a = 2, b = 4):
    yield [a + b, a-b]

data = addTwoNums()
print(data)

l = [1,2,3,4]
for i, f in enumerate(l):
    print(f"at index {i} = {f}")