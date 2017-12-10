# sieve the primes
sieve = [True for i in range(1000000)]
sieve[0] = False
sieve[1] = False
for i in range(4, 1000000, 2):
    sieve[i] = False
for i in range(3, 1000000, 2):
    if sieve[i]:
        for j in range(i * i, 1000000, 2 * i):
            sieve[j] = False

primes = [i for i in range(1000000) if sieve[i]]

############################################################

def primeFactors(n):
    factors = {}
    for p in primes:
        if n % p == 0:
            factors[p] = 1
            n //= p
        while n % p == 0:
            factors[p] += 1
            n //= p
        if n in primes:
            factors[n] = 1
            n //= n
        if n == 1:
            break
    return factors

############################################################

def product(l):
    ans = 1
    for i in l:
        ans *= i
    return ans

n, k = map(int, input().split())

fact = primeFactors(n)
if sum([fact[x] for x in fact]) < k:
    print(-1)
else:
    factors = []
    for f in fact:
        for _ in range(fact[f]):
            factors.append(f)
    ans = factors[:k-1]
    p = factors[k-1:]
    ans.append(product(p))
    print(*ans)