# str1="My Name is {0} and age is {1}"
# name="Neeraj"
# age=59
# print(str1.format(age,name))

# name="Sumit"
# age=23
# weight=45.8967

# print(f"My Name is {name} and age is {age} weight is {weight:.3f} and plus is: {7+8}")
# print(f"My Name is {{name}} and age is {age} weight is {weight:.3f} and plus is: {7+8}")

# recursion
# its like a loop -->terminating condition

# 6!=> 6*5*4*3*2*1=720
# 5!=> 5*4*3*2*1=120

# printing a factorial

def fact(number):
    if(number==0 or number==1):
        return 1
    else:
        return number*fact(number-1)

print("The factorial is:",fact(6))

# fibbonicci series

# 0,1,1,2,3,5,8,13,21

# fact(5)==> 5*fact(4)
#             5*4*fact(3)
#             5*4*3*fact(2)
#             5*4*3*2*fact(1)
#             5*4*3*2*1=120

