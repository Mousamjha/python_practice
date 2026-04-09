

class Outer:

    def __init__(self):
        print("Outer Class")

    
    class Inner:

        def __init__(self):
            print("Inner Class")

        def m1(self):
            print("Instance Method of Inner")


# Call Inner class instance method

obj = Outer()
innerObj = obj.Inner()
innerObj.m1()