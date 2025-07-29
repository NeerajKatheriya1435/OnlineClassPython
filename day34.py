class Student:
    def __init__(self,name):
        self.name=name

class Result(Student):
    def __init__(self, name,marks1,marks2):
      super().__init__(name)
      self.marks1=marks1
      self.marks2=marks2

    def showMarks(self):
        print(f"Name is {self.name}")
        print(f"Marks 1 is {self.marks1}")
        print(f"Marks 2 is {self.marks2}")
    

class FinalPecentage(Result):
    def __init__(self, name, marks1, marks2,RollNumber):
        super().__init__(name, marks1, marks2)
        self.RollNumber=RollNumber

    def showPerntage(self):
        self.total=self.marks1+self.marks2
        print(f"The total marks {self.total}")

newStd=FinalPecentage("Shubham",34,56,111101)
# newStd.showMarks()
newStd.showPerntage()