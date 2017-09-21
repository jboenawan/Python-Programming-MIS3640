def gcd(a,b):
    number = 2
    if a % number != 0 and b % number != 0:
        return number+1 
    else:
        return gcd(a,b)
print(gcd(6,12))
