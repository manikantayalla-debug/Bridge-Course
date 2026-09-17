
def fact(x):
    if x == 1 or x == 0:
        return 1

    return x*fact(x-1)

print(fact(5))

square = lambda x=3: x*x
print(square())

x,y = input("Enter two numbers: ").split(" ")
x,y = int(x),int(y)
print(x,y)
print(type(x), type(y))
