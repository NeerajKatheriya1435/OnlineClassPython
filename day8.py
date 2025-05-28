
userInp1=int(input("Enter the number: "))

match userInp1:
    case 1:
        print("Today is Monday")
    case 2:
        print("Today is Tuesday")
    case 3:
        print("Today is Wednesday")
    case _ if userInp1>90:
        print("Please Enter number less than 90")
    case _ if userInp1>30:
        print("Please Enter number less than 30")
    case _:
        print("Please Input number between 1 to 3")