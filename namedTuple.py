from collections import namedtuple

REC = namedtuple("Rec", ['name', 'age', 'job'])
bob = REC(name='Bob', age=42, job=['Developer', 'senior'])
print(bob)
print(bob.age)