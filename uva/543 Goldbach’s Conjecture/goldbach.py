sieve = [True] * 1000001
sieve[:1] = [False, False]
sieve[4::2] = [False] * len(sieve[4::2])

for i in range(3, 1000, 2):
    if sieve[i]:
        sieve[i*i::2*i] = [False] * len(sieve[i*i::2*i])

primes = [i for i in range(1000001) if sieve[i]]
primeSet = {i for i in range(1000001) if sieve[i]}

n = int(input())
while n > 0:
    for i in primes:
        if n - i in primeSet:
            print("{} = {} + {}".format(n, i, n - i))
            break
    n = int(input())