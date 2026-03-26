

"""
    Create a module named basicmaths having four functions named add, sub, mult, and div. 
    All these functions take two arguments as numbers. Import the module in the main program 
    and call the respective function depending on the user requirement and return the computed result.
"""
class Calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def sum(self):
        return self.a + self.b
    
    def mul(self):
        return self.a * self.b
    
    def sub(self):
        if self.a < self.b:
            return self.b - self.a
        else:
            return self.a - self.b
        
    def div(self):
        return self.a / self.b
    
obj = Calculator(4, 2)
print(obj.div())