from math import sqrt

def isPrime(x):
    if x <= 1:
        return False
    elif x <= 3:
        return True
    if x % 2 == 0:
        return False
    for p in range(3, int(sqrt(x) + 1), 2):
        if x % p == 0:
            return False
    return True

def isSuperPrime(x):
    if not isPrime(x):
        return False
    for c in str(x):
        # print(c, isPrime(int(c)))
        if not isPrime(int(c)):
            return False
    return True

n = int(input())
while True:
    if isSuperPrime(n):
        print("Super")
    elif isPrime(n):
        print("Primo")
    else:
        print("Nada")
    try:
        n = int(input())
    except:
        break