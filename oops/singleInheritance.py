
class Parent:

    def m1(self):
        print("I am from parent class")


class Child(Parent):

    def m2(self):
        print("I am from child class")


# c = Child()
# c.m1()
# c.m2()


# Second example

class P:
    a = 10

    def __init__(self):
        print("Parent Class Constructor")
        self.b = 20

    def m1(self):
        print("Parent class instance method")

    @classmethod
    def m2(cls):
        print("Parent class Class Method")
        print(f"Class or Static variable: {cls.a}")

    @staticmethod
    def m3():
        print("Parent class Static Method")

class C(P):
    pass


c = C()
print(c.a)