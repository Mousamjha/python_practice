a = 153
a_length = len(str(a))
sumOfnthPower = 0
for char in str(a):
    nthPower = int(char)**a_length
    # print(nthPower)
    sumOfnthPower += nthPower
if sumOfnthPower == a:
    print("Armstrong Number")
else:
    print("Not a armstrong number")
# print(sumOfnthPower)