""""
Q 1. Left aligned  traingle
input =5
*
**
***
****
*****
---------------------

Q 2. Upper-left aligned  traingle
input=5
*****
****
***
**
*
---------------------

Q 3. Right aligned traingle
input=5
    *
   **
  ***
 ****
*****
----------------------

Q 4. Equilateral triangle
input=5
   *
  ***
 *****
*******
---------------------

Q 5. Ring Shape
input=5

   *
  ***
 *****
*******
 *****
  ***
   *

"""

# for i in range(1,18):
#     # i=3
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# for i in range(5,0,-1):
#     print(i)

#     *
#    **
#   ***
#  ****
# *****

# n=5

# for i in range(n,0,-1):
#     #  i=5
#     for j in range(i,1,-1):
#         print(" ",end=" ")
#     for i in range(1,n-i+2):
#         print("*",end=" ")
#     print()

#    *
#   ***
#  *****
# *******

# n=8
# incStart=2
# for i in range(n,0,-1):
#     #  i=5
#     for j in range(i,1,-1):
#         print(" ",end=" ")
#     for i in range(1,incStart):
#         print("*",end=" ")
#     print()
#     incStart=incStart+2

    
# class Animal:
#     name="animal"
#     lifeSpan=0

#     def showDetail(self):
#         print(f"The animal is {self.name} and life is {self.lifeSpan}")

# Horse=Animal()
# Horse.name="Horse"
# Horse.lifeSpan=70
# Horse.showDetail()

# # print(Horse.name)
# # print(Horse.lifeSpan)
# Lion=Animal()
# Lion.name="Babbar Sher"
# Lion.lifeSpan=90
# Lion.showDetail()

# Goat=Animal()
# Goat.showDetail()

# class Student:
#     def __init__(self,name,age,RollNumber):
#         self.name=name
#         self.age=age
#         self.rollNum=RollNumber
#     def showDetail(self):
#         print(f"My name is {self.name} and age is {self.age} and roll Number is {self.rollNum}")


# Std1=Student("Ayush",22,1101)
# Std2=Student("Suman",34,1102)

# Std1.showDetail()
# Std2.showDetail()


# Q 5. Ring Shape
# input=5

#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

# n=6
# # m=2
# for i in range(1,n):
#     for j in range(1,n-i):
#         print(" ",end=" ")
#     for k in range(1,2*i):
#         print("*",end=" ")
#     print()

# n=n-1
# m=n
# for i in range(1,n+2):
#     for k in range(1,i+1):
#         print(" ",end=" ")
#     for j in range(1,(2*m-2)):
#         print("*",end=" ")
#     print()
#     m=m-1

# n=12

# for i in range(1,n):
#     for j in range(1,n-i):
#         print(" ",end=" ")
#     for j in range(1,2*i):
#         print("*",end=" ")
#     print()
# m=n
# m=m-2
# for i in range(1,n-1):
#     for k in range(1,i+1):
#         print(" ",end=" ")
#     for j in range(1,(2*m)):
#         print("*",end=" ")
#     print()
#     m=m-1
    

#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

n=12
for i in range(1,n):
   for j in range(n-1,i,-1):
      print(" ",end=" ")
   for k in range(1,2*i):
      print("*",end=" ")
   print()

for i in range(1,n-1):
   for j in range(1,i+1):
      print(" ",end=" ")
   for k in range(1,2*(n-1)-2):
      print("*",end=" ")
   n=n-1
   print()
    







