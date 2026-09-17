def add(n1, n2):
    print(n1 + n2)

def sub(n1, n2):
    print(n1 - n2)

def div(n1, n2):
    print(n1 / n2)

def mul(n1, n2):
    print(n1 * n2)


def calculator(operator):
    match operator:
        case "+":
            n1 = int(input("Enter num1: "))
            n2 = int(input("Enter num2: "))
            add(n1, n2)

        case "-":
            n1 = int(input("Enter num1: "))
            n2 = int(input("Enter num2: "))
            sub(n1, n2)

        case "*":
            n1 = int(input("Enter num1: "))
            n2 = int(input("Enter num2: "))
            mul(n1,n2)

        case "/":
            n1 = int(input("Enter num1: "))
            n2 = int(input("Enter num2: "))
            div(n1,n2)

        case _:
            print("Invalid operator")


user_input = input("Enter operator (+, - , * ,/)")
calculator(user_input)
