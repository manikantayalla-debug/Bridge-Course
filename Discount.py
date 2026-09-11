age = int(input("Enter your age: "))

ticket_price = 500

if age < 12:
    ticket_price *= 0.9
    print("You are eligible for 10% discount and your ticket price : ",ticket_price)
else:
    print("Not discount for you and ticket price: ",ticket_price)
