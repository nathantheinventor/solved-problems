sieve = [True for i in range(10 ** 6)]
sieve[:1] = [False, False]
sieve[4::2] = [False] * len(sieve[4::2])

for i in range(3, 10 ** 3, 2):
    sieve[i * i::2 * i] = [False] * len(sieve[i * i::2 * i])

primes = [i for i in range(10 ** 6) if sieve[i]]

print(len(primes))
def isCircular(p):
    x = str(p)
    for i in range(len(x)):
        tmp = int(x[i:] + x[:i])
        if tmp not in primes:
            return False
    return True

for p in primes:
    if isCircular(p):
        print(p)

#print(circular[:20])