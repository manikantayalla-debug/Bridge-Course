start , end = 2 , 50
count = 0
temp = start

while temp <=end:
    isPrime = True
    i = 2
    while i < temp:
        if temp % i == 0:
            isPrime = False
            break
        i+=1

    if isPrime:
        count+=1
    temp +=1

print(count)