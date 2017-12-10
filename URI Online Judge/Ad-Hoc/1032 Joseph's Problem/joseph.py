sieve = [False] * 2 + [True] * 999998
for i in range(4, 1000000, 2):
    sieve[i] = False
for i in range(3, 1000, 2):
    if sieve[i]:
        for j in range(i * i, 1000000, 2 * i):
            sieve[j] = False

primes = [i for i in range(1000000) if sieve[i]]

def solve(n):
    l = list(range(1, n + 1))
    pos = 1
    for p in primes[1:n]:
        del l[pos]
        pos = (pos + p - 1) % len(l)
    return l[0]
    
n = int(input())
while n > 0:
    print(solve(n))
    n = int(input())