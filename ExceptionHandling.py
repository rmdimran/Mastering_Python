
try:
    num1 = float(input("Enter the first number : "))
    num2 = float(input("Enter the second number : "))

    result = num1 / num2
    print(result)
except ZeroDivisionError as err:
    print(err)
except ValueError as err:
    print("Invalid Input")