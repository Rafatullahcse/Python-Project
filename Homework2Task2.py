num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 > 0 and num2 > 0:
    print("Both numbers are positive")
elif num1 < 0 and num2 < 0:
    print("Both numbers are negative")
elif num1 == 0 and num2 == 0:
    print("Both numbers are zero")
else:
    if num1 > 0:
        print("The first number is positive")
    elif num1 < 0:
        print("The first number is negative")
    else:
        print("The first number is zero")
    if num2 > 0:
        print("The second number is positive")
    elif num2 < 0:
        print("The second number is negative")
    else:
        print("The second number is zero")
