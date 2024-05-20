import math
def isPrime(N):
    count = 0
    for i in range(1,N+1):
        if N%i==0:
            count += 1
    if count >2:
        print("False")
    else:
        print("True")
    
    
N = 24
isPrime(N)

#OPTIMAL APPROACH
def prime(N):
    count = 0
    sqrt = int(math.sqrt(N))
    for i in range(1,sqrt):
        if N%i==0:
            count +=1
            if i != N//i:
                count +=1
    if count >2:
        print("false")
    else:
        print("true")

N = 2
prime(N)
