# is there is any error in python program

userIndex=input("Enter the index: ")

try:
    list1=[7,45,89,23]
    print(list1[int(userIndex)])
# except ValueError:
#     print("Value Error in program")
# except IndexError:
#     print("Index Error in program")
except Exception as e:
    print(e)
print("Very Very Important lines")
print("Very Very Important lines")
print("Very Very Important lines")