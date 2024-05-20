import math
## brute force
def divisors(N):
    div = []
    for i in range(1,N+1):
        if N%i ==0:
            div.append(i)
    return div

N = 24
list1 = divisors(N)
for i in list1:
    print(i)


## OPTIMAL APPROACH
def divopt(N):

    div = []
    sqrt = int(math.sqrt(N))
    for i in range(1,sqrt+1):
        if N%i==0:
            div.append(i)
            if i != N//i:
                div.append(N//i)
    return div
print("opt")

N = 36
list1 = divopt(N)
for i in list1:
    print(i)