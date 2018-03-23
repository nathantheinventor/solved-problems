sieve = [True] * 10001
sieve[0] = False
sieve[1] = False
sieve[4::2] = [False] * len(sieve[4::2])
for i in range(3, 100, 2):
    sieve[i*i::2*i] = [False] * len(sieve[i*i::2*i])

primes = [x for x in range(10000) if sieve[x]]
ans = [0] * 10001
for i in range(len(primes)):
    tmp = primes[i]
    ans[tmp] += 1
    for p in primes[i+1:]:
        tmp += p
        if tmp <= 10000:
            ans[tmp] += 1
        else:
            break

n = int(input())
while n > 0:
    print(ans[n])
    n = int(input())