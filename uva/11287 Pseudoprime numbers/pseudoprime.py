from math import sqrt
from fractions import gcd

def powMod(base: int, exp: int, mod: int) -> int:
    if exp < 4:
        return (base ** exp) % mod
    tmp = powMod(base, exp // 2, mod) ** 2
    if exp % 2 == 1:
        tmp *= base
    return tmp % mod

def isPrime(x: int) -> bool:
    if x < 2:
        return False
    if x < 4:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(sqrt(x) + 1), 2):
        if x % i == 0:
            return False
    return True

p,a = map(int,input().split())
while (p,a) != (0,0):
    if powMod(a, p, p) == a % p and not isPrime(p) and a % p != 0:
        print("yes")
    else:
        print("no")
    
    p,a = map(int,input().split())