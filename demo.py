from unittest import case

n1 = float(input("Enter a number 1: "))
n2 = float(input("Enter a number 2: "))

op = input("enter the operator (+ - * /): ")

try:
    match op:
        case "+":
            print(n1 + n2)
        case "-":
            print(n1 - n2)
        case "*":
            print(n1 * n2)
        case "/":
            if(n1 != 0 and n2 == 0):
                print("Cannot divide by zero")
                exit(1)
            print(n1 / n2)
        case _:
            print("invalid operator")
except ZeroDivisionError:
    print(0)






