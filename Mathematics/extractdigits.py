import math
def extract(N):
    ans = []
    while N>0:
        lastDigit = N%10
        ans.append(lastDigit)
        N = math.floor(N/10)
    ans.reverse()
    return ans

N = 12345
digits = extract(N)
print("Extracted Digits:", end=" ")
for num in digits:
    print(num, end=" ")
print()



























