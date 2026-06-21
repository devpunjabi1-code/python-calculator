a = float(input("Enter a number here: "))
b = float(input("Enter a number here: "))

choice = input("enter operators(+,-,X,/,^,sqroot,%): ")

if (choice == "+"):
    print(a+b)
elif (choice == "-"):
    print(a-b)
elif (choice == "X"):
    print(a*b)
elif (choice == "/"):
    if (b == 0):
        print("Invalid number.")
    else:
        print(a/b)
elif (choice == "^"):
    print(a**b)
elif (choice == "sqroot"):
    import math
    print(math.sqrt(a))
elif (choice == "%"):
    if (b == 0):
        print("Invalid number.")
    else:
        print((a/b)*100 ,"%")
else:
    print("Invalid Operation")

