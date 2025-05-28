# ayush=(8,)
# list1=[8,9,6,"rohan",9,78,56]
# dict1={
#     "Shivam":"Rohan",
#    "Age":56
# }

# print(type(ayush))
# print(type(list1))
# print(type(dict1))

# print(ayushtuple)
# print(ayushtuple[-2])

# print(len(ayushtuple))

# print(ayushtuple[len(ayushtuple)-3])
# print(ayushtuple[len(ayushtuple)-2]) //6
# print(ayushtuple[-2]) //6

tuple1=(8,9,6,"rohan",9,78,56,56)

# print(tuple1[-6:-2])
# print(tuple1[len(tuple1)-6:len(tuple1)-2])
# print(tuple1[:])
# for item in tuple1:
#     print(item)

list1= list (tuple1)
list1.append(89)
tuple1=tuple (list1)
print(tuple1)