from math import sqrt

def isPrime(x: str) -> bool:
    x = int(x)
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
    
n = input()
while True:
    if isPrime(n):
        if isPrime(n[::-1]) and n[::-1] != n:
            print(n, "is emirp.")
        else:
            print(n, "is prime.")
    else:
        print(n, "is not prime.")
    try:
        n = input()
    except:
        break