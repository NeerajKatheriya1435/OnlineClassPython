# with open('sample.txt', 'w') as f:
#     f.write('Hello World! Durgesh Ayush is smart Enough')
#     f.truncate(5)

# with open('sample.txt', 'r') as f:
#     print(f.read())


# def square(num1):
#     return num1*num1

# square=lambda a:a+8
# cube=lambda a,b,c:a+b+c
# # print(square(5))
# print(cube(3,6,5))

# def addTwoNum(funcGreet,num1,num2):
#     print(funcGreet(6))
#     print("Hello The sum is",(num1+num2))

# # def greet():
# #     print("Hello Sir Godd Morning")
# durgesh=lambda x:x+2

# addTwoNum(durgesh,12,10)

# from functools import reduce
# list1=[2,4,7,5]

# 0,1,1,2,3,5,8,13,21


# def square(num1):
#     return num1+5

# squaredList=list(map(lambda x:x*x,list1))

# squaredList=list(filter(lambda x:x>3,list1))
# sum=reduce(lambda x,y:x*y,list1)
# print(sum)

# a=[7,87,9]
# b=[7,8,9]
a="Suman"
b="Suman"
print(a is b)
print(a == b)
