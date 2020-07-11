from collections import Counter

#Find discriminant of any elliptic curve

def prime_factors(n):
    if n<0:
        n = -1*n
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return (factors, Counter(factors))



def disc(a1,a3,a2,a4,a6):
    b2 = a1**2+4*a2
    b4 = 2*a4 + a1*a3
    b6 = a3**2 + 4*a6
    b8 = (a1**2)*a6 + 4*a2*a6 -a1*a3*a4 + a2*a3**2 - a4**2
    discriminant = b2**2*(-b8) -8*(b4**3) - 27*(b6**2) + 9*b2*b4*b6
    if (discriminant<0):
        print("It is negative")
    else:
        print("It is positive")
    return(discriminant)

print(prime_factors(disc(-1,-4,-4,0,0)))
