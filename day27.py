
# class Employee:
#     name="Suman"
#     age=78
#     def showDetail(self):
#         print(f"My name is {self.name} and age is {self.age}")

# obj1=Employee()
# obj1.name="Suresh"

# obj1.showDetail()

# obj2=Employee()
# obj2.name="Mahesh"
# obj2.showDetail()

# print(obj1.name)
# print(obj1.age)
# obj1.name="Ayush"
# obj1.age=45

# obj2=Employee()
# obj2.name="Shyam"
# obj2.age=78

# obj1.showDetail()
# obj2.showDetail()

class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("Contsructor called")

    def showDetail(self):
        print(f"My name is {self.name} and age is {self.age}")
    
# obj=Employee()
obj1=Employee("Ayush",64)
obj2=Employee("Shubham",45)

obj1.showDetail()
obj2.showDetail()

# obj1.showDetail()