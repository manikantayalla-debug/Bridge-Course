
while True:
    userInput = input("Enter option (+,-,*,/,! {factorial}) : ")
    match userInput:
        case "+":
            n1 = int(input("Enter num1: "))
            n2 = int(input("Enter num2: "))
            print(n1 + n2)

        case "-":
            n1 = int(input("Enter num1: "))
            n2 = int(input("Enter num2: "))
            print(n1 - n2)

        case "*":
            n1 = int(input("Enter num1: "))
            n2 = int(input("Enter num2: "))
            print(n1 * n2)

        case "/":
            n1 = int(input("Enter num1: "))
            n2 = int(input("Enter num2: "))
            print(n1 / n2)

        case "!":
            n1 = int(input("Enter num1: "))
            fact = 1
            for i in range(1,n1+1):
                fact *= i
            print(fact)


        case "exit":
            exit()

        case _:
            print("Invalid input")