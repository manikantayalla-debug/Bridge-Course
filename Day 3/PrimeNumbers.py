start,end = 2, 50
count = 0
temp = start
while temp!=end:
    isPrime = True
    t = start
    start+=1
    i=2
    while i < t:
        if t % i == 0:
            isPrime = False
            break
    if isPrime:
        count +=1
    temp +=1
print(count)
