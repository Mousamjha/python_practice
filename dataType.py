""" I am learning Python
 with Papa 

   1. Basic DataType 
        a. int
        b. string 
        c. float
        d. bool
   2. Sequence Datatype 
        a. list
        b. tuple
        c. dict
    """

#integer
# heere a is called identifier or variable which 
a = 1
print(type(a))

#float
b = 1.0
print(type(b))

# string
c = 'siddhant'
print(type(c))

# bool
d = True
print(type(d))

# def sum(a, b):
#     return a + b

# sumVal = sum(10, 5)
# print(f"The sum is {sumVal}")

#sequence datatype 
# List []
lst = [1, 2, 3, 4, 5, "Orange", "Apple", 10.5, True]
print(type(lst))
lst.append("siddhant")
print(lst)

# Tuple ()
tup = (1,2,3,"Orange", "Apple", 10.0, False)
print(type(tup))
print(tup)

#Dictionary {key: value}
d = {"Class": "VII", "Section": "E", "Students": ["Siddhant", "Mousam", "Goutam", "Sujata"]}
print(d['Students'])
print(d["Class"])

print(f"{d["Students"][3]} studies in class {d["Class"]} and section {d["Section"]}")



