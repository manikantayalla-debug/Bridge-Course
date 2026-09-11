a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))

if(a>=b and a > c):
    print(a)
elif(b>a and b >= c):
    print(b)
elif (a==b==c):
    print("All numbers are equal")
else:
    print(c)

