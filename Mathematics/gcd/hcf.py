def hcf(a,b):
    gcd = 1
    for i in range(min(a,b),1,-1):
        if a%i ==0 and b%i == 0:
            gcd = i
    return gcd

def lcm(a,b,gcd):
    lcm = 1
    lcm = a*b/gcd
    return lcm
gcd = hcf(9,12)
print(gcd)
lcm = lcm(9,12,gcd)
print(lcm)