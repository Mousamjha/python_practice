

class Students:

    def __init__(self, marks, name):
        self.name = name
        self.marks = marks

    
    def display(self):
        print(f"Student Name: {self.name} and roll no: {self.marks}")


class ExtraMarks:

    def neatnessMarks(stud):
        print(stud.__dict__)
        stud.marks = stud.marks + 10
        stud.display()


obj = Students(32, 'A')
ExtraMarks.neatnessMarks(obj)