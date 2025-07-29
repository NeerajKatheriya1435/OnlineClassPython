# class Car:
#     company="Tesla" # class variables
#     def __init__(self,model,id):
#         self.model=model
#         self.id=id
        
    
#     def info(self):
#         self.company="Tata Motors"
#         print(f"This is {self.model} and company is {self.company}")


#     @staticmethod
#     def addTwo(num1,num2):
#         return num1+num2
    
#     def __str__(self):
#         return f"This is my string and characters are {len(self.model)}"
    
    
# obj1=Car("Safari Kumar",101)

# print(str(obj1))

# multiple Inheritance

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def showDetails(self):
        print(f"My name is {self.name} and age is {self.age}")

class Programmer:
    def __init__(self,skill):
        self.skill=skill
    
    def showDetails(self):
        print(f"My skill is {self.skill}")

class Hacker(Student,Programmer):
    def __init__(self, name, age,skill,id):
        # Student.__init__(self,name, age)
        # super().__init__(skill)
        super().__init__(name, age)
        Programmer.__init__(self,skill)
        self.id=id
    
    # def showDetails(self):
    #     print(f"My name is {self.name}")
    #     print(f"My age is {self.age}")
    #     print(f"My skill is {self.skill}")
    #     print(f"My id is {self.id}")

# ayushHacker=Hacker("Ayush",23,"python",1101)
# ayushHacker.showDetails()

print(Hacker.mro())
