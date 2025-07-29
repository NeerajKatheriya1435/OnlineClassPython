class Person:
    def __init__(self,name,age,ayush):
        
        self.aysuh=ayush # public varible
        self._name=name  # protected varibles
        self.__age=age # private varibles
    
    def showDetails(self):
        print(f"My name is {self.__name} and age is {self.age}")

class Child(Person):
    def __init__(self, name, age,lang):
        super().__init__(name,age)
        self.lang=lang
    
    def showDetails(self):
        print(f"My name is {self.__name} and lang is {self.lang}")
        super().showDetails()

# Rohan=Child("Rohan",45,"Java")

# Rohan.showDetails()
# print(Rohan.age)
# Rohan.showDetails()
# print(Rohan._Person__name)

# public varaible -->outside the class in side class
# private varibles --> Inside class not outside not subclass
# proteted varibles --> Inside class subclass access not outside