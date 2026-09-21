n = int(input("Enter a number: "))

print(len(str(n)))
digits  = 0

while n>0:
    n//=10
    digits += 1

print(digits)
