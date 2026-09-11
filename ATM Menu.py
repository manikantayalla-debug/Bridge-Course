account_bal = 0.0

while True:
    userInput = int(input("""
                             1 : Check Balance
                             2 : Deposit
                             3 : Withdraw
                             4 : Exit"""))
    match userInput:
        case 1:
            print(f"Your Balance is: {account_bal}")

        case 2:
            amount = float(input("Enter amount to deposit: "))
            if amount <= 0:
                print("Invalid amount")
                continue
            account_bal += amount
            print(f"Your updated Balance is: {account_bal}")
        case 3:
            amount = float(input("Enter amount to withdraw: "))
            if(amount > account_bal):
                print("Amount is greater than your balance")
                continue
            elif(amount <= 0):
                print("Invalid amount")
                continue
            account_bal -= amount
            print(f"Your updated Balance is: {account_bal}")
        case 4:
            break


