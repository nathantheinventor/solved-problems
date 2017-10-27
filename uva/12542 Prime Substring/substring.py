primes = []
sieve = [True for i in range(100000)]
sieve[0] = False
sieve[1] = False
for i in range(4, 100000, 2):
    sieve[i] = False
for i in range(3, 317):
    if sieve[i]:
        for j in range(i * i, 100000, 2 * i):
            sieve[j] = False
for i in range(100000):
    if sieve[i]:
        primes.append(i)


n = input()
while n != "0":
    ans = 0
    l = len(n)
    for i in range(l):
        for j in range(1,6):
            x = int(n[i:i + j])
            if i + j <= l and x in primes:
                ans = max(ans, x)
    print(ans)
    n = input()