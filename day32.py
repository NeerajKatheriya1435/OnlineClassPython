class Car:
    company="Tesla" # class variables
    def __init__(self,model,id):
        self.model=model
        self.id=id
        
    
    def info(self):
        self.company="Tata Motors"
        print(f"This is {self.model} and company is {self.company}")


    @staticmethod
    def addTwo(num1,num2):
        return num1+num2
    
    
obj1=Car("Safari",101)
# print(Car.addTwo(6,4))

# Car.info(obj1)
# obj1.info()

# obj2=Car("Suzuki",102)
# obj2.info()
# Car.company="Hundai"
# print(Car.company)

# print(Car.addTwo(5,7))

# print(Car.addTwo(obj1,7,9))

# print(obj1.__dict__)

# print(dir(obj1))

list1=[8,67,6]
# print(dir(list1))
help(list1.remove)