import os

# sieve the primes
sieve = [True for i in range(100000)]
sieve[0] = False
sieve[1] = False
for i in range(4, 100000, 2):
    sieve[i] = False
for i in range(3, 100000, 2):
    if sieve[i]:
        for j in range(i * i, 100000, 2 * i):
            sieve[j] = False

primes = [i for i in range(100000) if sieve[i]]

############################################################

def primeFactors(n):
    os.system("factor {} > factors.txt".format(n))
    with open("factors.txt") as f:
        fact = [int(x) for x in f.read().split()[1:]]
        fact2 = {}
        for f in fact:
            if f not in fact2:
                fact2[f] = 0
            fact2[f] += 1
        return fact2

############################################################

def factors(n):
    pf = primeFactors(n)
    factors = [1]
    for p in pf:
        newFactors = []
        for f in factors:
            for i in range(pf[p] + 1):
                newFactors.append(f * p ** i)
        factors = newFactors
    return list(set(factors))

############################################################

def τ(n):
    return len(factors(n))

############################################################

def σ(n):
    return sum(factors(n))

############################################################

def isAbundant(n):
    return σ(n) > 2 * n

for _ in range(2, 29000):
    if isAbundant(_):
        print(_)