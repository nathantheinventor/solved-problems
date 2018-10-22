from math import sqrt
def isPrime(x):
    if x < 2:
        return False
    if x < 4:
        return True
    if x % 2 == 0:
        return False
    if x % 3 == 0:
        return False
    for i in range(5, int(sqrt(n) + 2), 6):
        if x % i == 0:
            return False
        if x % (i + 2) == 0:
            return False
    return True

t = int(input())
for _ in range(t):
    m, n = map(int, input().split())
    for i in range(m, n + 1):
        if isPrime(i):
            print(i)
    if _ != t - 1:
        print("")