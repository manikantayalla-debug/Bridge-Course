n = int(input("Enter a no: "))
rev = 0
t=n
while n>0:
    rev = (rev *10) + n%10
    n //= 10


while(t>0):
    print(t%10,end="")
    t//=10
print()
print(rev)
