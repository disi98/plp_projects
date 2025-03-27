def opr(num1, num2, operator):
    if operator == '+':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operator == '-':
        print(f"{num1} + {num2} = {num1 - num2}")
    elif operator == '*':
        print(f"{num1} + {num2} = {num1 * num2}")
    elif operator == '/':
        print(f"{num1} + {num2} = {num1 / num2}")
    else:
        print('Invalid operator')

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter operator: ")
opr(num1, num2, operator)
#

