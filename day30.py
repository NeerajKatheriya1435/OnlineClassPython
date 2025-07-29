# class Animal:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
    
#     def showDetails(self):
#         print(f"My name is {self.name} and age is {self.age}")

#     @property
#     def getName(self):
#         return self.name

#     @getName.setter
#     def setValue(self,str):
#         if(str.isalpha()): # This string should charact a-z or A-Z
#             self.name=str
#         else:
#             self.name="Not Set"

# obj1=Animal("Ayush",78)

# print(obj1.name)  # getting the value
# obj1.name=123456 # setting the value
# print(obj1.name)

# obj1.showDetails()
# print(obj1.getName) # recomended way for getting the value
# obj1.setValue="Ratna"
# print(obj1.getName)



class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def showDetails(self):
        print(f"My name is {self.name} and age is {self.age}")

class Child(Person):
    def __init__(self, name, age,lang):
        super().__init__(name,age)
        self.lang=lang
    
    # def showDetails(self):
        # print(f"My name is {self.name} and lang is {self.lang}")
        # super().showDetails()


Rohan=Child("Rohan",45,"Java")
Rohan.showDetails()


