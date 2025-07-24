
# without using decorators

# def namePrint():
#     print("Ayush Kumar")

# def greetFunc(namePrint):
#     print("Good Morning Sir")
#     namePrint()
#     print("Bye Bye Sir/Mam")

# greetFunc(namePrint)
# def decoratorAyush(printName):
#     def WrapperFunc():
#         print("Hello sir")
#         printName()
#         print("Bye Bye")
#     return WrapperFunc


# @decoratorAyush
# def printName():
#     print("Shubham Singh")

# printName()
def ayushDecor(addTwoNum):
    def wrapperFunc(*args):
        # print(*args)
        print("****************")
        addTwoNum(*args)
        print("****************")
    return wrapperFunc

@ayushDecor
def addTwoNum(num1,num2):
    print("The sum is: ",(num1+num2))

addTwoNum(3,9)