#Basic python usage
num1 = float(input("Enter a number:"))
num2 = float(input("Enter another number:"))
operator = input("Enter an operator (+, -, *, /):")

if operator == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

elif operator == '-':
    result = num1 =  num2
    print(f"{num1} - {num2} = {result}")

elif operator == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

elif operator == '/':
    if num2 !=0 and num1 >= num2:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allow or the denominator is less than numerator")
else:
    print("Invalid operator, Please use +, -, *, or /.")
