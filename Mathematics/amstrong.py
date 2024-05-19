def amstrong(N):
    def extract(N):
        ans = []
        while N>0:
            lastDigit=N%10
            ans.append(lastDigit)
            N = N//10
        ans.reverse()
        return ans
    num = []
    num = extract(N)
    power = len(num)
    sum = 0
    for i in num:
        digit = int(i)
        sum += digit**power
    if N==sum:
        return True
    return False

sum = amstrong(125)
print(sum)