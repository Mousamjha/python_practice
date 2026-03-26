class Student:

    schoolName = "XYZ"  # static variable or class variable

    def __init__(self, name, rollNo):
        self.name = name  #instance variable
        self.rollNo = rollNo

    def printStudent(self):
        print(f"My name is {self.name} and roll no is {self.rollNo}")
        print(Student.schoolName)

    @staticmethod
    def printNos(x):
        for i in range(x): # i is local variable
            print(i)
    
    @classmethod
    def printSchoolName(pls):
        pls.schoolName = "ABC"
        print(pls.schoolName)


obj = Student("Mousam", 101)
print(obj.schoolName)
print(obj.name) 
print(obj.printStudent())       
# obj.printNos(10)
obj.printSchoolName()
print(obj.name)
print(Student.__dict__)